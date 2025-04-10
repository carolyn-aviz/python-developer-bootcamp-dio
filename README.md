# 💻 DESAFIO

Fomos contratados por um **grande banco** para desenvolver seu novo sistema.  
Esse banco deseja **modernizar suas operações** e, para isso, escolheu a linguagem **Python** como base.

---

## 📌 Requisitos da Primeira Versão (v1)

O sistema deve permitir **três operações principais**:

- Depósito
- Saque
- Extrato

---

### 💰 Operação de Depósito

- Deve ser possível **depositar apenas valores positivos**.
- A versão inicial trabalhará com **apenas um cliente**, portanto **não é necessário número de agência ou conta**.
- Todos os depósitos devem ser:
  - **Armazenados em uma variável**
  - **Exibidos no extrato**
- O valor do depósito deve:
  - Ser **adicionado ao saldo atual**
  - Atualizar o extrato com a informação do depósito

---

### 🏧 Operação de Saque

O sistema deve seguir as seguintes regras para saques:

- Permitir até **3 saques diários**
- Cada saque com valor **máximo de R$ 500,00**
- Regras de validação:
  - Saque > R$ 500,00 → ❌ Informar: *"Valor maior que o permitido"*
  - Mais de 3 saques → ❌ Informar: *"Número máximo de saques atingido"*
  - Saldo insuficiente → ❌ Informar: *"Saldo insuficiente para saque"*
- Todos os saques devem ser:
  - **Armazenados em uma variável**
  - **Exibidos no extrato**

---

### 📄 Operação de Extrato

O extrato deve exibir:

- Todos os **depósitos**
- Todos os **saques**
- O **saldo atual**

#### 🧾 Formato esperado:

```text
Movimentações:
- Depósito: R$ 100,00
- Saque: R$ 50,00
Saldo atual: R$ 50,00
