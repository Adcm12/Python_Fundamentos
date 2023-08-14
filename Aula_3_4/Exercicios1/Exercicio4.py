#  Crie uma classe chamada Agenda que represente uma agenda de contatos. A classe deve ter um atributo para armazenar uma lista de contatos.
#  Crie métodos para adicionar (adicionar_contato(nome, telefone)), remover (remover_contato(nome)), e exibir todos os contatos (exibir_contatos()).

class Agenda:
    
    contatos = []
    
    def adicionar_contato(item_lista):
        Agenda.contatos.append([item_lista])
        print('Adicionado con sucesso')
    
    def remover_contato(posicion):
        Agenda.contatos.pop(posicion)
        print('Removido con sucesso')
    
    def exibir_contatos():
        
        if len(Agenda.contatos) > 0:

            for i, valor in range(len(Agenda.contatos)):
                print(f'Posicion: {i}  Nombre: {Agenda.contatos[i][0]}  Telefone: {Agenda.contatos[i][1]}')

    def script():
        while True:

            try:
                metodo = input('Informe el metodo: ')

                if metodo == 'adicionar':
                    novo_item = input('Digite o item a ser adicionado na agenda: ')
                    novo_numero =int(input('Adicione o telefone: '))
                    Agenda.adicionar_contato([Agenda.item_lista])

                elif metodo == 'remover':

                    posicion = int(input('informe la poscion: '))
                    Agenda.remover_contato(posicion)

                elif metodo == 'exibir':

                    Agenda.exibir_contatos()

                elif metodo == 's':

                    break


            except Exception as erro:
                print('error')

Agenda.script()