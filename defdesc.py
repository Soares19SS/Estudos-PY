def calcular_desconto(preco, porcentagem):
    return preco - (preco * porcentagem / 100)

valor_final = calcular_desconto(1010, 25)
print(f'O valor final com desconto é de: R${valor_final:.2f}')