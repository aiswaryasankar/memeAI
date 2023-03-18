#!/usr/bin/env python3

"""
Test if Weaviate instance is up and running

Copied from https://github.com/weaviate/weaviate-examples/blob/main/nearest-neighbor-dog-search/weaviate-test.py
"""

import os
import logging
from logtail import LogtailHandler
import base64

import weaviate
handler = LogtailHandler(source_token="tvoi6AuG8ieLux2PbHqdJSVR")
logger = logging.getLogger(__name__)
logger.handlers = []
logger.addHandler(handler)
logger.setLevel(logging.INFO)

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

logger.info(f"Connecting to a weaviate instance at the following URL: {WEAVIATE_URL}")

client = weaviate.Client(WEAVIATE_URL, auth_client_secret=CLIENT_CONFIG)
schema = client.schema.get()

logger.info(f"Schema: {schema}")

logger.info("You can succesfully connect to the weaviate instance!")