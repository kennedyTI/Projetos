from django.db.models import CharField, Model, ForeignKey, IntegerField, SET_NULL


class Ramo(Model):

    caixaDeSeleção = (
        ('constr', 'Construção'),
        ('auto', 'Automobilistica'),
        ('Fer', 'Ferrovia'),
    )

    título = CharField(
        max_length=6,
        choices=caixaDeSeleção
    )

    def __str__(self):
        return self.título


class Cliente(Model):

    categoria = ForeignKey(
        Ramo,
        on_delete=SET_NULL,
        null=True,
        choices=Ramo.caixaDeSeleção
    )
    razãoSocial = CharField(max_length=30)
    nomeFantasia = CharField(max_length=30)
    cnpj = CharField(max_length=14)
    ramo = CharField(max_length=20)
    representante = CharField(max_length=30)
    fone01 = CharField(max_length=11)
    fone02 = CharField(max_length=11)
    email = CharField(max_length=30)
    número = IntegerField()
    rua = CharField(max_length=40)
    cidade = CharField(max_length=40)
    estado = CharField(max_length=40)
    cep = CharField(max_length=8)

    def __str__(self) -> CharField:
        return self.razãoSocial
