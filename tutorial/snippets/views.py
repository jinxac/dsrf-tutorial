# from django.http import HttpResponse, JsonResponse

# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

from rest_framework import generics


class SnippetList(generics.ListCreateAPIView):

  queryset = Snippet.objects.all()
  serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):

  queryset = Snippet.objects.all()
  serializer_class = SnippetSerializer




