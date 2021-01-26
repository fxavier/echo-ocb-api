
import graphene
from graphene_django import DjangoObjectType
from graphql import GraphQLError
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
    actaMensalCS_provincia = graphene.List(
        ActaMensalCSType, provincia_id=graphene.Int())
    all_actaMensalCG = graphene.List(
        ActaMensalCGType, unidade_sanitaria_id=graphene.Int())
    actaMensalCG_provincia = graphene.List(
        ActaMensalCGType, provincia_id=graphene.Int())
    all_resumoMensalVSL = graphene.List(
        ResumoMensalVSLType, unidade_sanitaria_id=graphene.Int())
    resumoMensalVSL_provincia = graphene.List(
        ResumoMensalVSLType, provincia_id=graphene.Int())
    all_dialogoComunitario = graphene.List(
        DialogoComunitarioType, unidade_sanitaria_id=graphene.Int())
    dialogoComunitario_provincia = graphene.List(
        DialogoComunitarioType, provincia_id=graphene.Int())

    all_programaRadio = graphene.List(
        ProgramaRadioType, unidade_sanitaria_id=graphene.Int())
    programaRadio_provincia = graphene.List(
        ProgramaRadioType, provincia_id=graphene.Int())

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

    def resolve_actaMensal(self, info, unidade_sanitaria_id):
        return ActaMensalCS.objects.filter(unidade_sanitaria_id=unidade_sanitaria_id, data_encontro=data_encontro)

    def resolve_actaMensalCS_provincia(self, info, provincia_id):
        return ActaMensalCS.objects.filter(provincia_id=provincia_id)

    def resolve_all_actaMensalCS(self, info, unidade_sanitaria_id=None):
        if unidade_sanitaria_id:
            return ActaMensalCS.objects.filter(unidade_sanitaria_id=unidade_sanitaria_id)
        return ActaMensalCS.objects.all()

    def resolve_all_actaMensalCG(self, info, unidade_sanitaria_id=None):
        if unidade_sanitaria_id:
            return ActaMensalCG.objects.filter(unidade_sanitaria_id=unidade_sanitaria_id)
        return ActaMensalCG.objects.all()

    def resolve_actaMensalCG_provincia(self, info, provincia_id):
        return ActaMensalCG.objects.filter(provincia_id=provincia_id)

    def resolve_all_resumoMensalVSL(self, info, unidade_sanitaria_id=None):
        if unidade_sanitaria_id:
            return ResumoMensalVSL.objects.filter(unidade_sanitaria_id=unidade_sanitaria_id)
        return ResumoMensalVSL.objects.all()

    def resolve_resumoMensalVSL_provincia(self, info, provincia_id):
        return ResumoMensalVSL.objects.filter(provincia_id=provincia_id)

    def resolve_all_dialogoComunitario(self, info, unidade_sanitaria_id=None):
        if unidade_sanitaria_id:
            return DialogoComunitario.objects.filter(unidade_sanitaria_id=unidade_sanitaria_id)
        return DialogoComunitario.objects.all()

    def resolve_dialogoComunitario_provincia(self, info, provincia_id):
        return DialogoComunitario.objects.filter(provincia_id=provincia_id)

    def resolve_all_programaRadio(self, info, unidade_sanitaria_id=None):
        if unidade_sanitaria_id:
            return ProgramaRadio.objects.filter(unidade_sanitaria_id=unidade_sanitaria_id)
        return ProgramaRadio.objects.all()

    def resolve_programaRadio_provincia(self, info, provincia_id):
        return ProgramaRadio.objects.filter(provincia_id=provincia_id)


