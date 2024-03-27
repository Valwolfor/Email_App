import pytest
from main import app as flask_app
from flask_jwt_extended import create_access_token


@pytest.fixture
def app():
    flask_app.config["TESTING"] = True
    # flask_app.config['ERROR_404_HELP'] = False
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()

def test_emails_inbox(client):
    # TODO: This shouldn't be hard coded but accessing with function gives: OutOfContextError
    access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxMTU1MzY3NywianRpIjoiY2M3YmRkMjgtMWRiYS00NWI4LWI1NjctNzI5ZGYwMjJhNDM2IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImNhcmxvc3F1aW50ZXJvMkBnbWFpbC5jb20iLCJuYmYiOjE3MTE1NTM2NzcsImNzcmYiOiIwMmZiMWFkYi0yMDNhLTRmZjMtYmM1Ni01ZGMzMGViZWNiZGUifQ.Wnp2j0TU2OnUSFMMQD6V5JWX7K1U6SCDXygNrGQGMSg"  # create_access_token("carlosquintero2@gmail.com", expires_delta=False)
    headers = {"Authorization": "Bearer {}".format(access_token)}

    response = client.get("/api/emails/inbox", headers=headers)
    resturned_mail = str(response.data)

    assert response.status_code == 200
    assert (
        "carlosquintero2@gmail.com" in resturned_mail
        and "recipient_folder" in resturned_mail
    )
    # TODO: How to test the contents of the inbox email?


def test_emails_sent(client):

    # TODO: This shouldn't be hard coded but accessing with function gives: OutOfContextError
    access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxMTU1MzY3NywianRpIjoiY2M3YmRkMjgtMWRiYS00NWI4LWI1NjctNzI5ZGYwMjJhNDM2IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImNhcmxvc3F1aW50ZXJvMkBnbWFpbC5jb20iLCJuYmYiOjE3MTE1NTM2NzcsImNzcmYiOiIwMmZiMWFkYi0yMDNhLTRmZjMtYmM1Ni01ZGMzMGViZWNiZGUifQ.Wnp2j0TU2OnUSFMMQD6V5JWX7K1U6SCDXygNrGQGMSg"  # create_access_token("carlosquintero2@gmail.com", expires_delta=False)
    headers = {"Authorization": "Bearer {}".format(access_token)}

    response = client.get("/api/emails/sent", headers=headers)
    resturned_mail = str(response.data)

    assert response.status_code == 200
    assert (
        "carlosquintero2@gmail.com" in resturned_mail
        and "recipient_folder" in resturned_mail
    )
    # TODO: How to test the contents of the inbox email?


def test_one_get_email_inbox(client):
    primary_key = "f1af4546-989e-4b01-a5ea-baf90ca4dbb0"

    # TODO: This shouldn't be hard coded but accessing with function gives: OutOfContextError
    access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxMTU1MzY3NywianRpIjoiY2M3YmRkMjgtMWRiYS00NWI4LWI1NjctNzI5ZGYwMjJhNDM2IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImNhcmxvc3F1aW50ZXJvMkBnbWFpbC5jb20iLCJuYmYiOjE3MTE1NTM2NzcsImNzcmYiOiIwMmZiMWFkYi0yMDNhLTRmZjMtYmM1Ni01ZGMzMGViZWNiZGUifQ.Wnp2j0TU2OnUSFMMQD6V5JWX7K1U6SCDXygNrGQGMSg"  # create_access_token("carlosquintero2@gmail.com", expires_delta=False)
    headers = {"Authorization": "Bearer {}".format(access_token)}

    response = client.get("/api/emails/inbox/{}".format(primary_key), headers=headers)
    resturned_mail = str(response.data)

    assert response.status_code == 200
    assert (
        "carlosquintero2@gmail.com" in resturned_mail
        and "recipient_folder" in resturned_mail
    )
    # TODO: How to test the contents of the inbox email?


def test_one_get_email_sent(client):
    primary_key = "f1af4546-989e-4b01-a5ea-baf90ca4dbb0"

    # TODO: This shouldn't be hard coded but accessing with function gives: OutOfContextError

    access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxMTU1MzY3NywianRpIjoiY2M3YmRkMjgtMWRiYS00NWI4LWI1NjctNzI5ZGYwMjJhNDM2IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImNhcmxvc3F1aW50ZXJvMkBnbWFpbC5jb20iLCJuYmYiOjE3MTE1NTM2NzcsImNzcmYiOiIwMmZiMWFkYi0yMDNhLTRmZjMtYmM1Ni01ZGMzMGViZWNiZGUifQ.Wnp2j0TU2OnUSFMMQD6V5JWX7K1U6SCDXygNrGQGMSg" #create_access_token("carlosquintero2@gmail.com", expires_delta=False)
    headers = {"Authorization": "Bearer {}".format(access_token)}

    response = client.get("/api/emails/sent/{}".format(primary_key), headers=headers)
    resturned_mail = str(response.data)

    assert response.status_code == 200
    assert (
        "carlosquintero2@gmail.com" in resturned_mail
        and "recipient_folder" in resturned_mail
    )
    # TODO: How to test the contents of the inbox email?
