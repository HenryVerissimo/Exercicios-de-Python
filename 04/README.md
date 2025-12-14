# 💻 Exercício de Lógica de Programação: Contagem de Anagramas por Grupo

## 🎯 Nível: Intermediário

### 📝 Enunciado

Você receberá uma lista de palavras (strings). Sua tarefa é agrupar essas palavras de forma que todos os membros de um grupo sejam **anagramas** entre si.

Após agrupar todas as palavras em seus respectivos grupos de anagramas, o objetivo final é determinar **quantos grupos distintos de anagramas existem** e qual é o **tamanho do maior grupo encontrado**.

### 💡 Definição de Anagrama

Duas palavras são anagramas uma da outra se puderem ser formadas reorganizando as letras da outra.

* **Exemplo:** `"listen"` e `"silent"` são anagramas.

### ⚙️ Requisitos de Implementação e Detalhes

1.  **Entrada:** Uma lista de strings (palavras), por exemplo: `["eat", "tea", "tan", "ate", "nat", "bat", "AET", "cat"]`.
2.  **Saída:** Sua função ou programa deve retornar uma estrutura de dados (ex: tupla ou lista em Python) contendo dois valores inteiros:
    * O **número total de grupos** de anagramas distintos encontrados.
    * O **tamanho do maior grupo** (o grupo com o maior número de palavras).
3.  **Case-Insensitive:** A comparação deve ser *case-insensitive* (não sensível a maiúsculas/minúsculas). Por exemplo, `"Ato"` e `"oat"` devem ser considerados anagramas.
4.  **Assunções:** Assuma que as palavras contêm apenas letras do alfabeto (A-Z ou a-z).

### 🔑 Resultado Esperado para o Exemplo

Para a entrada `["eat", "tea", "tan", "ate", "nat", "bat", "AET", "cat"]`, os grupos são:

* Grupo 1: \["eat", "tea", "ate", "AET"]
* Grupo 2: \["tan", "nat"]
* Grupo 3: \["bat"]
* Grupo 4: \["cat"]

A saída esperada é: `(4, 4)`

* **Número Total de Grupos:** 4
* **Tamanho do Maior Grupo:** 4