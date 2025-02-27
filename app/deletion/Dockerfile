FROM  python:3.12-slim AS installer 

WORKDIR /app

RUN apt-get update && apt-get install -y \
    pkg-config default-libmysqlclient-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt



# stage 2
FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    default-mysql-client \
    && rm -rf /var/lib/apt/lists/*

COPY --from=installer /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages

WORKDIR /app

COPY templates /app/templates
COPY app.py /app

EXPOSE 5000

CMD ["python3", "app.py"]