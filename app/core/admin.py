from django.contrib import admin
from core import models
from django.utils.translation import gettext as _


class ActaMensalCGAdmin(admin.ModelAdmin):
    ordering = ['id']


admin.site.register(models.Provincia)
admin.site.register(models.Distrito)
admin.site.register(models.UnidadeSanitaria)
admin.site.register(models.ResumoMensalVSL)
admin.site.register(models.ProgramaRadio)
admin.site.register(models.ActaMensalCG, ActaMensalCGAdmin)
admin.site.register(models.ActaMensalCS)
admin.site.register(models.DialogoComunitario)
