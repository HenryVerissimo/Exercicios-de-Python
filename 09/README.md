# Desafio de Lógica: Sistema de Gestão de Biblioteca Técnica

Este desafio tem como objetivo exercitar conceitos de lógica de programação intermediária utilizando a linguagem **Python**. O foco está na manipulação de estruturas de dados (listas e dicionários), tratamento de strings, ordenação e lógica de busca.

## 📝 Contexto do Projeto
Você deve desenvolver o motor de lógica para um sistema que organiza o acervo de uma biblioteca. O sistema deve processar entradas de dados brutas (strings formatadas) e transformá-las em informações estruturadas, permitindo consultas e relatórios.

---

## 🛠️ Requisitos Funcionais

### 1. Processamento e Estruturação
O sistema deve iniciar com uma base de dados bruta (uma lista de strings).
* **Formato da entrada:** `"Título | Autor | Ano | Categoria"`
* **Ação:** Criar uma função que processe essas strings, remova espaços em branco desnecessários e armazene os dados em uma estrutura de **Lista de Dicionários**.

### 2. Interface de Usuário (Menu)
O programa deve rodar em um loop, oferecendo as seguintes opções:

* **Listar por Categoria:** O usuário informa uma categoria e o sistema exibe os livros correspondentes, ordenados do **mais novo para o mais antigo**.
* **Busca por Autor:** Realizar uma busca por substring (não sensível a maiúsculas/minúsculas). Se o usuário digitar "Robert", o sistema deve encontrar "Robert C. Martin", por exemplo.
* **Relatório Estatístico:** Exibir:
    * A média de idade dos livros (baseado no ano atual).
    * A categoria com o maior volume de títulos.
* **Sair:** Encerra a execução do programa.

### 3. Regras de Negócio e Validação
* **Validação de Data:** Não permitir o processamento ou cadastro de livros com anos de publicação futuros.
* **Feedback:** Caso uma busca não encontre resultados, exibir uma mensagem clara ao invés de uma tela vazia.
* **Persistência Temporária:** As alterações (como o status de empréstimo) devem durar enquanto o programa estiver em execução.

---

## 🚀 Desafio Adicional (Diferencial)
Implemente uma funcionalidade de **Gestão de Empréstimos**:
1. Adicione um campo `disponivel` (booleano) para cada livro.
2. Crie uma opção no menu para "Emprestar Livro".
3. Se o livro estiver disponível, altere para `False`. Se já estiver emprestado, avise o usuário.

---

## 💡 Sugestões de Implementação para Python
* Utilize o método `.split('|')` para separar os dados.
* Use a função `sorted()` com uma `lambda` function para a ordenação por ano.
* Trate as entradas do usuário com `.strip().lower()` para evitar erros de digitação.