# Use the new base image
FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PADDLEX_FONT_DIR=/tmp/paddlex_fonts


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
    libgl1 \
    && apt-get clean

# Install PaddlePaddle and PaddleOCR
RUN python -m pip install --no-cache-dir \
    paddlepaddle==3.0.0 -i https://www.paddlepaddle.org.cn/packages/stable/cpu/ && \
    python -m pip install --no-cache-dir paddleocr==3.0.0

# Grant write permissions to site-packages fonts directory (Fix for PermissionError)
RUN chmod -R a+w /usr/local/lib/python3.12/site-packages/paddlex/utils/fonts

# Set working directory
WORKDIR /workspace

# Copy project files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the main script
CMD ["python", "main.py"]


