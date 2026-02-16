"""
SISTEMA DE IA COMPLETO - 3 TÉCNICAS EM 1 ARQUIVO
Demonstra diferentes abordagens de Inteligência Artificial
"""

import random
import re
import math
from collections import Counter


# ============================================================================
# 1. CHATBOT COM REGRAS (IA Baseada em Regras)
# ============================================================================

class ChatbotSimples:
    """IA mais básica: usa regras pré-definidas para responder"""
    
    def __init__(self):
        self.padroes = {
            r'oi|olá|hey': [
                'Olá! Como posso ajudar?',
                'Oi! Tudo bem?',
                'Hey! Em que posso ser útil?'
            ],
            r'como você está|tudo bem': [
                'Estou bem, obrigado por perguntar!',
                'Funcionando perfeitamente!',
                'Muito bem! E você?'
            ],
            r'seu nome|quem é você': [
                'Sou um chatbot simples feito em Python!',
                'Me chamo Bot v1.0',
                'Sou apenas um programa de computador'
            ],
            r'tchau|adeus|até logo': [
                'Até logo!',
                'Tchau! Foi um prazer conversar!',
                'Adeus! Volte sempre!'
            ]
        }
        
        self.resposta_padrao = [
            'Interessante! Pode me contar mais?',
            'Hmm, não entendi bem. Pode reformular?',
            'Desculpe, ainda estou aprendendo sobre isso.'
        ]
    
    def responder(self, mensagem):
        mensagem = mensagem.lower()
        for padrao, respostas in self.padroes.items():
            if re.search(padrao, mensagem):
                return random.choice(respostas)
        return random.choice(self.resposta_padrao)


# ============================================================================
# 2. CLASSIFICADOR ML (Machine Learning - Naive Bayes)
# ============================================================================

class ClassificadorTextoIA:
    """IA que aprende com exemplos para classificar textos"""
    
    def __init__(self):
        self.categorias = {}
        self.vocabulario = set()
        self.total_docs = 0
        self.contagem_cats = Counter()
    
    def treinar(self, textos, categorias):
        """Treina a IA com exemplos"""
        for texto, categoria in zip(textos, categorias):
            palavras = texto.lower().split()
            
            if categoria not in self.categorias:
                self.categorias[categoria] = []
            
            self.categorias[categoria].extend(palavras)
            self.vocabulario.update(palavras)
            self.contagem_cats[categoria] += 1
            self.total_docs += 1
        
        print(f"✓ Classificador treinado: {self.total_docs} exemplos, {len(self.vocabulario)} palavras")
    
    def calcular_probabilidade(self, palavra, categoria):
        palavras_cat = self.categorias[categoria]
        contagem = palavras_cat.count(palavra)
        total = len(palavras_cat)
        return (contagem + 1) / (total + len(self.vocabulario))
    
    def prever(self, texto):
        """Prevê a categoria de um novo texto"""
        palavras = texto.lower().split()
        scores = {}
        
        for categoria in self.categorias:
            prob_cat = self.contagem_cats[categoria] / self.total_docs
            score = math.log(prob_cat)
            
            for palavra in palavras:
                if palavra in self.vocabulario:
                    prob_palavra = self.calcular_probabilidade(palavra, categoria)
                    score += math.log(prob_palavra)
            
            scores[categoria] = score
        
        categoria_prevista = max(scores, key=scores.get)
        max_score = max(scores.values())
        confianca = math.exp(scores[categoria_prevista] - max_score)
        
        return categoria_prevista, confianca


# ============================================================================
# 3. REDE NEURAL (Deep Learning)
# ============================================================================

