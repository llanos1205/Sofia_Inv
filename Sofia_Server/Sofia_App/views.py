# from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets,status,generics
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import date
from Sofia_Server.Sofia_App.Modulos.Transacciones import serializers
class EquiposRelease(APIView):
    def get(self, request,pk,side):
        if side==1:
            obj=serializers.Asociacion.objects.filter(usuariofinal=pk,fecha_baja=None)
        else:
            obj=serializers.Asociacion.objects.filter(equipo_idequipo=pk,fecha_baja=None)
        for model in obj:
            model.fecha_baja=date.today().strftime('%Y-%m-%d')
            model.motivo="Baja"
            model.save()
        content={'message': 'Success!'}
        return Response(content)