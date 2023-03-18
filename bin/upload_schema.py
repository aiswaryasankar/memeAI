#!/usr/bin/env python3

"""
Create schema and add to Weaviate instance
"""

import os
import json

import weaviate

WEAVIATE_URL = os.getenv('WEAVIATE_URL')
CLIENT_CONFIG = None

if WEAVIATE_URL:
    # If a URL is provided, assume this is our remote instance
    # and check for an access token.
    access_token = os.getenv('ACCESS_TOKEN')
    if not access_token:
        raise ValueError("ACCESS_TOKEN environment variable not set. " \
            "This is needed to log into the Weaviate instance.")
    CLIENT_CONFIG = weaviate.AuthBearerToken(
        access_token=access_token,
        expires_in=300 # this is in seconds, by default 60s
        )
else:
    WEAVIATE_URL = 'http://localhost:8080'

print(f"Connecting to a weaviate instance at the following URL: {WEAVIATE_URL}")

SCHEMA = None
with open('weaviate-schema/schema.json', 'r') as f:
    SCHEMA = json.load(f)

print(SCHEMA)

client = weaviate.Client(WEAVIATE_URL, auth_client_secret=CLIENT_CONFIG) 

print("Delete old schema...")

old_schema = client.schema.get('Meme')
if old_schema['classes'] != 0:
    client.schema.delete_class("Meme")

print("Adding schema to Weviate...")

client.schema.create(SCHEMA)

print("Added schema to Weviate!")

schema = client.schema.get()

print("Dumping schema...")
print(json.dumps(schema, indent=4))