class RedeNeural:
    """Rede Neural que aprende padrões complexos"""
    
    def __init__(self, entradas, ocultos, saidas):
        self.entradas = entradas
        self.ocultos = ocultos
        self.saidas = saidas
        
        # Inicializa pesos aleatórios
        self.pesos_entrada = [[random.uniform(-1, 1) for _ in range(ocultos)] 
                              for _ in range(entradas)]
        self.pesos_saida = [[random.uniform(-1, 1) for _ in range(saidas)] 
                            for _ in range(ocultos)]
        
        self.bias_oculto = [random.uniform(-1, 1) for _ in range(ocultos)]
        self.bias_saida = [random.uniform(-1, 1) for _ in range(saidas)]
    
    def sigmoide(self, x):
        return 1 / (1 + math.exp(-x))
    
    def derivada_sigmoide(self, x):
        return x * (1 - x)
    
    def feedforward(self, entrada):
        """Propaga entrada pela rede"""
        # Camada oculta
        self.oculto = []
        for j in range(self.ocultos):
            soma = self.bias_oculto[j]
            for i in range(self.entradas):
                soma += entrada[i] * self.pesos_entrada[i][j]
            self.oculto.append(self.sigmoide(soma))
        
        # Camada de saída
        saida = []
        for k in range(self.saidas):
            soma = self.bias_saida[k]
            for j in range(self.ocultos):
                soma += self.oculto[j] * self.pesos_saida[j][k]
            saida.append(self.sigmoide(soma))
        
        return saida
    
    def treinar(self, dados_treino, epocas=1000, taxa_aprendizado=0.5, mostrar_progresso=True):
        """Treina a rede neural com backpropagation"""
        if mostrar_progresso:
            print(f"Treinando rede neural por {epocas} épocas...")
        
        for epoca in range(epocas):
            erro_total = 0
            
            for entrada, saida_esperada in dados_treino:
                saida_obtida = self.feedforward(entrada)
                
                # Calcula erro
                erro_saida = []
                for k in range(self.saidas):
                    erro = saida_esperada[k] - saida_obtida[k]
                    erro_saida.append(erro)
                    erro_total += erro ** 2
                
                # Backpropagation
                delta_saida = [erro_saida[k] * self.derivada_sigmoide(saida_obtida[k]) 
                              for k in range(self.saidas)]
                
                delta_oculto = []
                for j in range(self.ocultos):
                    erro = sum(delta_saida[k] * self.pesos_saida[j][k] 
                              for k in range(self.saidas))
                    delta_oculto.append(erro * self.derivada_sigmoide(self.oculto[j]))
                
                # Atualiza pesos
                for j in range(self.ocultos):
                    for k in range(self.saidas):
                        self.pesos_saida[j][k] += taxa_aprendizado * delta_saida[k] * self.oculto[j]
                
                for i in range(self.entradas):
                    for j in range(self.ocultos):
                        self.pesos_entrada[i][j] += taxa_aprendizado * delta_oculto[j] * entrada[i]
                
                for k in range(self.saidas):
                    self.bias_saida[k] += taxa_aprendizado * delta_saida[k]
                for j in range(self.ocultos):
                    self.bias_oculto[j] += taxa_aprendizado * delta_oculto[j]
            
            if mostrar_progresso and (epoca + 1) % 500 == 0:
                print(f"  Época {epoca + 1}/{epocas} - Erro: {erro_total:.6f}")
        
        if mostrar_progresso:
            print("✓ Rede neural treinada!")
    
    def prever(self, entrada):
        return self.feedforward(entrada)


# ============================================================================
# SISTEMA PRINCIPAL - MENU INTERATIVO
# ============================================================================

def demo_chatbot():
    """Demonstração do Chatbot com Regras"""
    print("\n" + "="*60)
    print("DEMO 1: CHATBOT COM REGRAS")
    print("="*60)
    print("Este chatbot usa regras pré-programadas para responder.")
    print("Digite 'sair' para voltar ao menu.\n")
    
    bot = ChatbotSimples()
    
    while True:
        usuario = input("Você: ")
        if usuario.lower() in ['sair', 'voltar']:
            break
        resposta = bot.responder(usuario)
        print(f"Bot: {resposta}\n")


