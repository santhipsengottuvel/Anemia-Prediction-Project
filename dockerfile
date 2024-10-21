FROM python:3.8-buster 

# Set the working directory
WORKDIR /app

# Copy requirements.txt first for better caching
COPY requirements.txt ./

# Install system dependencies
RUN apt-get update -y && \
    apt-get install -y build-essential libatlas-base-dev awscli && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Run the application
CMD ["python", "app.py"]