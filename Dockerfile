FROM python:3.13-alpine

ENV PYTHONUNBUFFERED=1

# Install OCR tools and dependencies
RUN apk add --no-cache \
    tesseract-ocr \
    tesseract-ocr-data-eng \
    tesseract-ocr-data-deu \
    poppler-utils \
    jpeg-dev \
    zlib-dev \
    tiff-dev \
    libxml2 \
    libxslt \
    gcc \
    musl-dev \
    libffi-dev

# Set Tesseract language data path (Alpine-specific)
ENV TESSDATA_PREFIX=/usr/share/tessdata

# Set working directory
WORKDIR /workspace

# Copy project files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the main script
CMD ["python", "main.py"]
