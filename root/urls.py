"""memeModel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from memeGeneration import views as memeGenerationView
from memeMatching import views as memeMatchingView
from appBackend import views as appBackendView

urlpatterns = [
    path('admin/', admin.site.urls),

    # MemeMatching endpoints
    path('matchTextToMeme/', memeMatchingView.match_text_to_meme_view),
    path('indexMemes/', memeMatchingView.index_memes_weaviate_view),
    path('generateMultipleMemeImages/', memeMatchingView.generate_multiple_meme_image_view),

    # MemeGeneration endpoints
    path('generateTextForMeme/', memeGenerationView.generate_text_for_meme_view),
    path('generateMeme/', memeGenerationView.generate_meme_image_view),

    # AppBackend endpoints
    path('memeGeneration/', appBackendView.meme_generation_view),
]
