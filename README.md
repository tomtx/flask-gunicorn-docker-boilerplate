# Boilerplate for Containerized Python Web App
> This is a boilerplate for containerized Python backend app aimed for production environments. It has **Flask** as a Python micro web framework, a **Gunicorn** as a Python Web Server Gateway Interface (WSGI) HTTP server, and a **Docker** as a container technology to package up this application. Consider connecting this web app with some reverse proxy, such as **Nginx** web server, to provide high performance & stability under real production loads.

## Instructions
Run the following Docker commands from the project root.
```
docker build -t web-app:latest .
docker run -d -p 5858:5858 web-app
```

## Requirements
* Docker 18+
