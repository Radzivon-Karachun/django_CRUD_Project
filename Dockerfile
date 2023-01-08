# base image
FROM python:3.10

# setup environment variable
ENV DockerHOME=/app

# set work directory
RUN mkdir -p $DockerHOME

# where your code lives
WORKDIR $DockerHOME

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip

COPY requirements.txt /app/requirements.txt
# run this command to install all dependencies
RUN pip install -r requirements.txt

# copy whole project to your docker home directory.
COPY . $DockerHOME

# port where the Django app runs
EXPOSE 8000

CMD ["python", "manage.py", "migrate"]
# start server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]