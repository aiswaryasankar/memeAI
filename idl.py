from dataclasses import *
import dataclasses
import json

# from marshmallow import EXCLUDE, fields, pre_dump, Schema, validate
import requests
from enum import Enum
from typing import List, Optional
import time
from dataclasses_json import dataclass_json
import typing


"""
  This file defines the IDL through which the front end and backend send requests
  and responses to each other.
"""

###
#
# MemeGeneration
#
###

@dataclass
class GenerateTextForMemeRequest:
     MemeImage: str
     InputText: str

@dataclass_json
@dataclass
class GenerateTextForMemeResponse:
     OutputText: str
     Error: Exception

@dataclass
class GenerateMemeImageRequest:
     MemeImage: str
     MemeText: str

@dataclass_json
@dataclass
class GenerateMemeImageResponse:
     ProcessedMeme: str
     Error: Exception



###
#
# MemeMatching
#
###

@dataclass
class IndexMemesWeaviateRequest:
	MemeImageLink: List[str]
	Description: List[str]

@dataclass_json
@dataclass
class IndexMemesWeaviateResponse:
	Error: Exception

@dataclass
class MatchTextToMemeRequest:
	InputText: str

@dataclass_json
@dataclass
class MatchTextToMemeResponse:
	Memes: List[str]
	Error: Exception

@dataclass
class GenerateMultipleMemeImagesRequest:
	NumVersions: int

@dataclass_json
@dataclass
class GenerateMultipleMemeImagesResponse:
	Memes: List[str]
	Error: Exception


###
#
# AppBackend
#
###

@dataclass
class MemeGenerationRequest:
     InputText: str

@dataclass_json
@dataclass
class MemeGenerationResponse:
     Memes: List[str]
     Error: Exception



