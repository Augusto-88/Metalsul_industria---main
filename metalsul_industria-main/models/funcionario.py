from database.conexao import Conexao
from datetime import date


# CLASSE FUNCIONARIO

class Funcionario:
    def __init__(
        self,
        id_funcionario=None,
        nome="",
        rg="",
        cpf="",
        data_nascimento=None,
        sexo="",
        estado_civil="",
        cargo="",
        telefone="",
        celular="",
        email="",
        departamento="",
        salario=0.0,
        data_admissao="",
        data_demissao="",
        turno="",
        status="ATIVO",
        observacoes=""
    ):
        self.id_funcionario = id_funcionario
        self.nome = nome
        self.rg = rg
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.sexo = sexo
        self.estado_civil = estado_civil
        self.cargo = cargo
        self.telefone = telefone
        self.celular = celular
        self.email = email
        self.departamento = departamento
        self.salario = salario
        self.data_admissao = data_admissao
        self.data_demissao = data_demissao
        self.turno = turno
        self.status = status
        self.observacoes = observacoes

    def __str__(self):
        return (
            f"\nFUNCIONÁRIO: {self.nome}"
            f"\nCPF: {self.cpf}"
            f"\nCARGO: {self.cargo}"
            f"\nDEPARTAMENTO: {self.departamento}"
            f"\nSALÁRIO: {self.salario}"
            f"\nSTATUS: {self.status}"
        )