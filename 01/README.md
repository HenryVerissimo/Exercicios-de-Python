# 💡 Exercício de Lógica de Programação em Python: Cálculo de Desconto

---

## 🚀 O Desafio

Você deve criar um programa em Python que simule o cálculo de **desconto** em uma compra baseando-se no **valor total** e na **categoria do cliente**.

---

## 📋 Requisitos de Implementação

1.  **Entrada de Dados:**
    * **Solicite** ao usuário que insira o **valor total da compra** (espera-se um número decimal).
    * **Solicite** ao usuário que insira a **categoria do cliente** como uma única letra maiúscula.

2.  **Regras de Desconto:**
    * Utilize a letra inserida para determinar o desconto a ser aplicado:
        * **'P'** (Premium): 15% de desconto.
        * **'E'** (Especial): 10% de desconto.
        * **'C'** (Comum): 5% de desconto.

3.  **Processamento e Saída:**
    * O programa deve calcular o **valor final a pagar** após a aplicação do desconto.
    * O programa deve **imprimir** o valor final calculado.

4.  **Tratamento de Erros:**
    * Se a **categoria** inserida for **inválida** (diferente de 'P', 'E' ou 'C'), o programa deve imprimir uma **mensagem de erro** (`"Categoria de cliente inválida. Nenhum desconto será aplicado."`) e exibir o valor total **original** da compra.

---

## Exemplo de Interação

| Entrada do Usuário | Saída Esperada |
| :--- | :--- |
| Valor: 100.00, Categoria: P | O valor final a pagar é: R$ 85.00 |
| Valor: 50.00, Categoria: C | O valor final a pagar é: R$ 47.50 |
| Valor: 200.00, Categoria: X | Categoria de cliente inválida. Nenhum desconto será aplicado. O valor final a pagar é: R$ 200.00 |