# Simple Python Flask Application for running inside containers #

Build the image -

```bash
$ docker build -t flask-app:latest .
```

Run the Docker container -

```bash
$ docker run -d -p 5000:5000 flask-app:latest
```
