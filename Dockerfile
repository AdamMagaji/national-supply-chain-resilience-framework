# Use a secure, lightweight official base image
FROM python:3.11-slim

# Set environment variables for stable container behavior
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Copy dependency structures
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy system code
COPY . /app/

# Run the system validation test on startup
CMD ["python", "app.py"]
