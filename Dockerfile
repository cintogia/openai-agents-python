# Use Python 3.11 as base image for better compatibility
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Create and activate virtual environment
RUN python -m venv env
ENV PATH="/app/env/bin:$PATH"
ENV VIRTUAL_ENV="/app/env"

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install openai-agents
RUN pip install --no-cache-dir 'openai-agents'

# Install development dependencies
RUN pip install --no-cache-dir ruff mypy mkdocs mkdocstrings griffe

# Copy the application code
COPY . .

# Load environment variables from .env file
COPY .env .
ENV $(cat .env | xargs)

# Set the default command
CMD ["python", "-m", "examples.pm_agent.main"]