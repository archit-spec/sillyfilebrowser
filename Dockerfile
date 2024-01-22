# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Create the "uploads" directory inside the container
RUN mkdir uploads

# Copy the requirements file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask app code to the container
COPY . .

# Expose the port that the Flask app will be listening on
EXPOSE 5000

# Set the command to run the Flask app
CMD ["python", "app.py"]
