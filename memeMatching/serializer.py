from rest_framework import serializers
from memeModel import idl
from rest_framework_dataclasses.serializers import DataclassSerializer
from rest_framework.parsers import JSONParser

"""
  This file will define all the Serializers for the meme generation service.  Serializers serve to map and handle validation between httpRequest objects passed into the service and the dataclasses used to store and pass data around internally between the various apps.
"""


class IndexMemesWeaviateRequestSerializer(DataclassSerializer):
  parser_classes = JSONParser
  class Meta:
    dataclass = IndexMemesWeaviateRequest


class MatchTextToMemeRequestSerializer(DataclassSerializer):
  parser_classes = JSONParser
  class Meta:
    dataclass = MatchTextToMemeRequest


