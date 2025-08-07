from http import HTTPStatus


def test_root_should_return_welcome_to_fast_zero(client):
    """Testa o endpoint root da aplicação"""
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Welcome to Fast Zero!'}
