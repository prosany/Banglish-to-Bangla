# Use an official Python runtime as the base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the FastAPI app into the container
COPY server.py .

# Expose port 7077
EXPOSE 7077

# Run the app using Uvicorn with FastAPI on port 7077
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "7077"]
