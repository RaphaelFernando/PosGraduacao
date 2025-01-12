#Sequência de Fibonacci é uma sucessão de números que aparece codificada em muitos fenômenos da natureza. 
# Descrita no final do século 12 pelo matemático italiano Leonardo Fibonacci, ela é infinita e começa com 0 e 1. 
# Os números seguintes são sempre a soma dos dois números anteriores. Portanto: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34?

def fib(x):

    if(x == 0 or x == 1):

        return x

    else:

        return fib(x-2) + fib(x-1)

n = 7

resultado = fib(n)

print(resultado)

#Realizando o teste de mesa, avalie as alternativas abaixo e assinale a que corresponde à realidade.

#Alternativas
#Alternativa 1:
#Quando o algoritmo atingir a execução da linha 15, será impresso o número 8 (oito) na tela.

#Alternativa 2:
#Quando o algoritmo atingir a execução da linha 15, será impresso o número 13 (treze) na tela.

#Alternativa 3:
#Quando o algoritmo atingir a execução da linha 15, será impresso o número 0 (zero) na tela.

#Alternativa 4:
#Quando o algoritmo atingir a execução da linha 15, será impresso o número 1 (hum) na tela.

#Alternativa 5:
#Quando o algoritmo atingir a execução da linha 15, será impresso o número 7 (sete) na tela.

#A resposta é alternativa 2,vai ser impresso o numero 13.