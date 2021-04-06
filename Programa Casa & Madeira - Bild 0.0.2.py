from datetime import date
class Cliente(): #Fazer login, fazer um pedido, consultar situação do pedido
    def __init__(self, user, dados_clientes = {}):
        self.user = user
        self.dados_clientes = dados_clientes
        self.dados_clientes = {
            "charles": 1234,
            "edinara": 4321,
            "jonas": 9876
        }

    def cadastrar_cliente(self): # Cadastra um no Cliente
        self.usuario_cliente = input ("Criar usuário: ")
        if self.usuario_cliente in self.dados_clientes:
            print (f"Usuários {self.usuario_cliente} já cadastrado! Insira um novo usuário.")
            self.cadastrar_cliente()    
        else:
            self.senha_cliente = int (input ("Criar senha de 6 dígitos numéricos: "))
            self.dados_clientes[self.usuario_cliente] = senha_cliente
            print("Usuário e Senha cadastrado com sucesso! Faça Login para continuar.")
            self.fazer_login_cliente()

    def fazer_login_cliente(self): #Dá acesso ao Cliente para acessar seus pedidos.
        print ("Área do Cliente")
        self.usuario_cliente = input ("Digite seu usuário: ")
        if self.usuario_cliente  not in self.dados_clientes:
            print ("Usuário não cadastrado. Faça seu cadastro abaixo.")
            self.cadastrar_cliente()
        else:    
            self.senha_cliente = int (input ("Digite sua senha: "))
            if self.senha_cliente not in self.dados_clientes.values():
                print ("Senha inválida! Tente novamente")
                self.fazer_login_cliente()
            else:
                print (f"Bem vindo(a) {self.usuario_cliente}!")
                self.navegar()

    def navegar(self):
        opcao1 = int (input ("\n1 - Solicitar um serviço\n2 - Consultar pedidos em execução\n"))
        if opcao1 == 1:
            pedido = input ("""Qual o serviço que deseja: """)
            contato = input ("Deixe seu nome e um conato para que possamos contactar voce: ")
            data_atual = date.today()
            with open("pedidos_clientes.txt", "a+") as pedidos_clientes:
                pedidos_clientes.write(f"Cliente {self.usuario_cliente} em {data_atual}\n{pedido}\n{contato}\n\n")
                print ("Obrigado! Em breve entraremos em contato!\n")
        elif opcao1 == 2:
            with open("pedidos_clientes.txt", "r") as pedidos_clientes:
                print(pedidos_clientes.read())
        else:
            print ("Opção Inválida! Por favor, tente novamente.")
            self.navegar()
                                       
class Funcionario(Cliente):#Receber dados do pedido do cliente, informar status do pedido, entregar pedido, liberar cobrança.
    def __init__(self, user, dados_colaboradores = {}):   
        self.user = user
        self.dados_colaboradores = dados_colaboradores
        self.dados_colaboradores = {
            "Lucas": 101010,
            "Gilvan": 102020
        }
        super().__init__(user)

    def fazer_login_colaborador(self): # Da acesso ao Colaborador às tarefas do dia.
        print ("Área do Colaborador")
        usuario_colaborador = input ("Insira seu Usuário: ")
        if usuario_colaborador not in self.dados_colaboradores:
            print ("Colaborador não encontrado! Tente novamente.")
            self.fazer_login_colaborador()
        else:
            senha_colaborador = int (input ("Senha: "))
            if senha_colaborador not in self.dados_colaboradores.values():
                print ("Senha inválida! Tente novamente")
                self.fazer_login_colaborador()
            else:
                print (f"Bem vindo {usuario_colaborador}!\n")
                self.serviços()
    
    def serviços(self):
        print("1 - Visualizar Pedidos \n2 - Informar a conclusão de um Pedido\n")
        opcao = int (input("Escolha uma opção: "))
        if opcao == 1:
            with open("pedidos_clientes.txt", "r") as pedidos_clientes:
                print(pedidos_clientes.read())
            self.serviços()    
        elif opcao == 2:
            with open("pedidos_clientes.txt", "r") as pedidos_clientes:
                print(pedidos_clientes.read())
                nome_cliente = input ("Nome do cliente: ")
                data = input ("Data do pedido: ")
                pedido = input ("Descrição breve do pepido: ")
                with open("pedidos_clientes_concluidos", "a+") as pedidos_clientes_concluidos:
                    pedidos_clientes_concluidos.write(f"PEDIDO CONCLUÍDO.\nCliente: {nome_cliente}, em {data}. Pedido {pedido}.")
                self.serviços()    
        else:
            print("Opçao inválida! Tente novamente.")
            self.serviços()        

class Gerente(Funcionario): #Comprar materiais do pedido, pagar funcionário, cobrar cliente, contato com o cliente.
    def __init__(self, user, dados_gerente = {"Marcelo": 102030}):
        self.user = user
        self.dados_gerente = dados_gerente
        super().__init__(user)

    def fazer_login_gerente(self):
        gerente = input ("Digite seu usuário: ")
        if gerente in dados_gerente:
            print("Bem vindo, {gerente}!")
            self.ler_pedidos_clientes()
        else:
            print ("Usuário ou Senha incorreta! Tente Novamente.")
            self.fazer_login_gerente()

    def ler_pedidos_clientes(self):
        print ("1 - Ver Lista de Pedidos dos Clientes EM PRODUÇÃO\n2 - Ver Lista de Pedidos dos Clientes CONCLUÍDOS\n")
        opcao = int (input ("Digite a opção: "))
        if opcao == 1:
            with open("pedidos_clientes.txt", "r") as padidos_clientes:
                print(pedidos_clientes.read())
        elif opcao == 2:        
            with open("pedidos_clientes_concluidos.txt", "r") as pedidos_clientes_concluidos:
                print (pedidos_clientes_concluidos.read())
                prosseguir = int (input ("Digite 1 para Agendar Entregas ou 2 para Voltar: "))
                if prosseguir == 1:
                    print("Entregas agendadas com sucesso!")
                    self.ler_pedidos_clientes()
                elif prosseguir == 2:
                    self.ler_pedidos_clientes()
                else:
                    print("Opção Inválida! Tente novamente.")
                    self.ler_pedidos_clientes()    

class Marcenaria(Gerente):
    def __init__(self, user):
        self.user = user
        super().__init__(user)

    def identificar(self): #Identifica se o usuário é Cliente ou Colaborador.
        print ("\nBem vindo ao Casa & Madeira\n")
        print ("Faça Login para prosseguir:")
        identificar = int (input ("1 - Sou Cliente\n2 - Sou Colaborador\n"))
        if identificar == 1:
            self.fazer_login_cliente()
        elif identificar == 2:
            self.fazer_login_colaborador()
        else:
            print("Opção Inválida! Tente novamente.")
            self.identificar()    
                 

user = Marcenaria('eu')
user.identificar()