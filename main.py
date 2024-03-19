import json
import pandas as pd
from colorama import Fore, Style


# Classe que define o Sistema de Recomendação
class SistemaRecomendacao:
    def __init__(self, arquivo_json):
        # Carrega os dados do arquivo JSON usando a biblioteca Pandas
        self.dados = pd.read_json(arquivo_json)
        # Lista para armazenar as preferências do usuário
        self.preferencias_usuario = []

    # Método para calcular a média das recomendações
    def calcular_media_recomendacao(self):
        return self.dados['nota_filme'].mean()

    # Método para encontrar o comentário com a menor nota
    def menor_nota(self):
        menor_comentario = self.dados.loc[self.dados['nota_filme'].idxmin()]
        return menor_comentario['nome'], menor_comentario['nota_filme'], menor_comentario['critica']

    # Método para encontrar o comentário com a maior nota
    def maior_nota(self):
        maior_comentario = self.dados.loc[self.dados['nota_filme'].idxmax()]
        return maior_comentario['nome'], maior_comentario['nota_filme'], maior_comentario['critica']

    # Método para verificar se o filme foi bem avaliado (mais de 50% das avaliações são 4 ou mais)
    def filme_bem_avaliado(self):
        return (self.dados['nota_filme'] >= 4).sum() / len(self.dados) >= 0.5


# Função para exibir o menu de opções
def menu():
    print(Fore.GREEN + "===== Sistema de Recomendação =====" + Style.RESET_ALL)
    print("1. Calcular média da recomendação")
    print("2. Comentário com menor nota")
    print("3. Comentário com maior nota")
    print("4. Verificar se o filme foi bem avaliado")
    print("0. Sair")


# Função principal que controla o fluxo do programa
def main():
    # Instancia o sistema de recomendação, passando o nome do arquivo JSON como argumento
    sistema = SistemaRecomendacao("myDataSet.json")
    escolha = None

    # Loop principal do programa
    while escolha != '0':
        menu()  # Exibe o menu de opções
        escolha = input("Escolha uma opção: ")  # Solicita a escolha do usuário

        # Executa a ação correspondente à escolha do usuário
        if escolha == '1':
            print("Média da recomendação:", sistema.calcular_media_recomendacao())
        elif escolha == '2':
            nome, nota, critica = sistema.menor_nota()
            print("Comentário com menor nota:", nome, "- Nota:", nota, "- Critica:", critica)
        elif escolha == '3':
            nome, nota, critica = sistema.maior_nota()
            print("Comentário com maior nota:", nome, "- Nota:", nota, "- Critica:", critica)
        elif escolha == '4':
            if sistema.filme_bem_avaliado():
                print("O filme foi bem avaliado.")
            else:
                print("O filme não foi bem avaliado.")
        elif escolha == '0':
            print("Saindo...")
        else:
            print("Opção inválida. Tente novamente.")


# Função principal que inicia o programa
if __name__ == "__main__":
    main()
