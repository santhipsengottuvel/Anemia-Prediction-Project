FROM python:3.11-buster

# Set the working directory
WORKDIR /app
COPY . /app
# Copy requirements.txt first for better caching
COPY requirements.txt ./

# Install system dependencies
RUN apt-get update -y && \
    apt-get install -y build-essential libatlas-base-dev awscli && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install --default-timeout=100 --retries 5 --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Run the application
CMD ["python3", "app.py"]