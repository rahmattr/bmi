# Simple BMI Calculator

A Simple BMI Calculator REST API

## Installation 

From a `bash` shell

```bash 
  virtualenv venv
  . venv/bin/activate
  pip3 install -r requirements.txt
  uvicorn main:app
```

######
## Deployment with Docker

To deploy this project with `docker` run

```bash
  docker build -t simplebmicalc .
  docker run -d --rm -it -v $(pwd):/app -p 8000:8000 --name simplebmicalc simplebmicalc start
  # How to See the Logs
  docker logs --follow --tail=1000 simplebmicalc
```
## API Reference

#### Calculate BMI

```http
  POST /bmi
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `height` | `int` | **Required**. Height in Centimeters|
| `weight` | `int` | **Required**. Weight in Kilograms |

## Authors

- [@rahmattr](https://www.github.com/rahmattr) .

  
