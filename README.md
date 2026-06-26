# 📍 Validador de CEP em Python

Este projeto consiste em um **Validador de CEP** desenvolvido em **Python**, utilizando a API pública do **ViaCEP** para consultar informações de endereços brasileiros em tempo real.

O programa recebe um CEP informado pelo usuário, realiza uma requisição HTTP para a API e exibe informações como rua, bairro, cidade e estado. Caso o CEP informado seja inválido ou inexistente, o sistema informa o erro de forma simples e intuitiva.

<p align="center">
  <img src="https://img.shields.io/badge/linguagem-Python-blue?style=for-the-badge" alt="Linguagem Python">
  <img src="https://img.shields.io/badge/status-em desenvolvimento-orange?style=for-the-badge" alt="Status em desenvolvimento">
</p>

---

# 🐍 Conceitos Praticados

Durante o desenvolvimento deste projeto foram aplicados diversos conceitos importantes da linguagem Python:

- Consumo de APIs REST
- Requisições HTTP utilizando a biblioteca `requests`
- Manipulação de dados em formato JSON
- Estruturas Condicionais
- Entrada e saída de dados pelo terminal
- Validação de informações retornadas pela API
- Organização da lógica do programa

---

# 🚀 Funcionalidades

✅ Consulta de CEP em tempo real

✅ Integração com a API ViaCEP

✅ Exibição automática de:

- Rua
- Bairro
- Cidade
- Estado

✅ Validação de CEP inválido

✅ Interface simples executada no terminal

---

# 🖥️ Exemplo de Execução

```text
Digite o CEP: 01001000

CEP encontrado!

Rua: Praça da Sé
Bairro: Sé
Cidade: São Paulo
Estado: SP
```

### Exemplo para CEP inválido

```text
Digite o CEP: 99999999

CEP inválido
```

---

# ⚙️ Como Executar

### Instalar a biblioteca Requests

```bash
pip install requests
```

### Executar o programa

```bash
python validador_cep.py
```

---

# 🎓 Importância Acadêmica

Este projeto representa um importante passo no aprendizado de desenvolvimento com Python, permitindo compreender como aplicações podem consumir informações disponibilizadas por serviços externos através de APIs REST.

Além disso, reforça conceitos fundamentais como requisições HTTP, manipulação de dados em JSON e integração entre sistemas, competências amplamente utilizadas no desenvolvimento de software moderno.

---

# 🚀 Aprendizados

Durante este projeto foram desenvolvidas habilidades relacionadas a:

- Consumo de APIs
- Programação em Python
- Manipulação de JSON
- Requisições HTTP
- Tratamento de respostas
- Integração entre aplicações
- Organização e legibilidade de código

---

# 📂 Estrutura do Projeto

```text
Validador-de-Cep-em-Python/
│
├── validador_cep.py
├── README.md
└── requirements.txt
```

---

# 👩‍💻 Autora

**Karina Beilich**

GitHub: https://github.com/KarinaBeilich

---

> 🎯 Projeto desenvolvido para praticar integração com APIs REST, manipulação de dados em JSON e os fundamentos da programação em Python através da consulta de CEPs utilizando o serviço ViaCEP.
