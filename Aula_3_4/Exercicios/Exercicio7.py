# Crie uma classe chamada Banco que represente um banco. A classe deve ter atributos para armazenar uma lista de contas bancárias.
# Crie métodos para adicionar (criar_conta(titular, saldo_inicial)), remover (encerrar_conta(numero)), exibir o total de saldo de todas as contas (total_saldo())

class ContaBancaria:
    def __init__(self, numero, titular, saldo_inicial):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo_inicial

class Banco:
    def __init__(self):
        self.contas = []

    def criar_conta(self, titular, saldo_inicial):
        novo_numero = len(self.contas) + 1
        nova_conta = ContaBancaria(novo_numero, titular, saldo_inicial)
        self.contas.append(nova_conta)
        return novo_numero

    def encerrar_conta(self, numero):
        conta_encerrada = None
        for conta in self.contas:
            if conta.numero == numero:
                conta_encerrada = conta
                break

        if conta_encerrada:
            self.contas.remove(conta_encerrada)
            return f"Conta {numero} encerrada com sucesso."
        else:
            return f"Conta {numero} não encontrada."

    def total_saldo(self):
        saldo_total = sum(conta.saldo for conta in self.contas)
        return saldo_total

# Exemplo de uso
banco = Banco()

numero_conta1 = banco.criar_conta("João", 1000)
numero_conta2 = banco.criar_conta("Maria", 1500)

print(banco.total_saldo())  # Saída: 2500

banco.encerrar_conta(numero_conta1)
print(banco.total_saldo())  # Saída: 1500
