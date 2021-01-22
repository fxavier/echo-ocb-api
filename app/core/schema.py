
import graphene
from graphene_django import DjangoObjectType
from core.models import Provincia, Distrito, UnidadeSanitaria, ActaMensalCG, ActaMensalCS,\
    ResumoMensalVSL, DialogoComunitario, ProgramaRadio
from django.db.models import Q


class ProvinciaType(DjangoObjectType):
    class Meta:
        model = Provincia


class DistritoType(DjangoObjectType):
    class Meta:
        model = Distrito


class UnidadeSanitariaType(DjangoObjectType):
    class Meta:
        model = UnidadeSanitaria


class ActaMensalCGType(DjangoObjectType):
    class Meta:
        model = ActaMensalCG


class ActaMensalCSType(DjangoObjectType):
    class Meta:
        model = ActaMensalCS


class ResumoMensalVSLType(DjangoObjectType):
    class Meta:
        model = ResumoMensalVSL


class DialogoComunitarioType(DjangoObjectType):
    class Meta:
        model = DialogoComunitario


class ProgramaRadioType(DjangoObjectType):
    class Meta:
        model = ProgramaRadio


class Query(graphene.ObjectType):
    provincias = graphene.List(ProvinciaType)
    provincia = graphene.Field(ProvinciaType, id=graphene.Int(required=True))
    distritos = graphene.List(DistritoType, provincia_id=graphene.Int())
    distrito = graphene.Field(DistritoType, id=graphene.Int(required=True))
    uss = graphene.List(UnidadeSanitariaType, distrito_id=graphene.Int())
    us = graphene.Field(UnidadeSanitariaType, id=graphene.Int(required=True))
    all_actaMensalCS = graphene.List(
        ActaMensalCSType, unidade_sanitaria_id=graphene.Int())

    def resolve_provincias(self, info):
        return Provincia.objects.all()

    def resolve_provincia(self, info, id):
        return Provincia.objects.get(pk=id)

    def resolve_distritos(self, info, provincia_id=None):
        if provincia_id:
            return Distrito.objects.filter(provincia_id=provincia_id)
        return Distrito.objects.all()

    def resolve_uss(self, info, distrito_id=None):
        if distrito_id:
            return UnidadeSanitaria.objects.filter(distrito_id=distrito_id)
        return UnidadeSanitaria.objects.all()

    def resolve_all_actaMensalCS(self, info, unidade_sanitaria_id=None):
        if unidade_sanitaria_id:
            return ActaMensalCS.objects.filter(unidade_sanitaria_id=unidade_sanitaria_id)
        return ActaMensalCS.objects.all()


class AddActaMensalCS(graphene.Mutation):
    actaMensalCS = graphene.Field(ActaMensalCSType)

    class Arguments:
        unidade_sanitaria_id = graphene.Int()
        data_encontro = graphene.Date()
        data_proximo_encontro = graphene.Date()
        participantes_homens = graphene.Int()
        participantes_mulheres = graphene.Int()
        nome_facilitador = graphene.String()

    def mutate(self, info, **kwargs):
        us = UnidadeSanitaria.objects.get(
            pk=kwargs.get('unidade_sanitaria_id'))
        actaMensalCS = ActaMensalCS.objects.create(
            unidade_sanitaria=us,
            data_encontro=kwargs.get('data_encontro'),
            data_proximo_encontro=kwargs.get('data_proximo_encontro'),
            participantes_homens=kwargs.get('participantes_homens'),
            participantes_mulheres=kwargs.get('participantes_mulheres'),
            nome_facilitador=kwargs.get('nome_facilitador')
        )
        actaMensalCS.save()
        # Notice we return an instance of this mutation
        return AddActaMensalCS(actaMensalCS=actaMensalCS)


class Mutation:
    add_actaMensalCS = AddActaMensalCS.Field()
