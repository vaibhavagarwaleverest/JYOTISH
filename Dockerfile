# Use an official .NET runtime image as the base image
FROM mcr.microsoft.com/dotnet/sdk:7.0 AS dotnet-build
WORKDIR /app

# Install Python, pip, and venv
RUN apt-get update && apt-get install -y python3 python3-pip python3-venv

# Create a virtual environment
RUN python3 -m venv /app/venv

# Activate the virtual environment and upgrade pip
ENV PATH="/app/venv/bin:$PATH"
RUN pip install --upgrade pip

# Copy the requirements file and install Python dependencies
COPY backend/requirement.txt .
RUN pip install -r requirement.txt

# Copy the rest of the application code
COPY . .

# Set the working directory to the backend
WORKDIR /app/backend

# Expose the port your application will run on
EXPOSE 8000

# Set the entry point for the application
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8000"]