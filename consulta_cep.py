import requests

def main():

    print('##################')
    print('---Consulta CEP---')
    print('##################')

    cep = input('Digite o CEP desejado: ')

    if len(cep) != 8:
        print('Digite um CEP válido!')
        exit()

    request = requests.get('https://viacep.com.br/ws/{}/json/' .format(cep))

    dados_endereco = request.json()

    if 'erro' not in dados_endereco:
        print('---- CEP encontrado! ----')

        print('CEP: {}' .format(dados_endereco['cep']))
        print('LOGRADOURO: {}' .format(dados_endereco['logradouro']))
        print('COMPLEMENTO: {}' .format(dados_endereco['complemento']))
        print('BAIRRO: {}'.format(dados_endereco['bairro']))
        print('CIDADE: {}'.format(dados_endereco['localidade']))
        print('ESTADO: {}'.format(dados_endereco['uf']))

    else:
        print('CEP inválido.\n')

        opcao = int(input('Deseja realizar nova consulta? Digite 1 para SIM e 2 para SAIR.'))

        if opcao == 1:
            main()

        else:
            print('Saindo do sistema!')

if __name__ == '__main__':
    main()


