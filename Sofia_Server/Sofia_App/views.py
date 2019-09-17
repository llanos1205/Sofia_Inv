from django.shortcuts import render
from django.contrib.auth.models import User, Group
from Sofia_Server.Sofia_App.models import Equipo
from rest_framework import viewsets,status
from Sofia_Server.Sofia_App.serializers import UserSerializer, GroupSerializer,EquipoSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class EquipoViewSet(viewsets.ModelViewSet):
    queryset=Equipo.objects.all().order_by('idequipo')
    serializer_class=EquipoSerializer

@api_view(['GET','POST'])
def Equipo_list(request,format=None):
    if request.method == 'GET':
        snippets = Equipo.objects.all()
        serializer = EquipoSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = EquipoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def Equipo_detail(request, pk,format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        equipo = Equipo.objects.get(pk=pk)
    except Equipo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EquipoSerializer(equipo)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = EquipoSerializer(equipo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        equipo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

