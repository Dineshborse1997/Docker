# Use an official Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy app.py into the container
COPY app.py .

# Install Flask
RUN pip install flask

# Expose port 5000
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
