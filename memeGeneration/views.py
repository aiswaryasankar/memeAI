from django.shortcuts import render

# Create your views here.
from .serializer import *
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from .handler import *
from memeModel import idl 

"""
  This file will handle the actual external facing API for the MemeGeneration service.
  This includes mapping all the httpRequest / httpResponse objects to internal
  dataclass objects and performing the necessary validation steps that are specified
  in the serializers class. If there are any issues in this mapping / validation it will
  return an error immediately.  This file is necessary since service to service will make
  calls to the handler based on the dataclass request/ response whereas the front end will
  make requests through http which needs to be serialized from the JSON struct that's passed in.
"""


@api_view(['POST'])
def generate_text_for_meme_view(request):
  """
    Generate text for meme
  """
  req = GenerateTextForMemeRequestSerializer(data=request.data)
  if not req.is_valid():
    return Response(req.errors)

  generateTextForMemeRequest = req.validated_data
  res = generate_text_for_meme(generateTextForMemeRequest)

  return Response(res.to_json())



@api_view(['POST'])
def generate_meme_image_view(request):
  """
    Create meme image
  """
  req = GenerateMemeImageRequestSerializer(data=request.data)
  if not req.is_valid():
    return Response(req.errors)

  createMemeImageRequest = req.validated_data
  res = generate_meme_image(createMemeImageRequest)

  return Response(res.to_json())



