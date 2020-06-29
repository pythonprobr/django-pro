import pytest
from django.urls import reverse
from pytest_django.asserts import assertContains

from webdev.tarefas.models import Tarefa


@pytest.fixture
def tarefa_pendente(db):
    return Tarefa.objects.create(nome='Tarefa 1', feita=False)


@pytest.fixture
def resposta_com_tarefa_pendente(client, tarefa_pendente):
    resp = client.post(
        reverse('tarefas:detalhe', kwargs={'tarefa_id': tarefa_pendente.id}),
        data={'feita': 'true', 'nome': f'{tarefa_pendente.nome}-editada'}
    )
    return resp


def test_status_code(resposta_com_tarefa_pendente):
    assert resposta_com_tarefa_pendente.status_code == 302


def test_tarefa_feita(resposta_com_tarefa_pendente):
    assert Tarefa.objects.first().feita


@pytest.fixture
def tarefa_feita(db):
    return Tarefa.objects.create(nome='Tarefa 1', feita=True)


@pytest.fixture
def resposta_com_tarefa_feita(client, tarefa_feita):
    resp = client.post(
        reverse('tarefas:detalhe', kwargs={'tarefa_id': tarefa_feita.id}),
        data={'nome': f'{tarefa_feita.nome}-editada'}
    )
    return resp


def test_tarefa_pendentes(resposta_com_tarefa_feita):
    assert not Tarefa.objects.first().feita
