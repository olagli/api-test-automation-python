# API Test Automation Project (with Python and pytest)

## Overview
This project contains automated API tests for a public REST API:
https://jsonplaceholder.typicode.com

It demonstrates basic API testing practices using Python and pytest.

## What is tested in this project
- GET /users
- POST /posts
- PUT /posts/{id}
- DELETE /posts/{id}

Includes:
- status code validation
- response structure checks
- parametrized tests
- pytest fixtures

## Project structure
api-tests/
  api/
    -client.py
  tests/
    -test_users.py
    -test_posts.py
  conftest.py
  README.md

## Install dependencies
pip install requests pytest

## Run tests with
pytest -v
or
py -m pytest -v

## Notes
- The API used is a mock service and may return inconsistent responses for PUT/DELETE.
- Fixtures are used to reuse test data.
- Parametrization is used to avoid duplication.

