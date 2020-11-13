from django.http import JsonResponse
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json

@api_view(['GET'])
def username_email_collection(request):
	username_email_collection_json=list(User.objects.values('username','email'))
	return Response(username_email_collection_json)
