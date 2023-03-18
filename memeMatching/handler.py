from django.http.response import JsonResponse
from rest_framework.response import Response
import logging
from .serializer import *
from logtail import LogtailHandler
from datetime import datetime
import openai
import weaviate
import os
from idl import *


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


def hello_world(helloWorldRequest):
  """
    Demo function for testing purposes
  """
  logger.info(helloWorldRequest)
  logger.info(helloWorldRequest.name)


def match_text_to_meme(matchTextToMemeRequest):
  """
    Generate meme text for a given input text
  """

  try:
    emotionalDescription = "Describe the emotional value of this text " + str(generateTextForMemeRequest.InputText)

    memeQueryText = openai.Completion.create(
      engine="text-davinci-003",
      prompt=emotionalDescription,
      temperature=0.7,
      max_tokens=500,
      n=1,
      stop=None,
      frequency_penalty=0,
      best_of=1,
      presence_penalty=0,
    )

    logger.info("Meme query text: " + str(memeQueryText))

    # Use that text to match with memes
    source_text = { "concepts": memeQueryText.choices[0].text }

    weaviate_results = CLIENT.query.get("Meme", ["description", 'image']).with_near_text(source_text).with_limit(2).do()

    logger.info("Weaviate results: " + str(weaviate_results))

    # Return the meme URL and description
    return MatchTextToMemeResponse(
      Memes=weaviate_results["data"]["Get"]["Meme"],
      Error=None,
    )

  except Exception as e:
    return MatchTextToMemeResponse(
      Memes=[],
      Error=str(e),
    )



def index_memes_weaviate(indexMemesWeaviateRequest):
  """
    Index memes in weaviate
  """
  pass






