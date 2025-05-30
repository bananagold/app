FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy files
COPY fixssl.py .
COPY certificates/ ./certificates/

# Install Flask
RUN pip install flask

# Expose HTTPS port
EXPOSE 80

# Run app
CMD ["python", "fixssl.py"]
