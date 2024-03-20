import json
import pandas as pd
from colorama import Fore, Style


# Carregar dados do arquivo JSON
def load_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


# Classe para representar um produto eletrônico.
class Product:
    def __init__(self, nome, preco, nota, fornecedor):
        self.nome = nome
        self.preco = preco
        self.nota = nota
        self.fornecedor = fornecedor


# Classe para o sistema de recomendação
class RecommendationSystem:
    def __init__(self, data):
        self.products = self.process_data(data)

    # Processar os dados do JSON
    def process_data(self, data):
        products = []
        for item in data:
            product = Product(item['nome'], item['preco'], item['nota'], item['fornecedor'])
            products.append(product)
        return products

    # Exibir lista de produtos disponíveis para o usuário
    def display_products(self):
        unique_products = list(set([product.nome for product in self.products]))
        print("Escolha um produto:")
        for i, product_name in enumerate(unique_products, start=1):
            print(f"{i}. {product_name}")

    # Calcular recomendação com base no menor preço
    def recommend_lowest_price(self, product_name):
        filtered_products = [product for product in self.products if product.nome == product_name]
        recommended_product = min(filtered_products, key=lambda x: x.preco)
        return recommended_product

    # Calcular recomendação com base na avaliação mais alta
    def recommend_highest_rating(self, product_name):
        filtered_products = [product for product in self.products if product.nome == product_name]
        recommended_product = max(filtered_products, key=lambda x: x.nota)
        return recommended_product


# Função para formatar a saída do produto recomendado
def format_recommendation(product):
    return f"{Fore.GREEN}{product.nome}{Style.RESET_ALL} - Preço: {Fore.BLUE}{product.preco}{Style.RESET_ALL}, Nota: {Fore.YELLOW}{product.nota}{Style.RESET_ALL}, Fornecedor: {Fore.CYAN}{product.fornecedor}{Style.RESET_ALL}"


# Função principal
def main():
    file_path = "myDataSet.json"
    data = load_data(file_path)
    recommendation_system = RecommendationSystem(data)

    while True:
        recommendation_system.display_products()

        try:
            choice = int(
                input("\nDigite o número correspondente ao produto para ver a recomendação (ou 0 para sair): "))
            if choice == 0:
                print("Obrigado por usar o sistema de recomendação!")
                break
            elif choice < 0 or choice > len(set([product.nome for product in recommendation_system.products])):
                print("Por favor, digite um número válido.")
                continue
            else:
                product_name = list(set([product.nome for product in recommendation_system.products]))[choice - 1]
                recommended_lowest_price = recommendation_system.recommend_lowest_price(product_name)
                recommended_highest_rating = recommendation_system.recommend_highest_rating(product_name)

                print("\nRecomendação baseada no menor preço:")
                print(format_recommendation(recommended_lowest_price))

                print("\nRecomendação baseada na avaliação mais alta:")
                print(format_recommendation(recommended_highest_rating))

        except ValueError:
            print("Por favor, digite um número válido.")


if __name__ == "__main__":
    main()
