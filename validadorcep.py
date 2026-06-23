import requests

def buscar_por_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        resposta = requests.get(url, timeout=5)
        dados = resposta.json()
        return None if "erro" in dados else dados
    except requests.exceptions.RequestException:
        print("Erro de conexão. Verifique sua internet.")
        return None

def buscar_por_endereco(uf, cidade, logradouro):
    url = f"https://viacep.com.br/ws/{uf}/{cidade}/{logradouro}/json/"
    try:
        resposta = requests.get(url, timeout=5)
        dados = resposta.json()
        return dados if isinstance(dados, list) and len(dados) > 0 else None
    except requests.exceptions.RequestException:
        print("Erro de conexão. Verifique sua internet.")
        return None

def exibir_endereco(dados):
    print("\nCEP encontrado!\n")
    print(f"CEP:     {dados.get('cep', '-')}")
    print(f"Rua:     {dados.get('logradouro', '-')}")
    print(f"Bairro:  {dados.get('bairro', '-')}")
    print(f"Cidade:  {dados.get('localidade', '-')}")
    print(f"Estado:  {dados.get('uf', '-')}")

def cep_termina_em_000(cep):
    cep_limpo = cep.replace("-", "").strip()
    return cep_limpo.endswith("000") and len(cep_limpo) == 8

while True:
    cep = input("\nDigite o CEP (ou 'sair' para encerrar): ").strip()

    if cep.lower() == "sair":
        print("Programa encerrado!")
        break

    cep_limpo = cep.replace("-", "").strip()

    if len(cep_limpo) != 8 or not cep_limpo.isdigit():
        print("CEP inválido. Digite 8 números.")
        continue

    dados = buscar_por_cep(cep_limpo)

    if dados:
        exibir_endereco(dados)
        continue

    if cep_termina_em_000(cep_limpo):
        print(f"\nCEP '{cep_limpo}' não encontrado no ViaCEP (possível CEP geral de localidade).")
        print("Vamos tentar localizar pelo endereço.\n")

        uf       = input("Digite a UF (ex: SP): ").strip().upper()
        cidade   = input("Digite a cidade (ex: Sao Paulo): ").strip()
        logradouro = input("Digite o logradouro (ex: Avenida Paulista): ").strip()

        resultados = buscar_por_endereco(uf, cidade, logradouro)

        if resultados:
            if len(resultados) == 1:
                print("\nEndereço localizado:")
                exibir_endereco(resultados[0])
            else:
                print(f"\n{len(resultados)} resultado(s) encontrado(s):\n")
                for i, r in enumerate(resultados, 1):
                    print(f"  [{i}] CEP: {r.get('cep')} — {r.get('logradouro')}, "
                          f"{r.get('bairro')}, {r.get('localidade')}/{r.get('uf')}")
        else:
            print("Endereço não encontrado. Verifique os dados e tente novamente.")
    else:
        print("CEP inválido ou não encontrado.")