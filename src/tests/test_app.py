def test_root_must_returns_200_and_expected_string(client):
    response = client.get('/')

    assert response.status_code == 200
    assert response.json() == {'message': 'Home sweet home!'}
