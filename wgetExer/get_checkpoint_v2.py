import os
import tarfile
import urllib.request

VERSION = "v2"
SAVEDIR = "checkpoints"

CHECKPOINTS = [(1.4, 224), (1.3, 224)]
for multiplier in [1.0, 0.75, 0.5, 0.35]:
    for input_size in [224, 192, 160, 128, 96]:
        CHECKPOINTS.append((multiplier, input_size))


def download_checkpoint(multiplier, input_size):
    modelname = "mobilenet_{}_{}_{}".format(VERSION, multiplier, input_size)
    url = "https://storage.googleapis.com/mobilenet_v2/checkpoints/{}.tgz".format(modelname)
    print("Downloading...", url)
    if not os.path.exists(os.path.join(SAVEDIR, modelname)):
        os.makedirs(os.path.join(SAVEDIR, modelname))
    tar_path = os.path.join(SAVEDIR, modelname, os.path.basename(url))
    urllib.request.urlretrieve(url, tar_path)
    print("Extract ", tar_path)
    with tarfile.open(tar_path, mode='r') as tar:
        tar.extractall(os.path.dirname(tar_path))


def download_all():
    for multiplier, input_size in CHECKPOINTS:
        download_checkpoint(multiplier, input_size)


def main():
    if not os.path.exists(SAVEDIR):
        os.mkdir(SAVEDIR)
    download_all()

if __name__ == '__main__':
    main()
