import requests

def main():

    print('###############################')
    print('---Bem vindo ao CONSULTA CEP---')
    print('###############################')

    # usuário digita o CEP para consulta
    cep = input('Digite o CEP desejado, sem pontos ou traços: ')

    # enquanto o CEP fornecido não apresentar 8 digitos, aparecerá a mensagem de erro seguida de uma nova solicitação de CEP
    while len(cep) != 8:
        print('Por favor, digite um CEP com 8 dígitos')
        cep = input('Digite o CEP desejado, sem pontos ou traços: ')

    # caso o CEP informado contenha 8 digitos, será feita uma requisão HTTP a webservice
    requisicao = requests.get('https://viacep.com.br/ws/{}/json/' .format(cep))

    # Os dados do CEP (caso seja válido) retornarão no formato json e serão atribuídos a variável dados_endereco  
    dados_endereco = requisicao.json()

    # caso o CEP seja encontrado, serão exibidos os dados referentes a ele
    if 'erro' not in dados_endereco:
        print('---- CEP encontrado! ----')

        print('CEP: {}' .format(dados_endereco['cep']))
        print('LOGRADOURO: {}' .format(dados_endereco['logradouro']))
        print('COMPLEMENTO: {}' .format(dados_endereco['complemento']))
        print('BAIRRO: {}'.format(dados_endereco['bairro']))
        print('CIDADE: {}'.format(dados_endereco['localidade']))
        print('ESTADO: {}'.format(dados_endereco['uf']))

    # caso o CEP não seja válido, será exibida uma mensagem mde erro
    else:
        print('CEP inválido.\n')


    opcao = int(input('Deseja realizar nova consulta? Digite 1 para CONTINUAR e 2 para SAIR.'))

    # caso o usuário opte por continuar a consulta, a função será executada novamente
    if opcao == 1:
        main()

    else:
        print('------------------------------------------')
        print('O sistema está sendo finalizado. Obrigada!')

# caso a função solicitada tenha o nome main, será executada
if __name__ == '__main__':
    main()


