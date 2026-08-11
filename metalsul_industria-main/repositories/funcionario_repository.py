from database.conexao import Conexao
from models.funcionario import Funcionario


class FuncionarioRepository:
    def __init__(self):
        self.db = Conexao()

    def criar_funcionario(self, registro):
        return Funcionario(
        id_funcionario=registro[0],
        nome=registro[1],
        cpf=registro[2],
        rg=registro[3],
        data_nascimento=registro[4],
        sexo=registro[5],
        estado_civil=registro[6],
        email=registro[7],
        telefone=registro[8],
        celular=registro[9],
        cargo=registro[10],
        departamento=registro[11],
        salario=registro[12],
        data_admissao=registro[13],
        data_demissao=registro[14],
        turno=registro[15],
        status=registro[16],
        observacoes=registro[17]
    )

    def salvar(self, funcionario):
        sql = """
                INSERT INTO funcionario
                (
                    nome,
                    cpf,
                    rg,
                    data_nascimento,
                    sexo,
                    estado_civil,
                    email,
                    telefone,
                    celular,
                    cargo,
                    departamento,
                    salario,
                    data_admissao,
                    data_demissao,
                    turno,
                    status,
                    observacoes
                )

                VALUES
                (
                    %s,%s,%s,%s,%s,%s,%s,%s,%s,

                    %s,%s,%s,%s,%s,%s,%s,%s
                )
                """
        valores = (
        funcionario.nome,
        funcionario.cpf,
        funcionario.rg,
        funcionario.data_nascimento,
        funcionario.sexo,
        funcionario.estado_civil,
        funcionario.email,
        funcionario.telefone,
        funcionario.celular,
        funcionario.cargo,
        funcionario.departamento,
        funcionario.salario,
        funcionario.data_admissao,
        funcionario.data_demissao,
        funcionario.turno,
        funcionario.status,
        funcionario.observacoes
        )
        # BLOCO DE TRATAMENTO DE ERRO:
        try:
            self.db.cursor.execute(sql, valores)
            self.db.commit()
            print("FUNCIONÁRIO CADASTRADO COM SUCESSO! :)")
        except Exception as erro:
            self.db.rollback()
            print(f"ERRO AO CADASTRAR FUNCIONÁRIO! {erro} :(")


            print("ALGO DEU ERRADO. :(")

    def buscar_por_id(self, id_funcionario):
        sql = """
            SELECT *
            FROM funcionario
            WHERE id_funcionario = %s
        """

        try:
            self.db.cursor.execute(sql, (id_funcionario,))

            registro = self.db.cursor.fetchone()
            if registro is None:
                return None

            return self.criar_funcionario(registro)

        except Exception as erro:
            print(f"ERRO AO BUSCAR FUNCIONÁRIO: {erro} :(")
            return None

    def listar(self):

            sql = """

                SELECT *

                FROM funcionario

                ORDER BY nome

            """

            try:

                self.db.cursor.execute(sql)

                registros = self.db.cursor.fetchall()


                funcionarios = []

                for registro in registros:
                    funcionarios.appende(self.criar_funcionario(registro))

                

                return funcionarios

            except Exception as erro:

                print(f"Erro ao listar funcionários: {erro}")

                return []
            
    def atualizar(self, funcionario):
        sql = """
                Update funcionario
                set
                    nome = %s,
                    cpf = %s,
                    rg = %s,
                    data_nascimento = %s,
                    sexo = %s,
                    estado_civil =%s,
                    email = %s,
                    telefone = %s,
                    celular =%s,
                    cargo =%s,
                    departamento =%s,
                    salario =%s,
                    data_admissao =%s,
                    data_demissao=%s,
                    turno =%s,
                    status=%s,
                    observacoes=%s
                    where id_funcionario = %s
            """
        valores = (
        funcionario.nome,
        funcionario.cpf,
        funcionario.rg,
        funcionario.data_nascimento,
        funcionario.sexo,
        funcionario.estado_civil,
        funcionario.email,
        funcionario.telefone,
        funcionario.celular,
        funcionario.cargo,
        funcionario.departamento,
        funcionario.salario,
        funcionario.data_admissao,
        funcionario.data_demissao,
        funcionario.turno,
        funcionario.status,
        funcionario.observacoes,
        funcionario.id_funcionario
        )
        try:
            self.db.cursor.execute(sql, valores)
            self.db.commit()
            if self.db.cursor.rowcount == 0:
                print("Funcionário NÃO ENCONTRADO!")
            else:
                print("funcionário atualizado!")

        except Exception as erro:
            self.db.rollback()
            print(f"Erro ao atualizar funcionário:{erro}")

    def excluir(self, id_funcionario):
        sql = """
            Delete From funcionario
            where id_funcionario = %s
        """
        try:
            self.db.cursor.execute(sql, (id_funcionario,))
            self.db.commit()
            if self.db.cursor.rowcount == 0:
                print("Funcionário não encontrado!")

            else:
                print("Funcionário excluido com sucesso!")


        except Exception as erro:
            self.db.rollback()
            print(f"Erro ao escluir usuário")

    def fechar(self):
        self.db.close()