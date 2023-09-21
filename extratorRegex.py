import re

endereco = 'Rua albino kaminski 273, casa, Bairro Alto, Curitiba, PR, 82820-310'

padrao = re.compile('[0-9]{5}[-]?[0-9]{3}')

busca = padrao.search(endereco)

if (busca):
    cep = busca.group()
    print(cep)