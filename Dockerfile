 # Use the Python 3.9 slim-buster base image
FROM python:3.9-slim-buster 

# Set the working directory inside the container to /app
WORKDIR /app

# Copy the requirements.txt file from the current directory to /app
COPY requirements.txt .  

# Install the Python dependencies specified in requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt  

# Copy all the files from the current directory to /app
COPY . .  

 # Set the environment variable FLASK_RUN_HOST to 0.0.0.0
ENV FLASK_RUN_HOST=0.0.0.0 

# Expose port 5000 for the Flask application to listen on
EXPOSE 5000  

# Run the command "flask run" to start the Flask application
CMD [ "flask", "run" ]  
