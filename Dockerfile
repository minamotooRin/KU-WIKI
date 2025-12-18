FROM python:3.11-slim

# Install system dependencies and clean up in single layer
RUN apt-get update && \
    apt-get install -y --no-install-recommends git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Create non-root user for security
RUN useradd -m -s /bin/bash mkdocs

WORKDIR /app

# Copy and install dependencies first (for better layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY --chown=mkdocs:mkdocs . .

# Switch to non-root user
USER mkdocs

# Expose the default MkDocs port
EXPOSE 8000

# Default command
CMD ["mkdocs", "serve", "--dev-addr=0.0.0.0:8000"]
