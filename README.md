# 🗺️ Validador de CEP em Python

Este é um script desenvolvido em **Python** que automatiza a validação e a busca de endereços através do CEP. O objetivo principal do projeto foi integrar a aplicação com uma API pública externa para agilizar o processo de checagem de dados cadastrais, eliminando a necessidade de consultas manuais e repetitivas.

<p align="center">
  <img src="https://img.shields.io/badge/linguagem-Python-blue?style=for-the-badge" alt="Python">
  <img src="https://img.shields.io/badge/status-conclu%C3%ADdo-success?style=for-the-badge" alt="Status Concluído">
</p>

---

## 🚀 Conceitos e Tecnologias Aplicados

* **Biblioteca `requests`:** Utilizada para fazer a comunicação do código em Python com a internet.
* **Consumo de API Rest:** Integração com a API pública do **ViaCEP** para enviar o CEP digitado e receber de volta o endereço completo.
* **Manipulação de Dados JSON:** Tratamento dos dados retornados pela API (como logradouro, bairro, cidade e estado) para exibi-los de forma organizada.
* **Tratamento de Erros:** Lógica para identificar CEPs inválidos, inexistentes ou erros de digitação, garantindo a estabilidade do programa.

---

## 🎨 Funcionalidades

- **Consulta Instantânea:** O usuário digita o CEP e o script faz a busca em tempo real.
- **Retorno Estruturado:** Exibe na tela o endereço completo (Rua, Bairro, Cidade e UF) correspondente ao CEP informado.
- **Validação de Formato:** Sistema que verifica se o dado inserido possui a estrutura correta antes de realizar a requisição.

---

## 🛠️ Como visualizar e executar

1. Entre na pasta do repositório aqui no GitHub.
2. Clique no arquivo principal (com a extensão `.py`) para visualizar toda a lógica do script direto pelo seu navegador.
3. Para rodar na sua máquina, é necessário ter o Python instalado e a biblioteca `requests` (instalada via `pip install requests` no terminal).

---

## 🧠 Importância Prática e Profissional

A criação de scripts de validação e integração via API é uma das habilidades mais valorizadas para a **automação de rotinas corporativas**. Esse tipo de lógica serve como base para otimizar fluxos de trabalho, higienizar bases de dados em planilhas e garantir a integridade de relatórios operacionais e de faturamento.

---

## 👤 Autora

* **Karina Beilich** - https://github.com/KarinaBeilich
