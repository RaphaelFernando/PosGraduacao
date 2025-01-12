#A passagem de parâmetros serve como um ponto de comunicação entre uma função e a chamada na mesma no meio do código,
#  possibilita a passagem de valores manipulados no código para a função, 
# a função pode ou não se utilizar destes dados passados por parâmetros para executar ações dentro da função. Com base no exposto, 
# vejamos o código a seguir:

 

def ObtemRegiao(uf):

    if (uf == "PA") or (uf == "AM") or (uf == "AP") or (uf == "RR") or (uf == "AC") or (uf == "RO") or (uf == "TO"):

        x = "Norte"

    if (uf == "BA") or (uf == "SE") or (uf == "AL") or (uf == "PE") or (uf == "PB") or (uf == "RN") or (uf == "CE") or (uf == "PI") or (uf == "MA"):

        x = "Nordeste"

    if (uf == "GO") or (uf == "MT") or (uf == "MS") or (uf == "DF"):

        x = "Centro-Oeste"

    if (uf == "SP") or (uf == "RJ") or (uf == "ES") or (uf == "MG"):

        x = "Sudeste"    

    if (uf == "PR") or (uf == "SC") or (uf == "RS"):

        x = "Sul"

    #return x

 

uf=str(input("Digite um Estado: "))

regiao=ObtemRegiao(uf)

print("Região do Estado: ", regiao)

 

#Assinale a alternativa correta sobre o código apresentado é:
 

#Alternativas
#Alternativa 1:
#O algoritmo não prosseguirá por que têm um erro sintático no código fonte.

#Alternativa 2:
#O algoritmo será interrompido com um erro na digitação de um Estado inválido.

#Alternativa 3:
#Nenhum nome de região será mostrado como resultado na última linha do algoritmo.

#Alternativa 4:
#Se dois Estados forem informados como entrada, será exibida apenas a região do primeiro.

#Alternativa 5:
#A variável uf recebida por parâmetro em ObtemRegiao() é exatamente a mesma declarada no algoritmo principal.

# Resposta correta é a questão 3.