# XXX is this the best base image?
FROM nvidia/cuda:11.6.2-base-ubuntu20.04
RUN apt-get update -y && apt-get install -y python3 python3-pip git && \
    pip install git+https://github.com/cloneofsimo/lora.git@v0.1.7 && \
    pip install diffusers==0.14 && \
    pip install accelerate==0.20.3


