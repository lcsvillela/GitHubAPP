from dados import Dados
import requests

def test__name():
    assert len(Dados("Python").get_informacao(1, "name")) > 1


def test_forks():
    assert len(Dados("Python").get_informacao(1, "description")) > 1


def test_pesquisar():
    assert Dados('Python').pesquisar() is not None

def test_get_informacao():
    assert Dados('Python').get_insformacao(1, "name") is not None
