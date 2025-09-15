SHELL := /bin/bash

APP ?= app.main:app
HOST ?= 127.0.0.1
PORT ?= 8000

install:
	poetry install

s serve:
	poetry run uvicorn $(APP) --reload --host $(HOST) --port $(PORT)
