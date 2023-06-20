from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def testPoint(request):
    content = {'message': 'Hello, GeeksforGeeks', 'method': request.method}
    return Response(content)
