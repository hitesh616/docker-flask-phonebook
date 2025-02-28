# Docker Flask Phonebook

This is a simple phonebook application built with Flask and Docker. The application allows users to add, view, and delete contacts. The application is divided into three microservices: `phonebook-home`, `phonebook-register`, and `phonebook-deletion`.

## Prerequisites

- Docker
- Docker Compose

## Project Structure

docker-flask-phonebook/
            │
            ├── app/
            |    └── home/
            |         		└── templates/
            |               			└── index.html
            |         		└──Dockerfile
            |         		└── app.py
            |         		└── requirements.txt
            |
            |    └── register/
            |        		└──Dockerfile
            |        		└── app.py
            |        		└── requirements.txt
            |
            |    └── deletion/
            |        		└── templates/
            |               			└── view_contacts.html
            |        		└──Dockerfile
            |        		└── app.py
            |        		└── requirements.txt
           ├── nginx/
            |        	└──Dockerfile
            |        	└── nginx-proxy.conf
           ├── docker-compose.yml

## Setup

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/docker-flask-phonebook.git
cd docker-flask-phonebook

2. **Replace TestPassword and TestUsername with the actual password for the MySQL user in Docker Compose file.**

3. **Build and run the Docker containers:**

```bash
docker-compose up --build

This command will build the Docker images and start the containers for the application and Nginx.
```
