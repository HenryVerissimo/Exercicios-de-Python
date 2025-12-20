# Desafio de Lógica: Processador de Performance Comercial (PPC)

## 🎯 Objetivo
Desenvolver um motor de processamento de dados para analisar o desempenho de vendas de uma unidade de negócio, consolidando informações financeiras e gerando métricas de performance para a diretoria.

## 📋 Enunciado do Problema
Você recebeu um conjunto de dados brutos contendo o registro de transações comerciais. O sistema deve processar esses dados para aplicar regras de bonificação variáveis e gerar um relatório consolidado que segmente os resultados por categoria de produto e identifique outliers de desempenho.

---

## 🛠️ Requisitos Funcionais

### 1. Cálculo de Remuneração Variável
O sistema deve aplicar uma taxa de bônus sobre o valor bruto de cada venda, seguindo rigorosamente as faixas abaixo:
- **Faixa Ouro:** Vendas acima de R$ 5.000,00 -> Bônus de 15%.
- **Faixa Prata:** Vendas de R$ 2.000,00 até R$ 5.000,00 -> Bônus de 10%.
- **Faixa Bronze:** Vendas abaixo de R$ 2.000,00 -> Bônus de 5%.

### 2. Consolidação por Segmento
O software deve agrupar o volume total financeiro (soma dos valores das vendas) para cada categoria de produto presente nos dados de entrada.

### 3. Extração de Métricas de Performance
O processamento deve resultar nas seguintes informações estatísticas:
- **Top Performer:** Identificação do colaborador que obteve o maior valor absoluto de bônus.
- **Ticket Médio:** O valor médio das vendas realizadas no período analisado.
- **Volume Total:** O somatório de todas as vendas brutas.

---

## ✅ Critérios de Aceitação

Para que o desafio seja considerado concluído, o código deve atender aos seguintes pontos:

- [ ] **Exatidão Financeira:** O cálculo do bônus deve respeitar as faixas de corte e ser aplicado individualmente.
- [ ] **Formatação de Saída:** Todos os valores monetários exibidos no terminal devem conter o prefixo `R$` e duas casas decimais (Ex: `R$ 1.250,50`).
- [ ] **Integridade de Dados:** O sistema deve ignorar ou tratar entradas onde o valor da venda seja igual ou inferior a zero (validação de segurança).
- [ ] **Agrupamento Dinâmico:** A soma por categoria deve funcionar mesmo que novas categorias (além das do exemplo) sejam adicionadas à lista original.
- [ ] **Saída Estruturada:** O relatório final deve ser claro e legível, separando as métricas individuais das métricas globais da loja.

---

## 📥 Dados de Entrada de Exemplo
Utilize a estrutura abaixo para validar sua lógica:

```python
dataset = [
    {"vendedor": "Ana", "valor": 7200.00, "categoria": "Eletrônicos"},
    {"vendedor": "João", "valor": 1200.00, "categoria": "Vestuário"},
    {"vendedor": "Maria", "valor": 3500.00, "categoria": "Eletrônicos"},
    {"vendedor": "Pedro", "valor": 4100.00, "categoria": "Alimentos"},
    {"vendedor": "Clara", "valor": 950.00, "categoria": "Vestuário"},
    {"vendedor": "Beatriz", "valor": 5000.00, "categoria": "Eletrônicos"}
]