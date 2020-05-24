def criar_conta(numero, titular, saldo, limite):
    return {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}

def depositar(conta, valor):
    conta["saldo"] += valor

def sacar(conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    return print("O saldo da sua conta é R$ {}" .format(conta["saldo"]))
