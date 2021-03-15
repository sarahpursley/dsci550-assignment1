FROM maven:3-jdk-8

# Set bash to default shell
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

# Do not prompt apt for user input when installing packages
ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies
RUN apt update && \
		apt install -y \
			build-essential \
			software-properties-common \
			python3 \
			python3-venv && \
		apt dist-upgrade -y

# Create virtualenv and add to path for default
ENV VIRTUAL_ENV=/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Copy repo from home (local changes have been made to the code)
COPY ./tika-img-similarity/ /tika-img-similarity/

# Change working directory
WORKDIR /tika-img-similarity

# Upgrade pip
RUN python -m pip install --upgrade pip

# Install python packages
#RUN pip install --no-dependencies \
RUN pip install -r requirements.txt

# Copy over input
COPY ./input/ /tika-img-similarity/input/
# Make output directory and mount volume
RUN mkdir /output
VOLUME /output
