# Exercício de Lógica de Programação: Análise de Dados de Sensores de Temperatura

## Objetivo

Desenvolver habilidades em manipulação de listas, uso de estruturas de repetição (loops) e aplicação de lógica condicional para filtragem e processamento de dados numéricos.

## Descrição do Problema

Escreva um programa em Python que processe uma lista de temperaturas em graus Celsius, realizando três análises distintas:

### 1. Contagem de Anomalias

Conte quantas leituras na lista são consideradas anômalas. Uma leitura é anômala se:
* `Temperatura > 30°C` (Calor Extremo)
* **OU**
* `Temperatura < 10°C` (Frio Extremo)

### 2. Cálculo da Média Válida

Calcule a média aritmética de todas as leituras **válidas**. Uma leitura é válida se:
* `10°C <= Temperatura <= 30°C`
* Se a lista não contiver nenhuma leitura válida, a média deve ser `0`.

### 3. Identificação do Pico Válido

Encontre o **índice (posição)** da **primeira** ocorrência da temperatura máxima dentre as leituras **válidas**.
* Se não houver nenhuma leitura válida na lista, retorne o índice `-1`.

## Requisitos Técnicos

* **Linguagem:** Python.
* **Restrições:** A solução deve ser implementada usando apenas a lógica de programação básica da linguagem. O uso de bibliotecas externas (e.g., `numpy`, `pandas`) é proibido.
* **Entrega:** Uma função que aceite a lista de temperaturas e retorne os três resultados solicitados.