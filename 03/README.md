# Desafio de Lógica: Análise de Sequência de Transações Bancárias

## Enunciado

Você deve criar um programa que simule o processamento de uma série de transações bancárias e gere um relatório de análise com base nos dados fornecidos.

A entrada do seu programa será uma lista de transações, onde cada transação é representada por um par de informações: o tipo de operação (que pode ser a *string* `"DEPOSITO"` ou `"SAQUE"`) e o valor da transação (um número positivo).

Seu programa deve realizar as seguintes tarefas obrigatórias, processando as transações na ordem em que aparecem:

1.  **Cálculo do Saldo Final:** Determine o saldo final da conta, considerando um saldo inicial de R$ 0,00.
2.  **Regra de Saque:** Um saque só deve ser efetuado se o saldo atual for **suficiente** para cobrir o valor da transação. Se o saldo for insuficiente, o saque deve ser **ignorado** (o saldo permanece o mesmo) e a transação não deve ser contabilizada.
3.  **Identificar a Maior Sequência de Depósitos:** Encontre e reporte o comprimento da maior sequência contínua (subsequência) de operações do tipo `"DEPOSITO"` que ocorreu na lista de transações.

## Requisitos de Saída

A saída esperada deve conter o Saldo Final calculado e o comprimento da Maior Sequência Contínua de Depósitos.