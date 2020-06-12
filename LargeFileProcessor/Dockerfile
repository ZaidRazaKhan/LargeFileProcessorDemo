# For more information, please refer to https://aka.ms/vscode-docker-python
FROM openjdk:8

ENV PYTHON_VERSION=3.7.3
ENV PYSPARK_PYTHON=python3
ENV PYSPARK_DRIVER_PYTHON=python3
ENV PRODUCT_DB_IP 'localhost'
ENV PRODUCT_FILE_ID '' 

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

# RUN apt-get install -y python3.7 python3.7-dev python-3.7-pip
# RUN rm -rf /var/lib/apt/lists/*

RUN apt-get update
RUN apt-get install -y build-essential
RUN apt-get install -y libffi-dev 
RUN apt-get install -y zlib1g-dev 
RUN apt-get install -y libssl-dev 


WORKDIR /usr/src

RUN wget https://www.python.org/ftp/python/$PYTHON_VERSION/Python-$PYTHON_VERSION.tgz

RUN tar xzf Python-$PYTHON_VERSION.tgz

WORKDIR /usr/src/Python-$PYTHON_VERSION

RUN ./configure --enable-optimizations --with-ensurepip=install

RUN make altinstall

RUN ln -s /usr/local/bin/python3.7 /usr/local/bin/python3
# RUN ln -s /usr/local/bin/python3.7 /usr/local/bin/python
RUN ln -s /usr/local/bin/pip3.7 /usr/local/bin/pip3
RUN ln -s /usr/local/bin/pip3.7 /usr/local/bin/pip
RUN ln -s /usr/local/bin/python3.7 /usr/bin/python3
# RUN ln -s /usr/local/bin/python3.7 /usr/bin/python
# RUN ln -s /usr/local/bin/pip3.7 /usr/bin/pip3
# RUN ln -s /usr/local/bin/pip3.7 /usr/bin/pip
# RUN ln -snf /bin/bash /bin/sh

SHELL ["/bin/bash", "-c"]

RUN pip install --user virtualenv
RUN python3 -m venv large-file-processor-env
RUN cat large-file-processor-env/bin/activate
RUN source large-file-processor-env/bin/activate
# RUN source  large-file-processor-env/bin/activate

RUN pip --version
RUN python --version
RUN pip --version
RUN python3 --version
RUN /usr/bin/python3 --version

WORKDIR /usr/local/src/pyspark-java8

RUN rm -rf /usr/src/Python-$PYTHON_VERSION
RUN rm -rf /usr/src/Python-$PYTHON_VERSION.tgz

# Install pip requirements
ADD requirements.txt .
# RUN /bin/bash -c "python -m pip install -r requirements.txt"
RUN python3 -m pip install -r requirements.txt
RUN cat requirements.txt
# RUN python3 import mysql.connector
WORKDIR /app
ADD . /app

RUN rm -rf /usr/local/src/pyspark-java8

# Switching to a non-root user, please refer to https://aka.ms/vscode-docker-python-user-rights
RUN useradd appuser && chown -R appuser /app
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["python3", "driver.py ${PRODUCT_DB_IP} ${PRODUCT_FILE_ID}"]
