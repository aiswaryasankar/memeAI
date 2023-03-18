# Welcome to the Meme.AI backend!

## Introduction

This repository contains code to run our AI meme generator.

## Setting up Environment

## Setting up Python Environment

1. Create a virtual env `virtualenv ~/memesAI`
2. Activate by running `source ~/memesAI/bin/activate`
3. Import all the requirements from requirements.txt through `pip install -r requirements.txt`

## Setting up Environment Variables

The meme generator requires three environment variables: `WEAVIATE_URL`, `ACCESS_TOKEN`, and `OPENAI_API_KEY`.
These can be set manually, or you can run the script `set-env-vars` to set them by running `source set-env-vars`.

NOTE: Before running `set-env-vars`, please make sure to populate the variables in the script.

## Running the App

The application can be run using the following command: `python manage.py runserver`

## Testing Weaviate

If you would like to test the weaviate instance, you can run `bin/weaviate_query_test.py`. 
If the script returns two descriptions and saves two image files, one with a squirrel and one with Leonardo DiCaprio, you are good to go.
