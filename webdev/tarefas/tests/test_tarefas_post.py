import pytest
from django.urls import reverse
from webdev.tarefas.models import Tarefa


@pytest.fixture
def resposta(client, db):
    resp = client.post(reverse('tarefas:home'), data={'nome': 'Tarefa'})
    return resp


def test_tarefa_existe_no_bd(resposta):
    assert Tarefa.objects.exists()


def test_redirecionamento_depois_do_savalmento(resposta):
    assert resposta.status_code == 302


@pytest.fixture
def resposta_dado_invalido(client, db):
    resp = client.post(reverse('tarefas:home'), data={'nome': ''})
    return resp


def test_tarefa_nao_existe_no_bd(resposta_dado_invalido):
    assert not Tarefa.objects.exists()


def test_pagina_com_dados_invalidos(resposta_dado_invalido):
    assert resposta_dado_invalido.status_code == 400
