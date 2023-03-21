# Welcome to the Meme.AI backend!

## Introduction

This repository contains code to run our AI Meme Generator.

## Setting up Environment

To run the Meme Generator, you will have to set up a Python environment and required enviornment variables.

## Setting up Python Environment

The Meme Generator has been tested using Python `3.9`.
If you are able to get this running on an older version of Python, or the Meme Generator fails to run
on a later version, please open an issue and we will look into it.

You can set up your Python envrionment using any method (e.g., Poetry, pipenv, conda, etc.), but please
make sure you have **all** packages from `requirements.txt` installed. 

**NOTE**: We have only tested `virtualenv` and `pipenv`. 
If you have success with other methods, please let us know and we can add instructions here!

### Setting up Envrionment using virtualenv

1. Create a virtual env `virtualenv ~/memesAI`
2. Activate by running `source ~/memesAI/bin/activate`
3. Import all the requirements from requirements.txt through `pip install -r requirements.txt`

### Setting up Envrionment using pipenv

1. Within this directory, run the following command: `pipenv shell`. This will create a new virtual environment and
activate it.
2. Install all requirements from `requirements.txt` via `pipenv install -r requirements.txt`.

## Setting up Environment Variables

The Meme Generator requires three environment variables: `WEAVIATE_URL`, `ACCESS_TOKEN`, and `OPENAI_API_KEY`.
Please note that without these, the Meme Generator may start up, but will not run.
These can be set manually, or you can run the script `set-env-vars` to set them by running `source set-env-vars`.

**NOTE**: Before running `set-env-vars`, please make sure to set the variables in the script.

## Test Querying and Connecting to Weaviate Instance

Prior to running the Meme Generator, you should test whether you can connect to the Weaviate instance and issue queries.
There are two scripts that can be used to do this: `bin/weaviate_test.py` and `bin/weaviate_query_test.py`.

### Test Connection
If you would like to test whether you can connect to the Weaviate instance, you can run `bin/weaviate_test.py`. 
This script should print out the schema on Weaviate upon successfully connecting to the Weaviate instance.

### Test Querying
If you would like to test whether you can query the Weaviate instance, you can run `bin/weaviate_query_test.py`. 
If the script returns two descriptions and saves two image files, you are good to go.

If you run into any issues here, please first check if you can connect to the Weaviate instance. 
If you can successfully connect, please double check your `OPENAI_API_KEY` key and make sure there are no issues there.

## Running the App

The application can be run using the following command: `python manage.py runserver`

**NOTE**: Currently, when you connect to `http://127.0.0.1:8000/`, you should see a `Page not found` error. 
This is expected as we currently do not have a default page.
Once we have a default page, this will disappear.
Thanks!