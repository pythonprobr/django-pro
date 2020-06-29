from django.test import Client


def test_home_status_code(client: Client):
    reposta = client.get('/')
    assert reposta.status_code == 200
