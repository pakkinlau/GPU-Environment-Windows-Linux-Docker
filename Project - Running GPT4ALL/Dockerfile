# Use an official NVIDIA CUDA base image with Python 3
# You can find a list of docker image on "latest CUDA" section on docker hub: https://hub.docker.com/r/nvidia/cuda
# PS1: It is not necessary to match base image OS with the host OS. Here, I use ubuntu 22.04 for longer support and compatibility with other packages.
# PS2: There are superset relationship between image options: Devel > Runtime > Base
# 'runtime' image contains base image and also CUDA runtime libraries. 
# 'deval' image contains extra libraries that help compile CUDA code.
# 'base' image is a bare miminum, and you need to install CUDA libraries manually.
# Here, I choose 'runtime' image.

FROM nvidia/cuda:12.3.2-cudnn9-runtime-ubuntu22.04

# Set environment variables to non-interactive 
# (this prevents some prompts asking yes or no questions)
ENV DEBIAN_FRONTEND noninteractive
# Set the PATH and LD_LIBRARY_PATH for the CUDA Toolkit (if necessary)
# Note: These are usually set by the base image.
ENV PATH /usr/local/cuda-12.3/bin:${PATH}
ENV LD_LIBRARY_PATH /usr/local/cuda-12.3/lib64:${LD_LIBRARY_PATH}

# Install system dependencies
# PS: 'sudo' is not necessary in docker container.
# Using `apt-get` to install python3.11 and more. 
# (the last step clean up the app package files to reduce image size)
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.11 python3.11-venv python3.11-dev \
    build-essential libssl-dev zlib1g-dev libbz2-dev \
    libreadline-dev libsqlite3-dev wget curl llvm \
    libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev \
    libffi-dev liblzma-dev git ca-certificates && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Set virtual environment variable
# Create a virtual environment and activate it
# Make sure we use the virtualenv
ENV VIRTUAL_ENV /opt/venv
RUN python3.11 -m venv $VIRTUAL_ENV
ENV PATH "$VIRTUAL_ENV/bin:$PATH"

# Upgrade GLIBC to the latest version (if necessary)
# RUN add-apt-repository ppa:ubuntu-toolchain-r/test && \
#     apt-get update && \
#     apt-get upgrade -y libc6

# Install NVIDIA drivers (if necessary) and CUDA Toolkit
# Note: These steps are typically not needed in a CUDA base image.
# The base image already includes the necessary CUDA libraries and tools.

# Install PyTorch with CUDA support
# --no-cache-dir is used to reduce the image size
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu113

# Install Jupyter
RUN pip install --no-cache-dir jupyter notebook jupyterlab
# Expose the port Jupyter will run on
EXPOSE 8888


# Set the working directory in the container
# Copy the local directory contents to the container's working directory
WORKDIR /app
COPY . /app

# Install any needed packages specified in requirements.txt
# Make sure you have a requirements.txt with gpt4all and any other dependencies listed
RUN pip3 install gpt4all

# In step 0, it is just an empty file. But later we will use command to complete it. 
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
# maybe put all required package on requirements.txt later. 

# Run JupyterLab
# --no-browser: prevent Jupyter lab from automatically opening the server in a web browser
# --allow-root: This allows Jupyter Lab to be run as the root user. 
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root"]