import os

class Sabores():
    def __init__(self):
        self.tipos_sabores = [
            '\033[92m1 - Voltar\033[0m', '2 - Calabresa', '3 - Quatro Queijos', '4 - Frango com Catupiry', '5 - Portuguesa',
            '6 - Pepperoni', '7 - Mussarela', '8 - Vegetariana', '         9 - Atum ', '10 - Bacon com Milho',
            '11 - Rúcula com Tomate Seco', '12 - Alho e Óleo', '13 - Chocolate com Morango',
            '14 - Banana com Canela', '15 - Brocolis com Catupiry', '16 - Margherita'
        ]

        self.tipos_bordas = ['1 - Tradicional', '2 - Catupiry', '3 - Cheddar', '4 - Chocolate', '5 - Recheada com Presunto e Queijo', '6 - Sem Borda']


    def um_sabor(self):
        main_instance.limpeza()

        # Dividir a lista em duas partes
        primeira_parte = self.tipos_sabores[:8]
        segunda_parte = self.tipos_sabores[8:]

        # Imprimir as duas colunas
        print("Possuímos os seguintes sabores:\n")
        for sabor1, sabor2 in zip(primeira_parte, segunda_parte):
            print(f"{sabor1:<40} {sabor2}\n")
        print('-------------------------')
        
        sabor_selecionado = int(input('Qual sabor você deseja? '))
        if sabor_selecionado in range(1, len(self.tipos_sabores) + 1):
            sabor_escolhido = self.tipos_sabores[sabor_selecionado - 1]
            if sabor_selecionado == 1:
                main_instance.limpeza()
                main_instance.cardapio()
            else:
                print(f'\nVocê selecionou: \033[92m{sabor_escolhido.split(" - ")[1]}\033[0m\n')
                input('Pressione Enter para continuar...')
                self.bordas()
        else:
            print('-------------------------')
            print('\033[91m\nSelecione um valor válido.\033[0m\n')
            input('Pressione Enter para continuar...')
            self.um_sabor()


    def dois_sabores(self):
        main_instance.limpeza()
        # Utilizando a lista de sabores já definida na inicialização
        primeira_parte = self.tipos_sabores[:8]
        segunda_parte = self.tipos_sabores[8:]

        print("Possuímos os seguintes sabores:\n")
        for sabor1, sabor2 in zip(primeira_parte, segunda_parte):
            print(f"{sabor1:<40} {sabor2}\n")
        print('-------------------------')
        sabor_selecionado1 = int(input('Qual o primeiro sabor da sua Pizza? '))
        if sabor_selecionado1 == 1:
            main_instance.limpeza()
            main_instance.cardapio()
        else:            
            sabor_selecionado2 = int(input('\nQual o segundo sabor da sua Pizza? '))
            if sabor_selecionado2 == 1:
                main_instance.limpeza()
                main_instance.cardapio()
            else:
                if sabor_selecionado1 in range(1, len(self.tipos_sabores) + 1) and sabor_selecionado2 in range(1, len(self.tipos_sabores) + 1):
                    sabor_escolhido1 = self.tipos_sabores[sabor_selecionado1 - 1]
                    sabor_escolhido2 = self.tipos_sabores[sabor_selecionado2 - 1]
                else:
                    print('-------------------------')
                    print('\033[91m\nSelecione um valor válido.\033[0m\n')
                    self.dois_sabores()

        print(f'\nVocê selecionou: \033[92m{sabor_escolhido1.split(" - ")[1]}\033[0m e \033[92m{sabor_escolhido2.split(" - ")[1]}\033[0m\n')
        input('Pressione Enter para continuar...')
        self.bordas()


    def voltar(self):
        main_instance.limpeza()
        main_instance.cardapio()


    def bordas(self):
        main_instance.limpeza()

        

class Main():
    def limpeza(self):
        os.system('cls')

    def boas_vindas(self):
        self.limpeza()
        print('''\n\033[92m
     _______  ______    __   ________   ________       ___      
    /       ||   _  \  |  | |       /  |       /      /   \     
   |   (----`|  |_)  | |  | `---/  /   `---/  /      /  ^  \    
    \   \    |   ___/  |  |    /  /       /  /      /  /_\  \   
.----)   |   |  |      |  |   /  /----.  /  /----. /  _____  \  
|_______/    | _|      |__|  /________| /________|/__/     \__\ 
                                                                
                                              
    \033[0m\n''')
        input('Pressione Enter para continuar...')
        self.limpeza()

    def mensagem(self):
        msg = 'Cardápio'
        self.limpeza()
        quantidade_letras = 0
        for letra in msg:
            if letra.isalpha():
                quantidade_letras += 1
        print('-'*quantidade_letras)
        print(msg)
        print('-'*quantidade_letras)

    def cardapio(self):
        print('Que tipo de pizza você deseja?\n')
        print('1 - Um sabor\n')
        print('2 - Dois sabores\n')
        
        divisao_pizza = None
        while divisao_pizza not in [1, 2]:
            try:
                divisao_pizza = int(input('- '))
                print()
                if divisao_pizza not in [1, 2]:
                    print("\033[91mOpção inválida. Escolha 1 ou 2.\033[0m\n")
            except ValueError:
                input("\033[91m\nPor favor, insira um valor válido.\033[0m")
                self.limpeza()
                self.cardapio()


        sabores_instance = Sabores()
        if divisao_pizza == 1:
            sabores_instance.um_sabor()
        elif divisao_pizza == 2:
            sabores_instance.dois_sabores()


if __name__ == "__main__":
    main_instance = Main()
    main_instance.limpeza()
    main_instance.boas_vindas()
    main_instance.mensagem()
    main_instance.cardapio()
    sabores_instance = Sabores()
    sabores_instance.um_sabor()
    sabores_instance.dois_sabores()
    sabores_instance.voltar()
    sabores_instance.bordas()
