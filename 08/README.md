# Desafio de Lógica: Sistema de Roteamento Interplanetário

## 🚀 Contexto
O objetivo é desenvolver o motor lógico para uma transportadora galáctica. O sistema deve ser capaz de processar um lote de pedidos, validar as restrições de carga, calcular os custos de frete com base em múltiplas variáveis e determinar a ordem de saída das entregas conforme critérios de prioridade técnica.

---

## 📋 Requisitos de Dados

Cada **Pedido** de entrada deve conter as seguintes propriedades:

| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `id` | Inteiro | Identificador único do pedido. |
| `peso` | Decimal | Peso da carga em quilogramas (kg). |
| `distancia` | Decimal | Distância do destino em Anos-Luz (AL). |
| `tipo_carga` | String | Categorias: `Comum`, `Perigosa` ou `Vital`. |
| `urgencia` | Inteiro | Escala de 1 a 5 (onde 5 é a prioridade máxima). |

---

## ⚙️ Regras de Negócio

### 1. Cálculo de Custos
O valor final deve ser calculado partindo de um **Custo Base de 100 créditos**, aplicando as seguintes regras sucessivas:

1.  **Distância:** +10 créditos para cada 1 Ano-Luz completo.
2.  **Peso:** Se `peso > 500kg`, adicionar 15% sobre o valor acumulado.
3.  **Adicionais por Categoria:**
    * **Perigosa:** +50 créditos (Seguro de Contenção).
    * **Vital:** +100 créditos (Suporte de Vida).
4.  **Desconto Especial:** Se `distancia < 5` E `tipo_carga == "Comum"`, aplicar 5% de desconto sobre o valor total final.

### 2. Algoritmo de Priorização
A ordem de processamento dos pedidos deve seguir esta hierarquia:
1.  **Tipo de Carga:** Pedidos `Vital` possuem prioridade absoluta.
2.  **Urgência:** Em caso de empate no tipo (ou para outros tipos), o maior nível de `urgencia` vence.
3.  **Distância:** Se o nível de urgência for igual, o pedido com a **menor distância** deve ser processado primeiro.

---

## 🛡️ Validações e Restrições

O sistema deve invalidar pedidos que não cumpram os critérios operacionais:

* **Capacidade da Nave:** O peso máximo por pedido é de **2.000kg**. Pedidos acima disso devem ser rejeitados.
* **Integridade de Dados:** Distâncias iguais ou menores que zero são consideradas erros de navegação.

---

## 📤 Saída Esperada (Output)

O processamento deve resultar em um relatório estruturado contendo:

1.  A listagem de pedidos **ordenada** pela prioridade.
2.  O status de cada item: `Sucesso`, `Erro: Excesso de Peso` ou `Erro: Destino Inválido`.
3.  O valor individual de cada frete aprovado.
4.  O **Somatório Total** de créditos a serem recebidos pelo lote completo.

---

> **Dica de Implementação:** Tente isolar a lógica de cálculo da lógica de ordenação para manter o código limpo e escalável.