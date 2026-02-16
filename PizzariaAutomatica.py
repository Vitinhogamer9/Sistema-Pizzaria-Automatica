##Pizzaria Automática
##Como vai ser? 
#Esta pizzaria não precisa de input, funciona sem interação.

import random
import time

Dia = 1
MinCliente = 10
MaxCliente = 25

NomesClientes = {
    "Miguel", "Arthur", "Helena", "Alice", "Heitor",
    "Laura", "Theo", "MariaAlice", "Davi", "Gabriel",
    "Gael", "Bernardo", "Valentina", "Heloísa", "Samuel", "Felipe",
    "Guilherme", "Francisca", "Eduardo", "Matheus", "Julia",
    "Bruno", "Marcelo", "Arthur", "Leonardo", "Bob"
}

Cardapio = {
    "Comidas" : {
        "Pizza Normal": 25.00,
        "Pizza Calabresa": 30.00,
        "Pizza Mussarela": 28.35,
        "Pizza com Bacon": 32.50,
        "Pizza Mexicana": 29.99,
        "Pizza Portuguesa": 29.99,
        "Pizza Frango com Catupiry": 31.50,
    },

    "Sobremesa" : {
        "Coca Cola": 5.50,
        "Guarana": 4.50,
        "Pepsi": 4.75,
        "Agua": 1.50,
        "Guaravita": 3.25,
        "Fanta": 4.25,
        "Sprite": 4.00,
        "Açai": 8.00
    }
}

Cozinheiros = {
    "Cozinheiro 1": {
        "Nome": "João",
        "Habilidade": 0.8
    },
    "Cozinheiro 2": {
        "Nome": "Maria",
        "Habilidade": 0.9
    },
    "Cozinheiro 3": {
        "Nome": "Carlos",
        "Habilidade": 0.7
    },
    "Cozinheiro 4": {
        "Nome": "Ana",
        "Habilidade": 0.85
    },
    "Cozinheiro 5": {
        "Nome": "Pedro",
        "Habilidade": 0.75
    }
}

garcons = {
    "Garçom 1": {
        "Nome": "Lucas",
        "Habilidade": 0.8
    },
    "Garçom 2": {
        "Nome": "Sofia",
        "Habilidade": 0.9
    },
    "Garçom 3": {
        "Nome": "Rafael",
        "Habilidade": 0.7
    },
    "Garçom 4": {
        "Nome": "Isabela",
        "Habilidade": 0.85
    },
    "Garçom 5": {
        "Nome": "Gustavo",
        "Habilidade": 0.75
    }
}

Atendentes = {
    "Atendente 1": {
        "Nome": "Fernanda",
        "Habilidade": 0.8
    },
    "Atendente 2": {
        "Nome": "Bruno",
        "Habilidade": 0.9
    }
}


## Configurações dos clientes
TiposClientes = {
    "Normal": {
        "PalavrasInicioCliente": [
            "Oi, tem {} e {}?",
            "Bom dia, gostaria de pedir {} e {}.",
            "Eae meu chapa, tem {} e {}?",
            "Olá, eu gostaria de pedir {} e {} por favor.",
            "Oi, tem {} e {} no cardápio?"
        ],  
        "PalavrasMalEntendimento": [
            "Que? Está confundindo, eu pedi {} e {}!",
            "Não, eu pedi {} e {}!",
            "Qual foi, tá surdo? Eu pedi {} e {}!",
            "Ei, eu pedi {} e {}, não isso aí"
        ],
        "PalavrasAgradecidas": [
            "Obrigado",
            "Muito obrigado, tenha um otimo dia!",
            "Valeu, até a próxima!",
            "Agradeço, até mais!"
        ],
        "Pensamento": [
            "Hmmm... Se não tem isso, o que eu vou comer?",
            "Poxa, queria muito isso, mas tudo bem.",
            "Ah, que pena, mas vou escolher outra coisa.",
            "Hmm, não tem isso, mas vou escolher outra coisa."
        ],
        "Pergunta": [
            "Vocês tem {} e {}?",
            "Tem como pedir {} e {}?",
            "Eu queria pedir {} e {}, tem como?",
            "Eu queria pedir {} e {}, tem como pedir?"
        ]
    },
    "Arrogante": {
        "PalavrasInicioCliente": [
            "Bora, Bora, quero meu pedido logo! {} e {}! Pra Hoje!",
            "Rapido, quero meu pedido! {} e {}! Já!",
            "Não me faça esperar, quero {} e {}! Já!",
            "Eu quero meu pedido agora! {} e {}! Não tenho tempo a perder!",
            "Vamos lá, quero meu pedido! {} e {}! Já!"
        ],  
        "PalavrasMalEntendimento": [
            "Você é surdo? Eu pedi {} e {}!",
            "Não, eu pedi {} e {}!",
            "Eu FALEI que pedi {} e {}!",
            "EU DISSE que pedi {} e {}, não isso aí!"
        ],
        "PalavrasAgradecidas": [
            "Só perdi tempo aqui, não volto mais.",
            "Ta, também não é tão ruim, mas não volto mais.",
            "Ah, até que não é tão ruim, mas não volto mais.",
            "Hmmm, não é tão ruim, mas não volto mais."
        ],
        "Pensamento" : [
            "Como assim não tem isso? Vocês são incompetentes!",
            "Isso é um absurdo, como vocês não tem isso?!",
            "Vocês estão de brincadeira, como não tem isso?!",
            "Isso é ridículo, como vocês não tem isso?!",
            "Pizzaria ruim também, tem nada no cardápio, que porcaria!"
        ],
        "Pergunta": [
            "Vocês tem {} e {}? Tem que ter!",
            "Tem como pedir {} e {}? Tem que ter!",
            "Eu queria pedir {} e {}, tem como? Tem que ter!",
            "Eu queria pedir {} e {}, tem como pedir? Tem que ter!"
        ]
    },
    "Atendente" : {
        "PalavraInicioEspecial" : [
            "Olá, bom dia oque gostaria de pedir?",
            "Oi, seja bem vindo, oque deseja pedir?",
            "Eae, oque vai querer hoje?",
            "Oi, seja bem vindo, oque deseja pedir hoje?",
            "Olá, vai querer oque?"
        ],
        "PalavraRejeitação" : [
            "Desculpe, mas não temos isso no cardápio.",
            "Infelizmente, não oferecemos esse item.",
            "Lamento, mas não temos essa opção disponível.",
            "Desculpe, mas esse item não está em nosso cardápio."
        ],
        "PalavraConfirmação" : [
            "Sim, seu pedido de {} e {} foi confirmado! Obrigado por escolher nossa pizzaria!",
            "Seu pedido de {} e {} foi confirmado! Agradecemos por escolher nossa pizzaria!",
            "Pedido de {} e {} confirmado! Obrigado por escolher nossa pizzaria!",
            "Sim tem {} e {}! Seu pedido foi confirmado! Obrigado por escolher nossa pizzaria!",
        ]
    }
}

