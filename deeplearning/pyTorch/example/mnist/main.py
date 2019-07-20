# taken from https://github.com/pytorch/examples/blob/master/mnist/main.py
import argparse
import torch
from torch import nn
from torch.nn import functional as F
from torch import optim
from torchvision import datasets, transforms
from torch.autograd import Variable


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 10, kernel_size=5)
        self.conv2 = nn.Conv2d(10, 20, kernel_size=5)
        self.conv2_drop = nn.Dropout2d()
        self.fc1 = nn.Linear(320, 50)
        self.fc2 = nn.Linear(50, 10)

    def forward(self, x):
        x = F.relu(F.max_pool2d(self.conv1(x), 2))
        x = F.relu(F.max_pool2d(self.conv2_drop(self.conv2(x)), 2))
        x = x.view(-1, 320)
        x = F.relu(self.fc1(x))
        x = F.dropout(x, training=self.training)
        x = self.fc2(x)
        return F.log_softmax(x, dim=1)


def train(args, kwargs):
    torch.manual_seed(args.seed)
    if args.cuda:
        torch.cuda.manual_seed(args.seed)

    train_loader = torch.utils.data.DataLoader(
        datasets.MNIST('./data', train=True, download=True,
                       transform=transforms.Compose([
                           transforms.ToTensor(),
                           transforms.Normalize((0.1307,), (0.3081,))
                       ])),
        batch_size=args.batch_size, shuffle=True, **kwargs)

    model = Net()
    if args.cuda:
        model.cuda()

    optimizer = optim.SGD(model.parameters(), lr=args.lr,
                          momentum=args.momentum)

    for epoch in range(1, args.epochs+1):
        model.train()
        for batch_idx, (data, target) in enumerate(train_loader):
            if args.cuda:
                data, target = data.cuda(), target.cuda()
            data, target = Variable(data), Variable(target)
            optimizer.zero_grad()
            output = model(data)
            loss = F.nll_loss(output, target)
            loss.backward()
            optimizer.step()
            if batch_idx % args.log_interval == 0:
                print('Train Epoch: {}[{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                    epoch, batch_idx*len(data), len(train_loader.dataset),
                    100. * batch_idx/len(train_loader), loss.data[0]))

    return model


def test(args, kwargs, model):
    model.eval()
    test_loss = 0
    correct = 0
    test_loader = torch.utils.data.DataLoader(
        datasets.MNIST('./data', train=False, transform=transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize((0.1307,), (0.3081,))
        ])),
        batch_size=args.test_batch_size, shuffle=True, **kwargs)
    for data, target in test_loader:
        if args.cuda:
            data, target = data.cuda(), target.cuda()
        data, target = Variable(data, volatile=True), Variable(target)
        output = model(data)
        test_loss += F.nll_loss(output, target, size_average=False).data[0]
        pred = output.data.max(1, keepdim=True)[1]
        correct += pred.eq(target.data.view_as(pred)).long().cpu().sum()

    test_loss /= len(test_loader.dataset)
    print('\nTest set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format(
        test_loss, correct, len(test_loader.dataset),
        100. * correct / len(test_loader.dataset)))


def parse_argument():
    parser = argparse.ArgumentParser(description="PyTorch MNIST Example")
    parser.add_argument('--batch_size', type=int, default=64,
                        metavar='N', help='input batch size for training')
    parser.add_argument('--test_batch_size', type=int, default=1000,
                        metavar='N', help='input batch size for testinf')
    parser.add_argument('--epochs', type=int, default=10,
                        metavar='N', help='number of epochs to train')
    parser.add_argument('--lr', type=float, default=0.01,
                        metavar='LR', help='learning rate')
    parser.add_argument('--momentum', type=float, default=0.5,
                        metavar='M', help='SGD momentum')
    parser.add_argument('--no-cuda', action='store_true',
                        default=False, help='disable CUDA training')
    parser.add_argument('--seed', type=int, default=1,
                        metavar='S', help='random seed')
    parser.add_argument('--log_interval', type=int, default=10, metavar='N',
                        help='how many batches to wait before logging training status')
    args = parser.parse_args()
    args.cuda = not args.no_cuda and torch.cuda.is_available()
    return args


def main():
    args = parse_argument()
    kwargs = {'num_workers': 1, 'pin_memory': True} if args.cuda else {}
    trained_model = train(args, kwargs)
    test(args, kwargs, trained_model)


if __name__ == '__main__':
    main()
