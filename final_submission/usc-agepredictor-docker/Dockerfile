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
			git \
      tar \
			wget && \
		apt dist-upgrade -y

# Clone AgePredictor
RUN git clone https://github.com/USCDataScience/AgePredictor.git

# Create directory for user data volume
#RUN mkdir /data

# Set work director
WORKDIR /AgePredictor

# Download and extract Apache Spark 2.0.0
RUN wget https://archive.apache.org/dist/spark/spark-2.0.0/spark-2.0.0-bin-hadoop2.7.tgz && \
    tar xvzf spark-2.0.0-bin-hadoop2.7.tgz

# Set Spark environment var
ENV SPARK_HOME="spark-2.0.0-bin-hadoop2.7"

# Download OpenNLP models used
RUN chmod +x bin/download-opennlp.sh && \
    ./bin/download-opennlp.sh

# Install AgePredictor
RUN mvn clean install

# Ensure execution permission of data processing scripts
RUN chmod +x data-processing-scripts/scripts/*

# Copy files to data dir
COPY data/* /AgePredictor/data/
