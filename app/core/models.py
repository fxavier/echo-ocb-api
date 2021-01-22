from django.db import models


class Provincia(models.Model):
    nome = models.CharField(max_length=150)

    def __str__(self):
        return self.nome


class Distrito(models.Model):
    nome = models.CharField(max_length=150)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class UnidadeSanitaria(models.Model):
    nome = models.CharField(max_length=150)
    distrito = models.ForeignKey(Distrito, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Unidade Sanitaria'
        verbose_name_plural = 'Unidades Sanitarias'

    def __str__(self):
        return self.nome


class ActaMensalCG(models.Model):
    unidade_sanitaria = models.ForeignKey(
        UnidadeSanitaria, on_delete=models.CASCADE)
    data_encontro = models.DateField(auto_now=False, auto_now_add=False)
    data_proximo_encontro = models.DateField(
        auto_now=False, auto_now_add=False)
    nparticipantes_homens = models.IntegerField()
    participantes_mulheres = models.IntegerField()
    nome_facilitador = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Acta Mensal do CG'
        verbose_name_plural = 'Actas Mensais do CG'

    def __str__(self):
        return self.nome_facilitador


class ResumoMensalVSL(models.Model):
    unidade_sanitaria = models.ForeignKey(
        UnidadeSanitaria, on_delete=models.CASCADE)
    nome_pessoa_facilitador = models.CharField(max_length=150)
    data_inicial = models.DateField(auto_now=False, auto_now_add=False)
    data_final = models.DateField(auto_now=False, auto_now_add=False)
    total_grupos = models.IntegerField()
    num_novos_mes = models.IntegerField()
    num_grupos_encerram_ciclo = models.IntegerField()
    membros_feminino = models.IntegerField()
    membros_masculino = models.IntegerField()
    membros_feminino_HIV_Pos = models.IntegerField()
    membros_masculino_HIV_Pos = models.IntegerField()
    perc_membros_feminino_HIV_Pos = models.DecimalField(
        max_digits=10, decimal_places=2)
    perc_membros_masculino_HIV_Pos = models.DecimalField(
        max_digits=10, decimal_places=2)
    cuid_cov_feminino = models.IntegerField()
    cuid_cov_masculino = models.IntegerField()
    membros_gaac_feminino = models.IntegerField()
    membros_gaac_masculino = models.IntegerField()
    outros_membros_feminino = models.IntegerField()
    outros_membros_masculino = models.IntegerField()
    membros_cs_feminino = models.IntegerField()
    membros_cs_masculino = models.IntegerField()
    membros_maes_feminino = models.IntegerField()
    membros_maes_masculino = models.IntegerField()

    class Meta:
        verbose_name = 'Resumo Mensal de VSL'
        verbose_name_plural = 'Resumos Mensais de VSL'

    def __str__(self):
        return self.nome_pessoa_facilitador


class DialogoComunitario(models.Model):
    unidade_sanitaria = models.ForeignKey(
        UnidadeSanitaria, on_delete=models.CASCADE)
    nome_facilitador = models.CharField(max_length=150)
    data_inicial = models.DateField(auto_now=False, auto_now_add=False)
    data_final = models.DateField(auto_now=False, auto_now_add=False)
    total_grupos = models.IntegerField()
    grupos_novos_mes = models.IntegerField()
    grupos_encerram_ciclo = models.IntegerField()
    participantes_fem_20_24 = models.IntegerField()
    participantes_fem_20_24 = models.IntegerField()
    participantes_fem_25_plus = models.IntegerField()
    participantes_fem_15_19 = models.IntegerField()
    participantes_masc_20_24 = models.IntegerField()
    participantes_masc_25_plus = models.IntegerField()
    participantes_masc_20_24 = models.IntegerField()
    participantes_masc_20_24 = models.IntegerField()
    participantes_masc_25_plus = models.IntegerField()
    participantes_masc_15_19 = models.IntegerField()
    referido = models.IntegerField()
    testagem = models.IntegerField()
    outros_servicos = models.IntegerField()

    class Meta:
        verbose_name = 'Dialogo Comunitario'
        verbose_name_plural = 'Dialogos Comunitarios'

    def __str(self):
        return self.nome_facilitador


class ProgramaRadio(models.Model):
    unidade_sanitaria = models.ForeignKey(
        UnidadeSanitaria, on_delete=models.CASCADE)
    supervisor_cbo = models.CharField(max_length=150)
    nome_radio_comunitaria = models.CharField(max_length=150)
    data_inicio = models.DateField(auto_now=False, auto_now_add=False)
    data_final = models.DateField(auto_now=False, auto_now_add=False)
    ret_geral_spots = models.IntegerField()
    ret_geral_debates = models.IntegerField()
    ret_geral_obs = models.IntegerField()
    ret_gravida_spots = models.IntegerField()
    ret_gravida_debates = models.IntegerField()
    ret_gravida_obs = models.IntegerField()
    tb_hiv_spots = models.IntegerField()
    tb_hiv_debates = models.IntegerField()
    tb_hiv_obs = models.IntegerField()
    tarv_crianca_spots = models.IntegerField()
    tarv_crianca_debates = models.IntegerField()
    tarv_crianca_obs = models.IntegerField()
    gbv_spots = models.IntegerField()
    gbv_debates = models.IntegerField()
    literacia_tarv_spot = models.IntegerField()
    literacia_tarv_database = models.IntegerField()
    literacia_tarv_obs = models.IntegerField()

    class Meta:
        verbose_name = 'Programa da Radio'
        verbose_name_plural = 'Programas da Radio'

    def __str__(self):
        return self.supervisor_cbo


class ActaMensalCS(models.Model):
    unidade_sanitaria = models.ForeignKey(
        UnidadeSanitaria, on_delete=models.CASCADE)
    data_encontro = models.DateField(auto_now=False, auto_now_add=False)
    data_proximo_encontro = models.DateField(
        auto_now=False, auto_now_add=False)
    participantes_homens = models.IntegerField()
    participantes_mulheres = models.IntegerField()
    nome_facilitador = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Acta Mensal do CS'
        verbose_name_plural = 'Actas Mensais do CS'

    def __str__(self):
        return self.nome_facilitador