##Iniciar o Ciclo de Atendimento
while True:
    print(f"\n{'='*30}")
    print(f"Dia {Dia}")
    print(f"\n{'='*30}")

    ClientesDoDia = random.randint(MinCliente, MaxCliente)
    Selecionados = random.sample(list(NomesClientes), ClientesDoDia)
    Clientes = {f"Cliente{i+1}": nome for i, nome in enumerate(Selecionados)}

    AtendenteSelecionado = random.sample(list(Atendentes.keys()), 2)[0]
    Atendente = {AtendenteSelecionado: Atendentes[AtendenteSelecionado]["Nome"]}


    SalarioTotal = 0

    for cliente, nome in Clientes.items():
        ClienteTipo = random.choices(
            ["Normal", "Arrogante"], weights=[70, 30])[0]
        
        P1 = random.choice(list(Cardapio["Comidas"].keys()))
        P2 = random.choice(list(Cardapio["Sobremesa"].keys()))
        PrecoSombremesa = Cardapio["Sobremesa"][P2]
        PrecoComida = Cardapio["Comidas"][P1]
        SalarioTotal += PrecoSombremesa + PrecoComida
        ChanceDeNaoter = random.choices([True, False], weights=[90, 10])[0]##Tem, não tem

## O atendente pergunta o que o cliente deseja pedir 
        time.sleep(3)
        print(f"{cliente} ({nome}): -- Entrou na pizzaria --")
        time.sleep(1.5)
        print(f"{list(Atendente.values())[0]}: {random.choice(TiposClientes['Atendente']['PalavraInicioEspecial'])}")
        time.sleep(1.5)
        print(f"{cliente} ({nome}): {random.choice(TiposClientes[ClienteTipo]['PalavrasInicioCliente']).format(P1, P2)}")
        time.sleep(1.5)
        if ChanceDeNaoter == False:
            ##Sorteia outro item do cardápio
            OpcoesComida = [comida for comida in Cardapio["Comidas"].keys() if comida != P1]
            if OpcoesComida:
                P1 = random.choice(OpcoesComida)
                PrecoComida = Cardapio["Comidas"][P1]
            
            OpcoesSobremesa = [Sobremesa for Sobremesa in Cardapio["Sobremesa"].keys() if Sobremesa != P2]
            if OpcoesSobremesa:
                P2 = random.choice(OpcoesSobremesa)
                PrecoSobremesa = Cardapio["Sobremesa"][P2]
            
            #Atualiza o salario total com os novos preços
            SalarioTotal += PrecoComida + PrecoSobremesa

            print(f"{list(Atendente.values())[0]}: {random.choice(TiposClientes['Atendente']['PalavraRejeitação'])}")
            time.sleep(1.5)
            print(f"{cliente} ({nome}): {random.choice(TiposClientes[ClienteTipo]['Pensamento'])}")
            time.sleep(1.5)
            print(f"{cliente} ({nome}): {random.choice(TiposClientes[ClienteTipo]['Pergunta']).format(P1, P2)}")
            time.sleep(1.5)
            print(f"{list(Atendente.values())[0]}: {random.choice(TiposClientes['Atendente']['PalavraConfirmação']).format(P1, P2)}")
            time.sleep(1.5)
            print(f"{cliente} ({nome}): {random.choice(TiposClientes[ClienteTipo]['PalavrasAgradecidas'])}")
            print(f"Preço total: R${PrecoComida + PrecoSombremesa:.2f}")
            print("\n" + "="*50 + "\n")
        else:
            print(f"{list(Atendente.values())[0]}: {random.choice(TiposClientes['Atendente']['PalavraConfirmação']).format(P1, P2)}")
            time.sleep(1.5)
            print(f"{cliente} ({nome}): {random.choice(TiposClientes[ClienteTipo]['PalavrasAgradecidas'])}")
            print(f"Preço total: R${PrecoComida + PrecoSombremesa:.2f}")
            print("\n" + "="*50 + "\n")

    print(f"\n🎉 FIM DO DIA {Dia} 🎉")
    print(f"Total de clientes atendidos: {len(Clientes)}")
    print(f"Total Arrecadado hoje: R${SalarioTotal:.2f}\n")

    Dia += 1
