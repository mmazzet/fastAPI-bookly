

auth_prefix = f"/api/v1/auth"

def test_user_creation(fake_session, fake_user_service, test_client):
    
    signup_data={
        "first_name":"richie",
        "last_name": "turcotte",
        "email" : "richie.turcotte@ethereal.email",
        "username" : "turco",
        "password" : "secret"
    },

    response = test_client.post(
        url=f"{auth_prefix}/signup",
        json=signup_data,
    )

    assert fake_user_service.user_exists_called_once()