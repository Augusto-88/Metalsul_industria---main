from repositories.funcionario_repository import FuncionarioRepository


class Menu:
    def __init__(self):
        self.repository = FuncionarioRepository()

#Futuru submenu funcionário

    def exibir(self):
        while True:
            print()
            print("="*60)
            print("METALSUL - SISTEMA DE GERENCIAMENTO")
            print("="*60)
            print("1 - Cadastrar Funcinario: ")
            print("2 - Buscar Funcinario: ")
            print("3 - Listar Funcinario: ")
            print("4 - Atualizar Funcinario: ")
            print("5 - Excluir Funcinario: ")
            print("0 - Sair: ")
            print("="*60)

            opcao = input("Escolha sua opção: ")
            if opcao == "1":
                self.cadastrar_funcionario()

            elif opcao == "2":
                self.buscar_funcionario()

            elif opcao == "3":
                self.listar_funcionario()


            elif opcao == "4":
                self.atualizar_funcionario()

            elif opcao == "5":
                self.excluir_funcionario()

            elif opcao == "0":
                self.repository.fechar()
                print("\nEncerrando o sistema...")                
                break
            else:
                print("Opção inválida")

    def buscar_funcionario(self):
        pass

    def listar_funcionario(self):
            pass

    def atualizar_funcionario(self):
            pass
    
    def excluir_funcionario(self):
            pass
