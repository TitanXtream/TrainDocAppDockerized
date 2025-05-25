# Use the new base image
FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye

# Set environment variables
ENV PYTHONUNBUFFERED=1
# This can be removed since we are switching to PaddleOCR

# Install system dependencies for PaddleOCR
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    build-essential \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libglib2.0-0 \
    libpoppler-cpp0v5 \
    libjpeg-dev \
    libz-dev \
    && apt-get clean

# Install PaddlePaddle and PaddleOCR
RUN pip install --no-cache-dir paddlepaddle paddleocr

# Set working directory
WORKDIR /workspace

# Copy project files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the main script
CMD ["python", "main.py"]
