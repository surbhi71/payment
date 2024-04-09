# Use the official Python image as a base
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /payment

# Copy the requirements file into the container at /payment
COPY requirements.txt /payment/

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /payment
COPY . /payment/

# Expose the port on which the Flask app will run
EXPOSE 5001

# Command to run the Flask application
CMD ["python", "app.py"]
