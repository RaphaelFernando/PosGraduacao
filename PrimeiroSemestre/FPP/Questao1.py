#A realização de testes de mesa em algoritmos que contém estruturas de decisão deve considerar o monitoramento de atribuições a variáveis,
#  valores de entrada e saída, constantes e a resolução de expressões. Além disso,
#  é preciso compreender o fluxo do algoritmo analisando o comportamento das condições presentes no código.
#  Considere a realização de um teste de mesa sobre o algoritmo abaixo.

Resto=0

Numero=int(input("Digite um número inteiro:"))

Resto = Numero % 2;

if (Resto == 0):

      print("Condição satisfeita. par\\n")

else:

      print("Condição não Satisfeita. impar\\n")


#De acordo com os resultados encontrados em seu teste de mesa, avalie as afirmações abaixo.

#I - O operador "percento" (%), remete à operação do cálculo do resto da divisão inteira entre dois números.

#II - O uso do símbolo % resulta em uma divisão entre os dois números.

#III - A mensagem do ELSE será impressa caso o número seja ímpar.

#Sendo assim, é correto o que se afirma em:

#Resposta correta é I, II e III.