from django.contrib import admin

from .models import (Persona, Sexo, EstadoCivil)


@admin.register(Sexo)
class SexoAdmin(admin.ModelAdmin):
    pass


@admin.register(EstadoCivil)
class EstadoCivilAdmin(admin.ModelAdmin):
    pass


@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    fields = ['nombre', 'apellidoPaterno', 'apellidoMaterno', 'fechaNacimiento', 'sexo', 'estadoCivil' ]

    list_display = ('nombre', 'apellidoPaterno', 'apellidoMaterno', 'fechaNacimiento', 'edad' )