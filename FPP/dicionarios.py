Produto = {
    'Codigo':       0,
    'Descricao':    0,
    'Preco':        0.0,
    'Quantidade':   0.0
}

Produto['Codigo'] = int(input("Digite o codigo do produto: "))
Produto['Descricao'] = input("Digite a descrição do produto: ")
Produto['Preco'] = float(input("Digite o preço do produto: "))
Produto['Quantidade'] = float(input("Digite a quantidade do produto: "))

print("Codigo: ", Produto['Codigo'])
print("Descrição: ", Produto['Descricao'])
print("Preço: ", Produto['Preco'])
print("Quantidade: ", Produto['Quantidade'])