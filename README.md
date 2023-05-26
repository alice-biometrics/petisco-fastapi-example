# petisco-fastapi-example 🍪 [![Pull Request (CI)](https://github.com/alice-biometrics/petisco-fastapi-example/actions/workflows/pull-request.yml/badge.svg)](https://github.com/alice-biometrics/petisco-fastapi-example/actions/workflows/pull-request.yml) [![codecov](https://codecov.io/gh/alice-biometrics/petisco-fastapi-example/branch/main/graph/badge.svg?token=N5FKUF17GU)](https://codecov.io/gh/alice-biometrics/petisco-fastapi-example)


<img src="https://github.com/alice-biometrics/custom-emojis/blob/master/images/alice_header.png?raw=true" width=auto>

[Petisco](https://github.com/alice-biometrics/petisco) is a framework for helping Python developers to build clean 
Applications in Python.

This repository is an example on how to take advantage of `pestico` framework on a 
[fastapi](https://github.com/tiangolo/fastapi) project.


## Installation

We strongly recommend to use venv in order to isolate your environment in your computer.
Additionally, we use the [lume](https://github.com/alice-biometrics/lume) package to manage all our command.

```console
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $ pip install lume
(venv) $ lume -install
```

## Testing ✅ 

The easiest way is to launch all tests with lume or pytest:

| lume                  | pytest            |
|-----------------------|-------------------|
| `(venv) $ lume -test` | `(venv) $ pytest` |

Or you can also run the tests by their type:

| lume                                                                                                  | pytest                                                                                             |
|-------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| `(venv) $ lume -test-unit`<br/>`(venv) $ lume -test-integration`<br/>`(venv) $ lume -test-acceptance` | `(venv) $ pytest -m unit`<br/>`(venv) $ pytest -m integration`<br/>`(venv) $ pytest -m acceptance` |


## Run it locally 💻

Run the application in your computer with:

| lume                  | pytest            |
|-----------------------|-------------------|
| `(venv) $ lume -local:run` | `(venv) $ python -m uvicorn app.main:app --reload` |

Try it and check documentation in [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

👉 Check the [lume.local.yml](lume.local.yml) if you need to extend your local run command (e.g add some environment variables.)

## Docker <img src="https://github.com/alice-biometrics/custom-emojis/blob/master/images/docker.png" width="18">

#### Build

| lume                  | docker                                                                    |
|-----------------------|---------------------------------------------------------------------------|
| `(venv) $ lume -docker:build` | `(venv) $ docker build -t petisco-fastapi-example -f docker/Dockerfile .` |


#### Use docker compose 

Use docker compose to run the service and its dependencies locally

| lume                     | docker                                                                    |
|--------------------------|---------------------------------------------------------------------------|
| `(venv) $ lume -docker:compose-up` | `(venv) $ docker-compose -f docker-compose.yml up -d` |

Try it and check documentation in [http://localhost:80/docs](http://localhost:80/docs)

#### Check RabbitMQ <img src="https://github.com/alice-biometrics/custom-emojis/blob/master/images/rabbitmq.png" width="18">

If you run docker compose, you can manage and check RabbitMQ queues in [http://localhost:15672/](http://localhost:15672/).

Credentials `guest:guest`

## Practice makes perfect 🤓

This project is ideal for getting started on petisco and fastapi development using hexagonal architecture in Python. 
Let's start playing with this repo. Find here some exercises to extend this application:

* Implement other TaskRepository using SQL, Redis, Elastic or whatever you like. 
* Implement other TaskLabeler using a simple NPL model.
* Implement more complex TaskLabeler with several labelers and publish additional events
* Subscribe to events and perform model modifications

Add your implementation to [dependencies.py](app/petisco/dependencies.py) and start playing with the project.

## Contact 📬

support@alicebiometrics.com
