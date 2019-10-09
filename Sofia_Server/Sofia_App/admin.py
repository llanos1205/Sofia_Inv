from django.contrib import admin
from Sofia_Server.Sofia_App.Modulos.Equipos.models import (OrdenadorHasLicencia,Atributo,Tablet,
Equipo,Ordenador,Impresora,OtroDispositivo,OtroDispositivoHasAtributo,Licencia,Os)
from Sofia_Server.Sofia_App.Modulos.InfoUser.models import Empresa,Cargo,Area,Gerencia,Ubicacion,Departamento,Permiso,Regional
from Sofia_Server.Sofia_App.Modulos.Transacciones.models import Auditoria,Asociacion
from Sofia_Server.Sofia_App.Modulos.Usuarios.models import UsuarioAdHasPermiso,UsuarioAd,Cuenta,UsuarioCorreo,Permiso
# Register your models here.

admin.site.register(Atributo)
admin.site.register(Tablet)
admin.site.register(Equipo)
admin.site.register(Ordenador)
admin.site.register(Impresora)
admin.site.register(OtroDispositivo)
admin.site.register(OtroDispositivoHasAtributo)
admin.site.register(Licencia)
admin.site.register(Os)
admin.site.register(Empresa)
admin.site.register(Cargo)
admin.site.register(Area)
admin.site.register(Gerencia)
admin.site.register(Ubicacion)
admin.site.register(Departamento)
admin.site.register(Permiso)
admin.site.register(Regional)
admin.site.register(Auditoria)
admin.site.register(Asociacion)
admin.site.register(UsuarioAd)
admin.site.register(UsuarioAdHasPermiso)
admin.site.register(Cuenta)
admin.site.register(UsuarioCorreo)
admin.site.register(OrdenadorHasLicencia)