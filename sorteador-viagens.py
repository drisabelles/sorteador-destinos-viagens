import random

lista_nacional = ["Acre", "Alagoas", "Amapá", "Amazonas", "Bahia", "Ceará", "Distrito Federal", "Espírito Santo", "Goiás", "Maraanhão", "Mato Grosso", "Mato Grosso do Sul", "Minas Gerais", "Pará", "Paraíba", "Paraná", "Pernambuco", "Piauí", "Rio de Janeiro", "Rio Grande do Norte", "Rio Grande do Sul", "Rondônia", "Roraima", "Santa Catarina", "São Paulo", "Sergipe", "Tocantins"]

lista_internacional_1 = ["Estados Unidos", "Canadá", "México", "Argentina", "Colômbia", "Peru", "Costa Rica", "Chile", "Cuba", "Venezuela", "Porto Rico", "Equador", "República Dominicana", "Bolívia", "Panamá", "Honduras", "El Salvador", "Guatemala", "Nicarágua", "Uruguai", "Belize", "Haiti", "Paraguai", "Jamaica", "Guiana", "Suriname", "Guiana Francesa", "Bahamas", "Curaçao", "Barbados", "Aruba", "Ilhas Turcas e Caicos", "Granada", "Ilhas Virgens Americanas", "Paises Baixos Caribenhos", "Trindade e Tobago, Ilhas Geórgia do Sul e Sandwich do Sul", "Ilhas Cayman", "Anguilla", "Santa Lúcia", "Guadalupe", "Martinica", "Ilhas Malvinas, Dominica", "Ilhas Virgens Britânicas", "São Cristovão e Névis", "Sint Maarten", "Antígua e Barbuda", "São Vicente e Granadinas", "Montserrat"]

lista_internacional_2 = ["Ucrânia", "Alemanha", "França", "Itália", "Reino Unido", "Polônia", "PaísesBaixos", "Suíça", "Áustria", "Grécia", "Suécia", "Bielorrúsia", "Rússia", "Bélgica", "Finlândia","Dinamarca", "Moldávia", "Romênia", "Noruega", "Croacia", "Tchéquia", "Hungria", "Irlanda", "Sérvia","Malta", "Lituânia", "Luxemburgo", "Bulgária", "Islândia", "Estônia", "Chipre", "Albânia", "Eslovênia","Eslováquia", "Letônia", "Kosovo", "Macedônia", "Mônaco", "Montenegro", "Bósnia e Herzegovina","Liechtenstein", "Vaticano", "Andorra", "San Marino", "Svalbard e Jan Mayen", "Ilha de Man", "Gibraltar","Ilhas Faroé", "Åland", "Jersey"]

lista_internacional_3 = ["Japão", "ndonésia", "China", "Índia", "Tailândia", "Coréia do Sul", "Filipinas", "Vietnã", "Singapura", "Malásia", "Hong Kong", "Irã", "Paquistão", "Taiwan", "Israel", "Arábia Saudita", "Catar", "Afeganistão", "Mongólia", "Cambodja", "Myanmar", "Sri Lanka", "Maldivas", "Laos", "Bangladesh", "Nepal", "Uzbequistão", "Ilha Christmas", "Macau", "Armênia", "Coreia do Norte", "Brunei", "Síria", "Líbano", "Emirados Árabes Unidos", "Iêmen", "Iraque", "Timor Leste", "Quirguistão", "Omã", "Jordânia", "Palestina", "Butão", "Ilhas Cocos", "Tajiquistão", "Turcomenistão", "Bahein", "Território do Oceano Índico Britânico", "Kuwait"]

lista_internacional_4 = ["Egito", "África do Sul", "Nigéria", "Quênia", "Gana", "Senegal", "Marrocos", "República Democrática do Congo", "Mali", "Tanzânia", "Argélia", "Etiópia", "Camarões", "Uganda", "Costa do Marfim", "Madagascar", "Sudão", "Somália", "Tunísia", "Zimbábue", "Angola", "Níger", "Burkina Faso", "Zâmbia", "República Centro-Africana", "Namíbia", "Moçambique", "Libéria", "Guiné", "Gabão", "Ruanda", "Malawi", "Serra" "Leoa", "Cabo Verde", "Líbia", "Ilhas Maurício", "Botsuana", "Gâmbia", "Togo", "Chade", "Benin", "Eritreia", "Guiné Equatorial", "Comores", "Saara Ocidental", "Djibouti", "Mauritânia", "Suazilândia", "Seychelles", "Burundi", "Sudão do Sul", "Lesoto"]

lista_internacional_5 = ["Tonga", "Nova Zelândia", "Austrália", "Fiji", "Papua-Nova Guiné", "Estados Federados da Micronésia", "Samoa", "Palau", "Kiribati", "Ilhas Salomão", "Vanuatu", "Nauru", "Polinésia Francesa", "Nova Caledônia", "Tuvalu", "Guam", "Ilhas Marshall", "Ilhas Cook", "Samoa Americana", "Niue", "Ilhas Mariana do Norte", "Ilha Norfolk", "Wallis e Fortuna", "Ilhas Pitcairn"]

escolha = int(input('Digite o código da operação que deseja realizar: \n1 - Sortear destino\n2 - Excluir destinho já realizado'))

if escolha == 1:

    localidade = int(input('Digite o código da localidade da viagem que deseja sortear: \n1 - Nacional\n2 - Internacional\n'))

    if localidade == 1:
        sorteado = random.choice(lista_nacional)
        print('O estado sorteado foi: {}'.format(sorteado))

    else:
        continente = int(input('Digite o código do continente no qual deseja sortear: \n1 - América\n2 - Europa\n3 - Ásia\n4 - África\n5 - Oceania\n'))

        if continente == 1:
            sorteado = random.choice(lista_internacional_1)
            print('O país sorteado foi: {}'.format(sorteado))

        elif continente == 2:
            sorteado = random.choice(lista_internacional_2)
            print('O país sorteado foi: {}'.format(sorteado))

        elif continente == 3:
            sorteado = random.choice(lista_internacional_3)
            print('O país sorteado foi: {}'.format(sorteado))

        elif continente == 4:
            sorteado = random.choice(lista_internacional_4)
            print('O país sorteado foi: {}'.format(sorteado))

        else:
            sorteado = random.choice(lista_internacional_5)
            print('O país sorteado foi: {}'.format(sorteado))
            
else:

    escolha_exclusao = int(input('Digite o código da localidade do destino que deseja excluir: \n1 - Nacional\n2 - Internacional '))

    if escolha_exclusao == 1:
        destino = str(input('Digite o nome do destino que deseja excluir: '))
        lista_nacional.remove(destino)

    else:
        continente = int(input('Digite o código do continente no qual deseja excluir um destino: \n1 - América\n2 - Europa\n3 - Ásia\n4 - África\n5 - Oceania\n'))
        destino = str(input('Digite o nome do destino que deseja excluir: '))

        if continente == 1:
            lista_internacional_1.remove(destino)

        elif continente == 2:
            lista_internacional_2.remove(destino)

        elif continente == 3:
            lista_internacional_3.remove(destino)

        elif continente == 4:
            lista_internacional_4.remove(destino)

        else:
            lista_internacional_5.remove(destino)
