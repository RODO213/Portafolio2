from django.contrib import admin
from .models import Arriendo, Cliente, Contacto

# Register your models here.

class ArriendoAdmin(admin.ModelAdmin):
    list_display = ["fecha_inicio", "fecha_termino", "descripcion_arriendo"] # para ver lista
    list_editable =["descripcion_arriendo"] # para editar
    search_fields = ["id_arriendo"] # para buscar
    list_filter = ["descripcion_tipo_pago"] # filtro de busqueda

admin.site.register(Arriendo, ArriendoAdmin)
admin.site.register(Cliente)
admin.site.register(Contacto)

