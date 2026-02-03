def test_register_and_login(client):
    # 1. Test Registration
    response = client.post('/register', json={
        "email": "test@example.com",
        "password": "securepassword123",
        "studio_name": "Test Studio"
    })
    assert response.status_code == 201
    assert b"User registered successfully" in response.data

    # 2. Test Login (Success)
    login_response = client.post('/login', json={
        "email": "test@example.com",
        "password": "securepassword123"
    })
    assert login_response.status_code == 200
    assert b"Logged in successfully" in login_response.data

    # 3. Test Login (Failure)
    fail_response = client.post('/login', json={
        "email": "test@example.com",
        "password": "wrongpassword"
    })
    assert fail_response.status_code == 401
    assert b"Invalid email or password" in fail_response.data