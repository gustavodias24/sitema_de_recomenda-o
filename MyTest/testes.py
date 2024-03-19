import pytest
from main import SistemaRecomendacao  # Importa a classe SistemaRecomendacao do arquivo main.py


# Fixture para criar uma instância do SistemaRecomendacao para os testes
@pytest.fixture
def sistema():
    return SistemaRecomendacao("../myDataSet.json")


# Teste parametrizado para a função filme_bem_avaliado
@pytest.mark.parametrize("notas, esperado", [
    ([5, 5, 4, 3], True),  # Teste com mais de 50% das avaliações com 4 ou mais estrelas
    ([3, 2, 1, 1], False)  # Teste com menos de 50% das avaliações com 4 ou mais estrelas
])
def test_filme_bem_avaliado(sistema, notas, esperado):
    # Modifica as avaliações do sistema para as notas fornecidas
    sistema.dados['nota_filme'] = notas
    # Verifica se o resultado da função é igual ao esperado
    assert sistema.filme_bem_avaliado() == esperado


# Teste para a função calcular_media_recomendacao
def test_calcular_media_recomendacao():
    # Cria uma instância do SistemaRecomendacao
    sistema = SistemaRecomendacao("../myDataSet.json")
    # Calcula a média das notas no conjunto de dados
    media_esperada = sum(sistema.dados['nota_filme']) / len(sistema.dados)
    # Verifica se o resultado da função é igual ao esperado
    assert sistema.calcular_media_recomendacao() == media_esperada


# Teste para verificar se o filme foi bem avaliado
def test_filme_bem_avaliado():
    # Cria uma instância do SistemaRecomendacao
    sistema = SistemaRecomendacao("../myDataSet.json")
    # Calcula a quantidade de avaliações bem avaliadas (notas >= 4)
    avaliacoes_bem_avaliadas = (sistema.dados['nota_filme'] >= 4).sum()
    # Verifica se a proporção de avaliações bem avaliadas é maior ou igual a 50%
    assert sistema.filme_bem_avaliado() == (avaliacoes_bem_avaliadas / len(sistema.dados) >= 0.5)
