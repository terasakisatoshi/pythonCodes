import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 6, 5)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1 = nn.Linear(16*5*5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        x = F.max_pool2d(F.relu(self.conv1(x)), (2, 2))
        x = F.max_pool2d(F.relu(self.conv2(x)), 2)
        x = x.view(-1, self.num_flat_features(x))
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

    def num_flat_features(self, x):
        size = x.size()[1:]
        num_features = 1
        for s in size:
            num_features *= s
        return num_features


def main():
    net = Net()
    print(net)
    params=list(net.parameters())
    inp=Variable(torch.randn(1,1,32,32))
    out=net(inp)
    print(out)
    net.zero_grad()
    target=Variable(torch.arange(1,11))
    criterion=nn.MSELoss()
    loss=criterion(out,target)
    loss.backward()

    print('conv1.bias.grad after backward')
    print(net.conv1.bias.grad)

if __name__ == '__main__':
    main()
