from funcoes import *

def test_verificar_carbono_false():
    result = verificar_conteudo_carbono(10)
    assert not result

def test_verificar_carbono_true():
    result = verificar_conteudo_carbono(5)
    assert result

def test_verificar_dureza_false():
    result = verificar_dureza_rockwell(40)
    assert not result

def test_verificar_dureza_true():
    result = verificar_dureza_rockwell(60)
    assert result


def test_verificar_resistencia_false():
    result = verificar_resistencia_tracao(60000)
    assert not result

def test_verificar_resistencia_true():
    result = verificar_resistencia_tracao(90000)
    assert  result



def test_calcular_grau_aco_10(mocker):
    mock_validar_conteudo_carbono = mocker.patch("funcoes.verificar_conteudo_carbono")
    mock_validar_conteudo_carbono.return_value = True

    mock_verificar_dureza_rockwell = mocker.patch("funcoes.verificar_dureza_rockwell")
    mock_verificar_dureza_rockwell.return_value = True

    mock_verificar_resistencia_tracao = mocker.patch("funcoes.verificar_resistencia_tracao")
    mock_verificar_resistencia_tracao.return_value = True

    grau_aco = calcular_grau_aco(5 , 75, 85000)
    assert grau_aco == 10




