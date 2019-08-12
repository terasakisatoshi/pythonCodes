#
# Yeah I know, I should have created Dockerfile for this example
#
docker run --rm -it \
    -v $PWD:/work \
    -w /work \
    ubuntu:16.04 /bin/bash -c "\
    apt-get update && apt-get install -y \
    python3 python3-pip && \
    pip3 install pytest && \
    pip3 install . && \
    pytest"