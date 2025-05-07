# Use official Python image
FROM python:3.11-slim

# Set work directory inside container
WORKDIR /app

# Copy only requirements first (if you have), then install (faster builds)
COPY requirements.txt .

# Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy all your application code
COPY . .

# Expose Flask port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
