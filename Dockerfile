# Use Python base image
FROM python:3.11

# Set working directory inside the container
WORKDIR /app

# Copy project files into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Define default command
CMD ["python", "src/app.py"]