class AddActaMensalCS(graphene.Mutation):
    actaMensalCS = graphene.Field(ActaMensalCSType)

    class Arguments:
        provincia_id = graphene.Int()
        distrito_id = graphene.Int()
        unidade_sanitaria_id = graphene.Int()
        data_encontro = graphene.Date()
        data_proximo_encontro = graphene.Date()
        participantes_homens = graphene.Int()
        participantes_mulheres = graphene.Int()
        nome_facilitador = graphene.String()

    def mutate(self, info, **kwargs):
        provincia = Provincia.objects.get(id=kwargs.get('provincia_id'))
        distrito = Distrito.objects.get(id=kwargs.get('distrito_id'))
        us = UnidadeSanitaria.objects.get(
            pk=kwargs.get('unidade_sanitaria_id'))
        actaMensalCS = ActaMensalCS.objects.create(
            provincia=provincia,
            distrito=distrito,
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


class UpdateActaMensalCS(graphene.Mutation):
    actaMensalCS = graphene.Field(ActaMensalCSType)

    class Arguments:
        actaMensalCS_id = graphene.Int(required=True)
        Provincia_id = graphene.Int()
        distrito_id = graphene.Int()
        unidade_sanitaria_id = graphene.Int()
        data_encontro = graphene.Date()
        data_proximo_encontro = graphene.Date()
        participantes_homens = graphene.Int()
        participantes_mulheres = graphene.Int()
        nome_facilitador = graphene.String()

    def mutate(self, info, **kwargs):
        actaMensalCS = ActaMensalCS.objects.get(
            pk=kwargs.get('actaMensalCS_id'))
        actaMensalCS.provincia_id = kwargs.get('provincia_id')
        actaMensalCS.distrito_id = kwargs.get('distrito_id')
        actaMensalCS.unidade_sanitaria_id = kwargs.get('unidade_sanitaria_id')
        actaMensalCS.data_encontro = kwargs.get('data_encontro')
        actaMensalCS.data_proximo_encontro = kwargs.get(
            'data_proximo_encontro')
        actaMensalCS.participantes_homens = kwargs.get('participantes_homens')
        actaMensalCS.participantes_mulheres = kwargs.get(
            'participantes_mulheres')
        actaMensalCS.nome_facilitador = kwargs.get('nome_facilitador')

        actaMensalCS.save()
        return UpdateActaMensalCS(actaMensalCS=actaMensalCS)


class DeleteActaMensalCS(graphene.Mutation):
    actaMensalCS_id = graphene.Int()

    class Arguments:
        actaMensalCS_id = graphene.Int(required=True)

    def mutate(self, info, actaMensalCS_id):
        actaMensalCS = ActaMensalCS.objects.get(pk=actaMensalCS_id)
        actaMensalCS.delete()

        return DeleteActaMensalCS(actaMensalCS_id=actaMensalCS_id)


class AddActaMensalCG(graphene.Mutation):
    actaMensalCG = graphene.Field(ActaMensalCGType)

    class Arguments:
        provincia_id = graphene.Int()
        distrito_id = graphene.Int()
        unidade_sanitaria_id = graphene.Int(required=True)
        data_encontro = graphene.Date(required=True)
        data_proximo_encontro = graphene.Date(required=True)
        participantes_homens = graphene.Int(required=True)
        participantes_mulheres = graphene.Int(required=True)
        nome_facilitador = graphene.String(required=True)

    def mutate(self, info, **kwargs):
        provincia = Provincia.objects.get(id=kwargs.get('provincia_id'))
        distrito = Distrito.objects.get(id=kwargs.get('distrito_id'))
        us = UnidadeSanitaria.objects.get(
            id=kwargs.get('unidade_sanitaria_id'))
        actaMensalCG = ActaMensalCG.objects.create(
            provincia=provincia,
            distrito=distrito,
            unidade_sanitaria=us,
            data_encontro=kwargs.get('data_encontro'),
            data_proximo_encontro=kwargs.get('data_proximo_encontro'),
            participantes_homens=kwargs.get('participantes_homens'),
            participantes_mulheres=kwargs.get('participantes_mulheres'),
            nome_facilitador=kwargs.get('nome_facilitador')
        )
        actaMensalCG.save()
        return AddActaMensalCG(actaMensalCG=actaMensalCG)


class UpdateActaMensalCG(graphene.Mutation):
    actaMensalCG = graphene.Field(ActaMensalCGType)

    class Arguments:
        actaMensalCG_id = graphene.Int(required=True)
        provincia_id = graphene.Int()
        distrito_id = graphene.Int()
        unidade_sanitaria_id = graphene.Int(required=True)
        data_encontro = graphene.Date(required=True)
        data_proximo_encontro = graphene.Date(required=True)
        participantes_homens = graphene.Int(required=True)
        participantes_mulheres = graphene.Int(required=True)
        nome_facilitador = graphene.String(required=True)

    def mutate(self, info, **kwargs):
        actaMensalCG = ActaMensalCG.objects.get(
            id=kwargs.get('actaMensalCG_id'))
        actaMensalCG.provincia_id = kwargs.get('provincia_id')
        actaMensalCG.distrito_id = kwargs.get('distrito_id')
        actaMensalCG.unidade_sanitaria_id = kwargs.get('unidade_sanitaria_id')
        actaMensalCG.data_encontro = kwargs.get('data_encontro')
        actaMensalCG.data_proximo_encontro = kwargs.get(
            'data_proximo_encontro')
        actaMensalCG.participantes_homens = kwargs.get('participantes_homens')
        actaMensalCG.participantes_mulheres = kwargs.get(
            'participantes_mulheres')
        actaMensalCG.nome_facilitador = kwargs.get('nome_facilitador')

        actaMensalCG.save()

        return UpdateActaMensalCG(actaMensalCG=actaMensalCG)


class DeleteActaMensalCG(graphene.Mutation):
    actaMensalCG_id = graphene.Int()

    class Arguments:
        actaMensalCG_id = graphene.Int(required=True)

    def mutate(self, info, actaMensalCG_id):
        actaMensalCG = ActaMensalCG.objects.get(id=actaMensalCG_id)
        actaMensalCG.delete()

        return DeleteActaMensalCG(actaMensalCG_id=actaMensalCG_id)


class AddResumoMensalVSL(graphene.Mutation):
    resumoMensalVSL = graphene.Field(ResumoMensalVSLType)

    class Arguments:
        provincia_id = graphene.Int()
        distrito_id = graphene.Int()
        unidade_sanitaria_id = graphene.Int(required=True)
        nome_pessoa_facilitador = graphene.String()
        data_inicial = graphene.Date()
        data_final = graphene.Date()
        total_grupos = graphene.Int()
        num_novos_mes = graphene.Int()
        num_grupos_encerram_ciclo = graphene.Int()
        membros_feminino = graphene.Int()
        membros_masculino = graphene.Int()
        membros_feminino_HIV_Pos = graphene.Int()
        membros_masculino_HIV_Pos = graphene.Int()
        perc_membros_feminino_HIV_Pos = graphene.Int()
        perc_membros_masculino_HIV_Pos = graphene.Int()
        cuid_cov_feminino = graphene.Int()
        cuid_cov_masculino = graphene.Int()
        membros_gaac_feminino = graphene.Int()
        membros_gaac_masculino = graphene.Int()
        outros_membros_feminino = graphene.Int()
        outros_membros_masculino = graphene.Int()
        membros_cs_feminino = graphene.Int()
        membros_cs_masculino = graphene.Int()
        membros_maes_feminino = graphene.Int()
        membros_maes_masculino = graphene.Int()

    def mutate(self, info, **kwargs):
        provincia = Provincia.objects.get(id=kwargs.get('provincia_id'))
        distrito = Distrito.objects.get(id=kwargs.get('distrito_id'))
        us = UnidadeSanitaria.objects.get(
            pk=kwargs.get('unidade_sanitaria_id'))
        resumoMensalVSL = ResumoMensalVSL.objects.create(
            provincia=provincia,
            distrito=distrito,
            unidade_sanitaria=us,
            nome_pessoa_facilitador=kwargs.get('nome_pessoa_facilitador'),
            data_inicial=kwargs.get('data_inicial'),
            data_final=kwargs.get('data_final'),
            total_grupos=kwargs.get('total_grupos'),
            num_novos_mes=kwargs.get('num_novos_mes'),
            num_grupos_encerram_ciclo=kwargs.get('num_grupos_encerram_ciclo'),
            membros_feminino=kwargs.get('membros_feminino'),
            membros_masculino=kwargs.get('membros_masculino'),
            membros_feminino_HIV_Pos=kwargs.get('membros_feminino_HIV_Pos'),
            membros_masculino_HIV_Pos=kwargs.get('membros_masculino_HIV_Pos'),
            perc_membros_feminino_HIV_Pos=kwargs.get(
                'perc_membros_feminino_HIV_Pos'),
            perc_membros_masculino_HIV_Pos=kwargs.get(
                'perc_membros_masculino_HIV_Pos'),
            cuid_cov_feminino=kwargs.get('cuid_cov_feminino'),
            cuid_cov_masculino=kwargs.get('cuid_cov_masculino'),
            membros_gaac_feminino=kwargs.get('membros_gaac_feminino'),
            membros_gaac_masculino=kwargs.get('membros_gaac_masculino'),
            outros_membros_feminino=kwargs.get('outros_membros_feminino'),
            outros_membros_masculino=kwargs.get('outros_membros_masculino'),
            membros_cs_feminino=kwargs.get('membros_cs_feminino'),
            membros_cs_masculino=kwargs.get('membros_cs_masculino'),
            membros_maes_feminino=kwargs.get('membros_maes_feminino'),
            membros_maes_masculino=kwargs.get('membros_maes_masculino')
        )
        resumoMensalVSL.save()
        return AddResumoMensalVSL(resumoMensalVSL=resumoMensalVSL)


class UpdateResumoMensalVSL(graphene.Mutation):
    resumoMensalVSL = graphene.Field(ResumoMensalVSLType)

    class Arguments:
        resumoMensalVSL_id = graphene.Int(required=True)
        provincia_id = graphene.Int()
        distrito_id = graphene.Int()
        unidade_sanitaria_id = graphene.Int(required=True)
        nome_pessoa_facilitador = graphene.String()
        data_inicial = graphene.Date()
        data_final = graphene.Date()
        total_grupos = graphene.Int()
        num_novos_mes = graphene.Int()
        num_grupos_encerram_ciclo = graphene.Int()
        membros_feminino = graphene.Int()
        membros_masculino = graphene.Int()
        membros_feminino_HIV_Pos = graphene.Int()
        membros_masculino_HIV_Pos = graphene.Int()
        perc_membros_feminino_HIV_Pos = graphene.Int()
        perc_membros_masculino_HIV_Pos = graphene.Int()
        cuid_cov_feminino = graphene.Int()
        cuid_cov_masculino = graphene.Int()
        membros_gaac_feminino = graphene.Int()
        membros_gaac_masculino = graphene.Int()
        outros_membros_feminino = graphene.Int()
        outros_membros_masculino = graphene.Int()
        membros_cs_feminino = graphene.Int()
        membros_cs_masculino = graphene.Int()
        membros_maes_feminino = graphene.Int()
        membros_maes_masculino = graphene.Int()

    def mutate(self, info, **kwargs):
        resumoMensalVSL = ResumoMensalVSL.objects.get(
            id=kwargs.get('resumoMensalVSL_id'))
        resumoMensalVSL.provincia_id = kwargs.get('provincia_id')
        resumoMensalVSL.distrito_id = kwargs.get('distrito_id')
        resumoMensalVSL.unidade_sanitaria_id = kwargs.get(
            'unidade_sanitaria_id')
        resumoMensalVSL.nome_pessoa_facilitador = kwargs.get(
            'nome_pessoa_facilitador')
        resumoMensalVSL.data_inicial = kwargs.get('data_inicial')
        resumoMensalVSL.data_final = kwargs.get('data_final')
        resumoMensalVSL.total_grupos = kwargs.get('total_grupos')
        resumoMensalVSL.num_novos_mes = kwargs.get('num_novos_mes')
        resumoMensalVSL.num_grupos_encerram_ciclo = kwargs.get(
            'num_grupos_encerram_ciclo')
        resumoMensalVSL.membros_feminino = kwargs.get('membros_feminino')
        resumoMensalVSL.membros_masculino = kwargs.get(
            'membros_masculino')
        resumoMensalVSL.membros_feminino_HIV_Pos = kwargs.get(
            'membros_feminino_HIV_Pos')
        resumoMensalVSL.membros_masculino_HIV_Pos = kwargs.get(
            'membros_masculino_HIV_Pos')
        resumoMensalVSL.perc_membros_feminino_HIV_Pos = kwargs.get(
            'perc_membros_feminino_HIV_Pos')
        resumoMensalVSL.perc_membros_masculino_HIV_Pos = kwargs.get(
            'perc_membros_masculino_HIV_Pos')
        resumoMensalVSL.cuid_cov_feminino = kwargs.get(
            'cuid_cov_feminino')
        resumoMensalVSL.cuid_cov_masculino = kwargs.get(
            'cuid_cov_masculino')
        resumoMensalVSL.membros_gaac_feminino = kwargs.get(
            'membros_gaac_feminino')
        resumoMensalVSL.membros_gaac_masculino = kwargs.get(
            'membros_gaac_masculino')
        resumoMensalVSL.outros_membros_feminino = kwargs.get(
            'outros_membros_feminino')
        resumoMensalVSL.outros_membros_masculino = kwargs.get(
            'outros_membros_masculino')
        resumoMensalVSL.membros_cs_feminino = kwargs.get(
            'membros_cs_feminino')
        resumoMensalVSL.membros_cs_masculino = kwargs.get(
            'membros_cs_masculino')
        resumoMensalVSL.membros_maes_feminino = kwargs.get(
            'membros_maes_feminino')
        resumoMensalVSL.membros_maes_masculino = kwargs.get(
            'membros_maes_masculino')

        resumoMensalVSL.save()
        return UpdateResumoMensalVSL(resumoMensalVSL=resumoMensalVSL)


class DeleteResumoMensalVSL(graphene.Mutation):
    resumoMensalVSL_id = graphene.Int()

    class Arguments:
        resumoMensalVSL_id = graphene.Int(required=True)

    def mutate(self, info, resumoMensalVSL_id):
        resumoMensalVSL = ResumoMensalVSL.objects.get(id=resumoMensalVSL_id)
        resumoMensalVSL.delete()

        return DeleteResumoMensalVSL(resumoMensalVSL_id=resumoMensalVSL_id)


class AddDialogoComunitario(graphene.Mutation):
    dialogoComunitario = graphene.Field(DialogoComunitarioType)

    class Arguments:
        provincia_id = graphene.Int()
        distrito_id = graphene.Int()
        unidade_sanitaria_id = graphene.Int()
        nome_facilitador = graphene.String()
        data_inicial = graphene.Date()
        data_final = graphene.Date()
        total_grupos = graphene.Int()
        grupos_novos_mes = graphene.Int()
        grupos_encerram_ciclo = graphene.Int()
        participantes_fem_20_24 = graphene.Int()
        participantes_fem_25_plus = graphene.Int()
        participantes_fem_15_19 = graphene.Int()
        participantes_masc_20_24 = graphene.Int()
        participantes_masc_25_plus = graphene.Int()
        participantes_masc_15_19 = graphene.Int()
        referido = graphene.Int()
        testagem = graphene.Int()
        outros_servicos = graphene.Int()

    def mutate(self, info, **kwargs):
        provincia = Provincia.objects.get(id=kwargs.get('provincia_id'))
        distrito = Distrito.objects.get(id=kwargs.get('distrito_id'))
        unidade_sanitaria = UnidadeSanitaria.objects.get(
            id=kwargs.get('unidade_sanitaria_id'))
        dialogoComunitario = DialogoComunitario.objects.create(
            provincia=provincia,
            distrito=distrito,
            unidade_sanitaria=unidade_sanitaria,
            nome_facilitador=kwargs.get('nome_facilitador'),
            data_inicial=kwargs.get('data_inicial'),
            data_final=kwargs.get('data_final'),
            total_grupos=kwargs.get('total_grupos'),
            grupos_novos_mes=kwargs.get('grupos_novos_mes'),
            grupos_encerram_ciclo=kwargs.get('grupos_encerram_ciclo'),
            participantes_fem_20_24=kwargs.get('participantes_fem_20_24'),
            participantes_fem_25_plus=kwargs.get('participantes_fem_25_plus'),
            participantes_fem_15_19=kwargs.get('participantes_fem_15_19'),
            participantes_masc_20_24=kwargs.get('participantes_masc_20_24'),
            participantes_masc_25_plus=kwargs.get(
                'participantes_masc_25_plus'),
            participantes_masc_15_19=kwargs.get('participantes_masc_15_19'),
            referido=kwargs.get('referido'),
            testagem=kwargs.get('testagem'),
            outros_servicos=kwargs.get('outros_servicos')
        )
        dialogoComunitario.save()
        return AddDialogoComunitario(dialogoComunitario=dialogoComunitario)


class UpdateDialogoComunitario(graphene.Mutation):
    dialogoComunitario = graphene.Field(DialogoComunitarioType)

    class Arguments:
        dialogo_comunitario_id = graphene.Int(required=True)
        provincia_id = graphene.Int()
        distrito_id = graphene.Int()
        unidade_sanitaria_id = graphene.Int()
        nome_facilitador = graphene.String()
        data_inicial = graphene.Date()
        data_final = graphene.Date()
        total_grupos = graphene.Int()
        grupos_novos_mes = graphene.Int()
        grupos_encerram_ciclo = graphene.Int()
        participantes_fem_20_24 = graphene.Int()
        participantes_fem_25_plus = graphene.Int()
        participantes_fem_15_19 = graphene.Int()
        participantes_masc_20_24 = graphene.Int()
        participantes_masc_25_plus = graphene.Int()
        participantes_masc_15_19 = graphene.Int()
        referido = graphene.Int()
        testagem = graphene.Int()
        outros_servicos = graphene.Int()

    def mutate(self, info, **kwargs):
        dialogoComunitario = DialogoComunitario.objects.get(
            id=kwargs.get('dialogo_comunitario_id'))
        dialogoComunitario.provincia_id = kwargs.get('provincia_id')
        dialogoComunitario.distrito_id = kwargs.get('distrito_id')
        dialogoComunitario.unidade_sanitaria_id = kwargs.get(
            'unidade_sanitaria_id')
        dialogoComunitario.nome_facilitador = kwargs.get('nome_facilitador')
        dialogoComunitario.data_inicial = kwargs.get('data_inicial')
        dialogoComunitario.data_final = kwargs.get('data_final')
        dialogoComunitario.total_grupos = kwargs.get('total_grupos')
        dialogoComunitario.grupos_novos_mes = kwargs.get('grupos_novos_mes')
        dialogoComunitario.grupos_encerram_ciclo = kwargs.get(
            'grupos_encerram_ciclo')
        dialogoComunitario.participantes_fem_20_24 = kwargs.get(
            'participantes_fem_20_24')
        dialogoComunitario.participantes_fem_25_plus = kwargs.get(
            'participantes_fem_25_plus')
        dialogoComunitario.participantes_fem_15_19 = kwargs.get(
            'participantes_fem_15_19')
        dialogoComunitario.participantes_masc_20_24 = kwargs.get(
            'participantes_masc_20_24')
        dialogoComunitario.participantes_masc_25_plus = kwargs.get(
            'participantes_masc_25_plus')
        dialogoComunitario.participantes_masc_15_19 = kwargs.get(
            'participantes_masc_15_19')
        dialogoComunitario.referido = kwargs.get('referido')
        dialogoComunitario.testagem = kwargs.get('testagem')
        dialogoComunitario.outros_servicos = kwargs.get('outros_servicos')

        dialogoComunitario.save()
        return UpdateDialogoComunitario(dialogoComunitario=dialogoComunitario)


class DeleteDialogoComunitario(graphene.Mutation):
    dialogo_comunitario_id = graphene.Int()

    class Arguments:
        dialogo_comunitario_id = graphene.Int(required=True)

    def mutate(self, info, dialogo_comunitario_id):
        dialogoComunitario = DialogoComunitario.objects.get(
            id=dialogo_comunitario_id)
        dialogoComunitario.delete()
        return DeleteDialogoComunitario(dialogo_comunitario_id=dialogo_comunitario_id)


class AddProgramaRadio(graphene.Mutation):
    programaRadio = graphene.Field(ProgramaRadioType)

    class Arguments:
        provincia_id = graphene.Int()
        distrito_id = graphene.Int()
        unidade_sanitaria_id = graphene.Int()
        supervisor_cbo = graphene.String()
        nome_radio_comunitaria = graphene.String()
        data_inicio = graphene.Date()
        data_final = graphene.Date()
        ret_geral_spots = graphene.Int()
        ret_geral_debates = graphene.Int()
        ret_geral_obs = graphene.Int()
        ret_gravida_spots = graphene.Int()
        ret_gravida_debates = graphene.Int()
        ret_gravida_obs = graphene.Int()
        tb_hiv_spots = graphene.Int()
        tb_hiv_debates = graphene.Int()
        tb_hiv_obs = graphene.Int()
        tarv_crianca_spots = graphene.Int()
        tarv_crianca_debates = graphene.Int()
        tarv_crianca_obs = graphene.Int()
        gbv_spots = graphene.Int()
        gbv_debates = graphene.Int()
        literacia_tarv_spot = graphene.Int()
        literacia_tarv_database = graphene.Int()
        literacia_tarv_obs = graphene.Int()

    def mutate(self, info, **kwargs):
        provincia = Provincia.objects.get(pk=kwargs.get('provincia_id'))
        distrito = Distrito.objects.get(pk=kwargs.get('distrito_id'))
        us = UnidadeSanitaria.objects.get(
            pk=kwargs.get('unidade_sanitaria_id'))
        programaRadio = ProgramaRadio.objects.create(
            provincia=provincia,
            distrito=distrito,
            unidade_sanitaria=us,
            supervisor_cbo=kwargs.get('supervisor_cbo'),
            nome_radio_comunitaria=kwargs.get('nome_radio_comunitaria'),
            data_inicio=kwargs.get('data_inicio'),
            data_final=kwargs.get('data_final'),
            ret_geral_spots=kwargs.get('ret_geral_spots'),
            ret_geral_debates=kwargs.get('ret_geral_debates'),
            ret_geral_obs=kwargs.get('ret_geral_obs'),
            ret_gravida_spots=kwargs.get('ret_gravida_spots'),
            ret_gravida_debates=kwargs.get('ret_gravida_debates'),
            ret_gravida_obs=kwargs.get('ret_gravida_obs'),
            tb_hiv_spots=kwargs.get('tb_hiv_spots'),
            tb_hiv_debates=kwargs.get('tb_hiv_debates'),
            tb_hiv_obs=kwargs.get('tb_hiv_obs'),
            tarv_crianca_spots=kwargs.get('tarv_crianca_spots'),
            tarv_crianca_debates=kwargs.get('tarv_crianca_debates'),
            tarv_crianca_obs=kwargs.get('tarv_crianca_obs'),
            gbv_spots=kwargs.get('gbv_spots'),
            gbv_debates=kwargs.get('gbv_debates'),
            literacia_tarv_spot=kwargs.get('literacia_tarv_spot'),
            literacia_tarv_database=kwargs.get('literacia_tarv_database'),
            literacia_tarv_obs=kwargs.get('literacia_tarv_obs')
        )
        programaRadio.save()
        return AddProgramaRadio(programaRadio=programaRadio)


class UpdateProgramaRadio(graphene.Mutation):
    programaRadio = graphene.Field(ProgramaRadioType)

    class Arguments:
        programa_radio_id = graphene.Int(required=True)
        provincia_id = graphene.Int()
        distrito_id = graphene.Int()
        unidade_sanitaria_id = graphene.Int()
        supervisor_cbo = graphene.String()
        nome_radio_comunitaria = graphene.String()
        data_inicio = graphene.Date()
        data_final = graphene.Date()
        ret_geral_spots = graphene.Int()
        ret_geral_debates = graphene.Int()
        ret_geral_obs = graphene.Int()
        ret_gravida_spots = graphene.Int()
        ret_gravida_debates = graphene.Int()
        ret_gravida_obs = graphene.Int()
        tb_hiv_spots = graphene.Int()
        tb_hiv_debates = graphene.Int()
        tb_hiv_obs = graphene.Int()
        tarv_crianca_spots = graphene.Int()
        tarv_crianca_debates = graphene.Int()
        tarv_crianca_obs = graphene.Int()
        gbv_spots = graphene.Int()
        gbv_debates = graphene.Int()
        literacia_tarv_spot = graphene.Int()
        literacia_tarv_database = graphene.Int()
        literacia_tarv_obs = graphene.Int()

    def mutate(self, info, **kwargs):
        programaRadio = ProgramaRadio.objects.get(
            id=kwargs.get('programa_radio_id'))
        programaRadio.provincia_id = kwargs.get('provincia_id')
        programaRadio.distrito_id = kwargs.get('distrito_id')
        programaRadio.unidade_sanitaria_id = kwargs.get('unidade_sanitaria_id')
        programaRadio.supervisor_cbo = kwargs.get('supervisor_cbo')
        programaRadio.nome_radio_comunitaria = kwargs.get(
            'nome_radio_comunitaria')
        programaRadio.data_inicio = kwargs.get('data_inicio')
        programaRadio.data_final = kwargs.get('data_final')
        programaRadio.ret_geral_spots = kwargs.get('ret_geral_spots')
        programaRadio.ret_geral_debates = kwargs.get('ret_geral_debates')
        programaRadio.ret_geral_obs = kwargs.get('ret_geral_obs')
        programaRadio.ret_gravida_spots = kwargs.get('ret_gravida_spots')
        programaRadio.ret_gravida_debates = kwargs.get('ret_gravida_debates')
        programaRadio.ret_gravida_obs = kwargs.get('ret_gravida_obs')
        programaRadio.tb_hiv_spots = kwargs.get('tb_hiv_spots')
        programaRadio.tb_hiv_debates = kwargs.get('tb_hiv_debates')
        programaRadio.tb_hiv_obs = kwargs.get('tb_hiv_obs')
        programaRadio.tarv_crianca_spots = kwargs.get('tarv_crianca_spots')
        programaRadio.tarv_crianca_debates = kwargs.get('tarv_crianca_debates')
        programaRadio.tarv_crianca_obs = kwargs.get('tarv_crianca_obs')
        programaRadio.gbv_spots = kwargs.get('gbv_spots')
        programaRadio.gbv_debates = kwargs.get('gbv_debates')
        programaRadio.literacia_tarv_spot = kwargs.get('literacia_tarv_spot')
        programaRadio.literacia_tarv_database = kwargs.get(
            'literacia_tarv_database')
        programaRadio.literacia_tarv_obs = kwargs.get('literacia_tarv_obs')

        programaRadio.save()
        return UpdateProgramaRadio(programaRadio=programaRadio)


class DeleteProgramaRadio(graphene.Mutation):
    programa_radio_id = graphene.Int()

    class Arguments:
        programa_radio_id = graphene.Int(required=True)

    def mutate(self, info, programa_radio_id):
        programaRadio = ProgramaRadio.objects.get(pk=programa_radio_id)

        programaRadio.delete()

        return DeleteProgramaRadio(programa_radio_id=programa_radio_id)


class Mutation:
    add_actaMensalCS = AddActaMensalCS.Field()
    update_actaMensalCS = UpdateActaMensalCS.Field()
    delete_actaMensalCS = DeleteActaMensalCS.Field()
    add_actaMensalCG = AddActaMensalCG.Field()
    update_actaMensalCG = UpdateActaMensalCG.Field()
    delete_actaMensalCG = DeleteActaMensalCG.Field()
    add_resumoMensalVSL = AddResumoMensalVSL.Field()
    update_resumoMensalVSL = UpdateResumoMensalVSL.Field()
    delete_resumoMensalVSL = DeleteResumoMensalVSL.Field()
    add_dialogoComunitario = AddDialogoComunitario.Field()
    update_dialogoComunitario = UpdateDialogoComunitario.Field()
    delete_dialogoComunitario = DeleteDialogoComunitario.Field()
    add_programaRadio = AddProgramaRadio.Field()
    update_programaRadio = UpdateProgramaRadio.Field()
    delete_programaRadio = DeleteProgramaRadio.Field()
