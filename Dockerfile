FROM python:3.11-slim

WORKDIR /app

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY main.py .
COPY static/ ./static/

# Expose port
EXPOSE 8000

# Run the application
CMD ["python", "main.py"]
