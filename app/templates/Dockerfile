FROM ubuntu:latest

RUN apt update && apt upgrade -y && \
    apt install -y python3 python3-pip python3.12-venv \
    pkg-config libmysqlclient-dev mysql-server && \
    rm -rf /var/lib/apt/lists/*  # Cleanup to reduce image size

WORKDIR /home/ubuntu

# Creating a virtual environment and install packages
RUN python3 -m venv phonebook && \
    ./phonebook/bin/pip install --upgrade pip && \
    ./phonebook/bin/pip install flask flask_mysqldb

COPY . ./phonebook

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 5000

CMD ["/entrypoint.sh"]
