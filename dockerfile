# Use a lightweight Ubuntu base
FROM ubuntu:22.04

# Install required tools
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        gdb \
        binutils \
        build-essential \
    && rm -rf /var/lib/apt/lists/*

# Create and set working directory
WORKDIR /home/bomb

# Copy all bomb-related files into the container
COPY . /home/bomb

# By default, run gdb so you can debug safely
# You can override at runtime: docker run ... <other cmd>
CMD ["gdb", "--args", "./bomb"]