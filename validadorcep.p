import requests

while True:

    cep = input("\nDigite o CEP (ou 'sair' para encerrar): ")

    if cep.lower() == "sair":
        print("Programa encerrado!")
        break

    url = f"https://viacep.com.br/ws/{cep}/json/"

    resposta = requests.get(url)

    dados = resposta.json()

    if "erro" in dados:
        print("CEP inválido")
    else:
        print("\nCEP encontrado!\n")

        print("Rua:", dados["logradouro"])
        print("Bairro:", dados["bairro"])
        print("Cidade:", dados["localidade"])
        print("Estado:", dados["uf"])