def demo_classificador():
    """Demonstração do Classificador ML"""
    print("\n" + "="*60)
    print("DEMO 2: CLASSIFICADOR DE TEXTO (MACHINE LEARNING)")
    print("="*60)
    print("Esta IA aprende a classificar textos em categorias.\n")
    
    ia = ClassificadorTextoIA()
    
    # Dados de treinamento
    textos_treino = [
        "adorei o filme foi incrível",
        "que filme maravilhoso amei",
        "excelente filme recomendo",
        "filme horrível muito ruim",
        "que filme terrível péssimo",
        "não gostei filme ruim",
        "python é uma linguagem de programação",
        "código em python é simples",
        "programar em python é legal",
        "futebol é um esporte popular",
        "jogador marcou gol no jogo",
        "time venceu a partida"
    ]
    
    categorias_treino = [
        "positivo", "positivo", "positivo",
        "negativo", "negativo", "negativo",
        "tecnologia", "tecnologia", "tecnologia",
        "esporte", "esporte", "esporte"
    ]
    
    print("Treinando o classificador...")
    ia.treinar(textos_treino, categorias_treino)
    
    print("\nTestando com novos textos:")
    print("-" * 60)
    
    testes = [
        "adorei programar em python",
        "que jogo maravilhoso",
        "filme péssimo não recomendo",
        "código simples e incrível"
    ]
    
    for teste in testes:
        categoria, confianca = ia.prever(teste)
        print(f"\nTexto: '{teste}'")
        print(f"→ Categoria: {categoria} (confiança: {confianca:.1%})")
    
    print("\n" + "-" * 60)
    input("\nPressione Enter para voltar ao menu...")


def demo_rede_neural():
    """Demonstração da Rede Neural"""
    print("\n" + "="*60)
    print("DEMO 3: REDE NEURAL (DEEP LEARNING)")
    print("="*60)
    print("Esta rede neural aprende a função lógica XOR do zero!\n")
    
    print("XOR (Ou Exclusivo):")
    print("  0 XOR 0 = 0")
    print("  0 XOR 1 = 1")
    print("  1 XOR 0 = 1")
    print("  1 XOR 1 = 0\n")
    
    # Criar rede
    rede = RedeNeural(entradas=2, ocultos=3, saidas=1)
    
    # Dados de treinamento
    dados_treino = [
        ([0, 0], [0]),
        ([0, 1], [1]),
        ([1, 0], [1]),
        ([1, 1], [0])
    ]
    
    # Treinar
    rede.treinar(dados_treino, epocas=2000, taxa_aprendizado=0.5)
    
    # Testar
    print("\nResultados após treinamento:")
    print("-" * 60)
    for entrada, esperado in dados_treino:
        resultado = rede.prever(entrada)
        acerto = "✓" if abs(resultado[0] - esperado[0]) < 0.1 else "✗"
        print(f"{acerto} Entrada: {entrada} → Esperado: {esperado[0]} | Obtido: {resultado[0]:.4f}")
    
    print("-" * 60)
    input("\nPressione Enter para voltar ao menu...")


def menu_principal():
    """Menu principal do sistema"""
    
    print("\n" + "="*60)
    print(" SISTEMA DE IA COMPLETO - 3 TÉCNICAS DE INTELIGÊNCIA ARTIFICIAL")
    print("="*60)
    
    while True:
        print("\nEscolha uma demonstração:")
        print("\n1. Chatbot com Regras (IA Baseada em Regras)")
        print("   → Usa padrões pré-definidos para conversar")
        print("\n2. Classificador de Texto (Machine Learning)")
        print("   → Aprende a categorizar textos com exemplos")
        print("\n3. Rede Neural (Deep Learning)")
        print("   → Aprende funções complexas do zero")
        print("\n0. Sair")
        print("-" * 60)
        
        escolha = input("\nSua escolha: ").strip()
        
        if escolha == "1":
            demo_chatbot()
        elif escolha == "2":
            demo_classificador()
        elif escolha == "3":
            demo_rede_neural()
        elif escolha == "0":
            print("\nAté logo! 👋")
            break
        else:
            print("\n❌ Opção inválida! Tente novamente.")


# ============================================================================
# EXECUTAR O PROGRAMA
# ============================================================================

if __name__ == "__main__":
    menu_principal()