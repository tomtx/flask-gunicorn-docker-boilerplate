# Boilerplate for Containerized Python Web App
> This is a boilerplate for containerized Python backend app aimed for production environments. It has **Flask** as a Python micro web framework, a **Gunicorn** as a Python Web Server Gateway Interface (WSGI) HTTP server, and a **Docker** as a container technology to package up this application. APIs are exposed via an *app server* that runs from Docker container by asynch operations that are threaded.

> FYI, users of this boilerplate should consider connecting this web app with some web server, such as **Nginx** reverse proxy, to provide high performance & stability under real production loads.

## Instructions
1) Run the following Docker commands, to build the Docker image & run the Docker container, from the project root.
```
docker build -t web-app:latest .
docker run -d -p 5858:5858 web-app
```
2) Go to the following URI in your browser to see the functional **Swagger** of this app.
```
localhost:5858/app
```
3) You should see some Swagger like this. Also, you can run that one sample authentication API included there. This should return the "Python hello world!" message in the repsonse body (no payload necessary).

<img src="swagger-screenshot.png" align="center" width="800">

## Requirements
* Docker CE 18+
