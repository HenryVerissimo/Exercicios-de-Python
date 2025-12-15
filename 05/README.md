# 💻 Desafio de Lógica de Programação: Análise de Log Simples

Este desafio envolve a criação de um sistema básico para gerar, processar e analisar dados de log, utilizando **Bash** para a automação e **Python** para o processamento de dados e cálculos estatísticos.

---

### 🎯 Objetivo

Criar uma solução que:
1. Gere um arquivo de log simulado.
2. Use um *script* **Bash** para orquestrar a geração e processamento inicial dos dados.
3. Use um *script* **Python** para realizar uma análise de dados mais profunda e produzir um relatório.

### 📜 Estrutura do Arquivo de Log Simulado

O *script* de geração (pode ser em Bash ou Python, mas a chamada deve ser do Bash) deve criar um arquivo chamado `access_log.txt` com **1000 linhas**. Cada linha deve simular um acesso e conter os seguintes campos, separados por um caractere de espaço:

| Campo | Tipo de Dado | Intervalo/Exemplo |
| :--- | :--- | :--- |
| **Timestamp (Unix)** | Número Inteiro | Exemplo: `1678886400` (um valor aleatório recente) |
| **User ID** | String | Exemplo: `user_001` até `user_100` (deve ter 100 usuários únicos) |
| **Status Code** | Número Inteiro | Valores possíveis: `200`, `404`, `500` |
| **Tempo de Resposta (ms)** | Número Inteiro | Um valor aleatório entre `50` e `5000` |

---

### 🛠️ Tarefas a Desenvolver

#### 1. Orquestrador Bash (`orchestrator.sh`)

Crie um *script* Bash que será o ponto de entrada do sistema. Ele deve realizar as seguintes ações na ordem:

* **Gerar Log:** Se o arquivo `access_log.txt` não existir, gere as 1000 linhas conforme a estrutura descrita acima.
* **Pré-processamento:** Filtre o `access_log.txt` e crie um novo arquivo chamado `successful_accesses.txt` contendo **apenas** as linhas onde o `Status Code` é **200**.
* **Invocar Python:** Chame o *script* Python (descrito na Tarefa 2), passando o arquivo `successful_accesses.txt` como argumento de linha de comando.
* **Limpeza:** Após a execução do Python, exiba uma mensagem de conclusão.

#### 2. Analisador Python (`analyzer.py`)

Crie um *script* Python que receberá o caminho para `successful_accesses.txt` como um argumento. Este *script* deve realizar as seguintes análises e imprimir um relatório formatado:

* **Contagem Total:** O número total de acessos bem-sucedidos (linhas no arquivo de entrada).
* **Tempo de Resposta Médio:** Calcular o tempo de resposta médio (em ms) de **todos** os acessos bem-sucedidos.
* **Usuários Únicos:** Contar e listar o número de **usuários únicos** presentes no arquivo.
* **Usuário Mais Ativo:** Identificar o `User ID` que realizou o maior número de acessos bem-sucedidos e o total de acessos desse usuário.

### 🚀 Entrega Esperada

Você deve entregar (ou ter na sua estrutura de projeto) os seguintes arquivos:
1.  `orchestrator.sh`
2.  `analyzer.py`

Ao executar `./orchestrator.sh`, o resultado final deve ser a impressão do relatório gerado pelo `analyzer.py` no console.