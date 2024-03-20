from main import load_data, RecommendationSystem


# rode com  pytest .\MyTest\testes.py

# Teste para verificar se o arquivo JSON contém 15 objetos
def test_json_loading():
    data = load_data("myDataSet.json")
    assert len(data) == 15


# Teste para verificar se a lista de produtos está sendo processada corretamente
def test_products_loading():
    data = load_data("myDataSet.json")
    assert len(data) > 0
    assert all("nome" in item and "preco" in item and "nota" in item and "fornecedor" in item for item in data)
