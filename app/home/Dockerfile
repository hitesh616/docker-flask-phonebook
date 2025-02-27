# Stage 1: Install dependencies
FROM python:3.7-alpine AS installer

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt -t /app/dependencies

# Stage 2: Build the final image
FROM python:3.7-alpine 

WORKDIR /app

# Copy installed dependencies from installer stage
COPY --from=installer /app/dependencies /usr/local/lib/python3.7/site-packages

# Copy application files
COPY templates /app/templates
COPY app.py /app

# Expose port 5000
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
