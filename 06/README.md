# Desafio de Lógica de Programação: Processamento Avançado de Strings

## 🎯 Objetivo

Criar uma função em Python que aceite uma *string* como entrada e execute duas tarefas distintas de processamento de texto:
1.  **Inverter a String:** Reverter a ordem de todos os caracteres da *string* de entrada.
2.  **Contar Vogais Únicas:** Contar o número total de **vogais únicas** presentes na *string*.

## 📖 Enunciado

Desenvolva uma função chamada `process_string(text)` que receba um único argumento (`text`, que é uma *string*) e retorne uma tupla contendo dois elementos:
1.  A *string* de entrada com seus caracteres invertidos.
2.  Um número inteiro que representa a contagem de **vogais únicas** (A, E, I, O, U) encontradas na *string*, independentemente de estarem em minúsculas ou maiúsculas.

## 📝 Requisitos e Restrições

1.  A função deve ser capaz de lidar corretamente com *strings* vazias.
2.  A contagem de vogais deve ser **case-insensitive** (não deve distinguir maiúsculas de minúsculas).
3.  **Vogais Únicas:** Considere apenas as cinco vogais padrão do alfabeto português/inglês (a, e, i, o, u). A contagem deve ser baseada na **quantidade de vogais distintas** que aparecem na *string*, e não na frequência total de vogais.

| Vogal | Contagem |
| :---: | :---: |
| A/a | 1 (se presente) |
| E/e | 1 (se presente) |
| I/i | 1 (se presente) |
| O/o | 1 (se presente) |
| U/u | 1 (se presente) |

4.  A função deve retornar estritamente uma tupla: `(string_invertida, contagem_vogais_unicas)`.

## 💡 Exemplo de Uso

```python
entrada_1 = "A Casa Amarela"
# String Revertida: "aleramA asaC A"
# Vogais Únicas Presentes: A, E (O 'i', 'o' e 'u' não estão presentes)
# Contagem Esperada: 2

entrada_2 = "sequoia"
# String Revertida: "aiouqes"
# Vogais Únicas Presentes: A, E, I, O, U
# Contagem Esperada: 5