# import Python Docker Image with Python
FROM python:3.6.5

# set the maintaner of this Dockerfile
MAINTAINER FirstName LastName "your.email@gmail.com"

# set the app directory
WORKDIR /usr/src/app

# copy all files to app directory
COPY . ./

# install Python packages for the app and the app server
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir gunicorn

# run the app with app server
CMD [ "gunicorn", "-c", "gunicorn.conf", "app:web_app" ]
