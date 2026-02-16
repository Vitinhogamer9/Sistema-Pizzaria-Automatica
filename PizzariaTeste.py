import time
import random


Dia = 1

Cardapio = {
    "Pizza Normal": 25.00,
    "Pizza Calabresa": 30.00,
    "Pizza Mussarela": 28.35,
    "Pizza com Bacon": 32.50,
    "Pizza Portuguesa": 29.99
}

Sobremesa = {
    "Coca Cola": 5.50,
    "Guarana": 4.50,
    "Pepsi": 4.75,
    "Agua": 1.50,
    "Guaravita": 3.25
}
##Configurações dos clientes
NomesClientes = {
    "Miguel", "Arthur", "Helena", "Alice", "Heitor",
    "Laura", "Theo", "MariaAlice", "Davi", "Gabriel",
    "Gael", "Bernardo", "Valentina", "Heloísa", "Samuel", "Felipe",
    "Guilherme", "Francisca", "Eduardo", "Matheus", "Julia",
    "Bruno", "Marcelo", "Arthur", "Leonardo"

}

TiposClientes = {
    "Normal", "Arrogante", "Rico"
}

MinCliente = 5
MaxCliente = 15



FrasesClientes = {
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
            "Ei, eu pedi {} e {}, não isso aí!",
            "Mano, eu pedi {} e {}, presta atenção!"
],
        "PalavrasAgradecidas": [
            
           "Isso mesmo, obrigado, estou ansioso para comer",
           "É isso dai mesmo, valeu, mal posso esperar para comer",
           "Sim, agradeço, estou animado para comer",
           "Sim Sim, muito obrigado, estou ansioso para saborear",
           "Aham, obrigado, estou empolgado para comer"
]

    },
        "Arrogante": {
            "PalavrasInicioCliente": [
                "Bora, Bora, quero meu pedido logo! {} e {}! Pra Hoje",
                "Eu quero meu pedido agora! {} e {}! Não tenho tempo a perder",
                "Não me faça esperar, quero {} e {}! Já!",
                "Eu quero meu pedido imediatamente! {} e {}! Não me faça esperar",
                "Você está trabalhando para mim, quero {} e {}! Rápido!"
            ],
            "PalavrasMalEntendimento": [
                "O que? Você não entendeu? Eu pedi {} e {}! Presta atenção!",
                "Não, eu pedi {} e {}! Você tá de brincadeira?",
                "Qual é o problema? Eu pedi {} e {}! Fala sério!",
                "Ei, eu pedi {} e {}, não isso aí! Tá me irritando!",
                "Mano, eu pedi {} e {}, presta atenção! Não me faça repetir!",
                "VOCÊ NÃO ENTENDEU? EU PEDI {} E {}! PRESTA ATENÇÃO! VOCÊ TÁ ME IRRITANDO!"
            ],
            "PalavrasAgradecidas": [
            "Isso mesmo, obrigado, estou ansioso para comer",
            "É isso dai mesmo, valeu, mal posso esperar para comer",
            "Sim, agradeço, estou animado para comer",
            "Sim Sim, muito obrigado, estou ansioso para saborear",
            "Aham, obrigado, estou empolgado para comer"
            ]
        },
"Rico": {
                "PalavrasInicioCliente": [
                    "Bom dia meu caro, gostaria de pedir {} e {}. Espero um serviço de qualidade.",
                    "Olá, estou interessado em pedir {} e {}. Espero um atendimento excelente.",
                    "Oi, gostaria de pedir {} e {}. Espero um serviço impecável.",
                    "Eae, quero pedir {} e {}. Espero um atendimento de primeira.",
                    "Olá, me traga {} e {}. Espero um serviço de alta qualidade."
            ],
                "PalavrasMalEntendimento": [
                    "Não, não, não! Eu pedi {} e {}! Esperava mais atenção...",
                    "Amigo, eu pedi {} e {}! Vou ter que falar com o gerente?",
                    "Peraí, eu pedi {} e {}! Pelo preço que pago, esperava mais!",
                    "Isso não é o que pedi! Quero {} e {}, pelo amor de Deus!",
                    "Olha, eu pedi {} e {}. Vamos fazer direito, sim?"
            ],
                "PalavrasAgradecidas": [
                    "Ah, isso mesmo, obrigado, estou ansioso para comer",
                    "Perfeito! Aqui está sua gorjeta, meu amigo!",
                    "Excelente! Pode guardar o troco para você!",
                    "Maravilhoso! Toma essa gorjeta generosa aí!",
                    "Ótimo serviço! Vou deixar uma gratificação extra!",
                    "Isso sim! Muito obrigado, pegue uma gorjeta!"
            ]
        }
}
PalavraUsuario = [
    "Bom dia, oque quer pedir? ",
    "Olá, oque deseja pedir? ",
    "Oi, oque gostaria de pedir? ",
    "Eae, oque quer pedir? ",
    "Olá, oque desejas? "
]

PalavraPergunta = [
    "Você quer ",
    "Você deseja ",
    "Você tá pedindo "
]

# Loop infinito para múltiplos dias
while True:
    print(f"\n{'='*50}")
    print(f"🍕 Hoje é o dia {Dia} 🍕")
    print(f"{'='*50}\n")
    
    # Gerar novos clientes para o dia
    ClientesDoDia = random.randint(MinCliente, MaxCliente)
    Selecionados = random.sample(list(NomesClientes), ClientesDoDia)
    Clientes = {f"Cliente{i+1}": nome for i, nome in enumerate(Selecionados)}
    
    TotalJuntado = 0
    
    # Loop para cada cliente do dia
    for cliente, nome in Clientes.items():
        ClienteTipo = random.choices(
        ["Normal", "Arrogante", "Rico"], 
        weights=[60, 25, 15])[0]

        R1 = random.choice(list(Cardapio.keys()))
        R2 = random.choice(list(Sobremesa.keys()))
        precoComida = Cardapio[R1]
        precoBebida = Sobremesa[R2]
        TotalJuntado += precoComida + precoBebida
##falas 
        time.sleep(1)
        print(random.choice(PalavraUsuario))
        time.sleep(1)
        print(f"{cliente} ({nome}): " + random.choice(FrasesClientes[ClienteTipo]["PalavrasInicioCliente"]).format(R1, R2))
        time.sleep(1)
        
        Resposta = input(random.choice(PalavraPergunta) + "→ ")
        time.sleep(1)
        
        if Resposta.strip().lower() == f"{R1} e {R2}".lower():
            print(f"{cliente} ({nome}): " + random.choice(FrasesClientes[ClienteTipo]["PalavrasAgradecidas"]))
            print(f"Preço total: R${precoComida + precoBebida:.2f}")
            print(f"Bonus do Rico: R${precoComida * 2:.2f}" if ClienteTipo == "Rico" else "")
        else:
            print(f"{cliente} ({nome}): " + random.choice(FrasesClientes[ClienteTipo]["PalavrasMalEntendimento"]).format(R1, R2))
        ## Finalização do  dia
        time.sleep(2)
        print("\n" + "="*50 + "\n")
    
    # Resumo do dia
    print(f"\n🎉 FIM DO DIA {Dia} 🎉")
    print(f"Total de clientes atendidos: {len(Clientes)}")
    print(f"Total Arrecadado hoje: R${TotalJuntado:.2f}\n")
    
    # Perguntar se quer continuar
    continuar = input("Deseja continuar para o próximo dia? (s/n): ").strip().lower()
    if continuar != 's':
        print(f"\n✨ Obrigado por jogar! Você trabalhou {Dia} dia(s)! ✨")
        break
    
    Dia += 1  # Incrementa o dia