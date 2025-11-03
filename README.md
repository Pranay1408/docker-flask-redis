# Docker Flask + Redis Project

![Docker](https://img.shields.io/badge/Docker-Ready-blue)
![Python](https://img.shields.io/badge/Python-3.11-green)
![Flask](https://img.shields.io/badge/Flask-Up-lightgrey)
![Redis](https://img.shields.io/badge/Redis-7-orange)

---

## Overview

This project is a **mini microservice** using **Flask + Redis**, running inside **Docker containers**.
It demonstrates how a Python API can interact with Redis for counting visits, fully containerized and ready for cloud deployment.

---

## Features

* Count visitor hits via Redis
* Reset counter anytime
* Multi-container setup with Docker Compose
* Fully portable and easy to deploy on **AWS EC2**

---

## Endpoints

| URL      | Description                    |
| -------- | ------------------------------ |
| `/`      | Welcome message                |
| `/count` | Increment and view visit count |
| `/reset` | Reset the counter to 0         |

---

## Deployment

* Already configured for **Docker Compose**.
* Can be deployed on any Linux server, including **AWS EC2**.
* Use `docker-compose up -d` to start both Flask and Redis containers.

---

## Notes

* Make sure **port 5000** (Flask) and **6379** (Redis) are open if running on cloud instances.
* Environment variables are set in the Dockerfile for Redis host and port.
* Works seamlessly with **Terraform + Ansible** setup if deployed on cloud.

---

## Author

Arpit (Your friendly DevOps learner 😎)
