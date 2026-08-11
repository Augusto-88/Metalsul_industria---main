from repositories.funcionario_repository import FuncionarioRepository


def main():

    repository = FuncionarioRepository()

    funcionario = repository.buscar_por_id(1)

    if funcionario:

        funcionario.salario = 8200.00
        funcionario.departamento = "Tecnologia"
        funcionario.cargo = "Analista Sênior"

        repository.atualizar(funcionario)

    else:
        print("Funcionário não encontrado.")

    repository.fechar()


if __name__ == "__main__":
    main()
    