# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.6

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# Set the working directory to /src
WORKDIR /src

# Copy the requirements file into the container at /src
ADD requirements.txt /src

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt