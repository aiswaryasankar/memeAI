#!/usr/bin/env python3

"""
Test if Weaviate instance contains objects by querying for
meme descriptions similar to `Happy`
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

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is required for uploading objects to Weaviate")

CLIENT = weaviate.Client(WEAVIATE_URL,
                         auth_client_secret=CLIENT_CONFIG,
                         additional_headers={"X-OpenAI-Api-Key": OPENAI_API_KEY})

def weaviate_text_search(text):
    """
    This function uses the nearText operator in Weaviate
    """
    source_text = { "concepts": text }

    weaviate_results = CLIENT.query.get("Meme", ["description", 'image']).with_near_text(source_text).with_limit(2).do()

    logger.info(weaviate_results)
    return weaviate_results["data"]["Get"]["Meme"]

logger.info(f"Connecting to a weaviate instance at the following URL: {WEAVIATE_URL}")

query_results = weaviate_text_search('Sad')

logger.info(query_results)

for i, res in enumerate(query_results):
    description = res['description']
    logger.info(f"Description: {description}")
    decoded_img = base64.b64decode(res['image'])
    with open(f'query-result-image-{i}.png', 'wb') as f:
        f.write(decoded_img)

logger.info("If you see descriptions and their corresponding images has been saved successfully, " \
      "you can succesfully query the weaviate instance!")




