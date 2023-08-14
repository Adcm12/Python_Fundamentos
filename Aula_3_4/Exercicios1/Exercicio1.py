# 1 - Classe Conta Bancária:
# Crie uma classe chamada ContaBancaria que simule uma conta
#  bancária simples. A classe deve ter os atributos titular,
#  saldo e numero. Crie métodos para depositar (depositar(valor))
# e sacar (sacar(valor)) dinheiro da conta, além de um método para
#  exibir o saldo atual (exibir_saldo()).

class ContaBancaria:
    mensagem_input = '\n1) Depositar, '
    mensagem_input += '\n2) Sacar, \n3) Exibir, \n4) Sair: '
    titular = 'Adrian Castillo'
    saldo = 0
    numero = 569784

    def deposita(valor):
        try:
            valor = float(valor)
            ContaBancaria.saldo += valor
            print('\nDeposito feito con succeso!!!')
        except:
            print('\nInforme um valor válido para depósito!')

    def saca(valor):
        try:
            valor = float(valor)
            ContaBancaria.saldo -= valor
            print('\nSaque realizado con sucesso!!!')
        except:
            print('Informe um valor válido para depósito!')

    def exibe():
        print(
            f'\nTitular: {ContaBancaria.titular}\nNumero de conta: {ContaBancaria.numero}\nSaldo: {ContaBancaria.saldo}'
        )

    def script():   
        while True:
            try:
                opcao = input(ContaBancaria.mensagem_input)
                if opcao == '1':
                    valor = input('\nInforme o valor: ')
                    ContaBancaria.deposita(valor)
                elif opcao == '2':
                    valor = input('\nInforme o valor: ')
                    ContaBancaria.saca(valor)
                elif opcao == '3':
                    ContaBancaria.exibe()
                elif opcao == '4':
                    print('\nVolte sempre com dinheiro!!')
                    break
            except:
                print('Informe uma opção válida!')

if __name__ == '__main__':
    ContaBancaria.script()