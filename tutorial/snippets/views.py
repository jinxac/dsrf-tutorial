# from django.http import HttpResponse, JsonResponse

# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import mixins
from rest_framework import generics


class SnippetList(
  generics.GenericAPIView,
  mixins.ListModelMixin,
  mixins.CreateModelMixin):

  queryset = Snippet.objects.all()
  serializer_class = SnippetSerializer

  def get(self, *args, **kwargs):
    return self.list(self, *args, **kwargs)

  def post(self, *args, **kwargs):
    return self.create(self, *args, **kwargs)


class SnippetDetail(
  generics.GenericAPIView,
  mixins.RetrieveModelMixin,
  mixins.UpdateModelMixin,
  mixins.DestroyModelMixin):

  queryset = Snippet.objects.all()
  serializer_class = SnippetSerializer

  def get(self, request, *args, **kwargs):
    return self.retrieve(request, *args, **kwargs)

  def put(self, request, *args, **kwargs):
    return self.update(request, *args, **kwargs)

  def delete(self, request, *args, **kwargs):
    return self.destroy(request, *args, **kwargs)




