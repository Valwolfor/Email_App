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
    access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxMTU1NTE5MCwianRpIjoiZGRiOTQzMDYtMjg3Yi00MGJlLThjNjYtNTdiMjdiZDVlY2FlIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImNhcmxvc3F1aW50ZXJvMkBnbWFpbC5jb20iLCJuYmYiOjE3MTE1NTUxOTAsImNzcmYiOiI3MGY0NWQ4My1mMTkxLTRkN2YtOGM5MS0xYTUxYTc4YWNiOGUifQ.sQ71faNI47vvA3jJmp8qszVgtVQgRstiJuIUwW_badk"  # create_access_token("carlosquintero2@gmail.com", expires_delta=False)
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
    access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxMTU1NTE5MCwianRpIjoiZGRiOTQzMDYtMjg3Yi00MGJlLThjNjYtNTdiMjdiZDVlY2FlIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImNhcmxvc3F1aW50ZXJvMkBnbWFpbC5jb20iLCJuYmYiOjE3MTE1NTUxOTAsImNzcmYiOiI3MGY0NWQ4My1mMTkxLTRkN2YtOGM5MS0xYTUxYTc4YWNiOGUifQ.sQ71faNI47vvA3jJmp8qszVgtVQgRstiJuIUwW_badk"  # create_access_token("carlosquintero2@gmail.com", expires_delta=False)
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
    primary_key = "77486b62-22d0-42ea-8eba-d25841eae014"

    # TODO: This shouldn't be hard coded but accessing with function gives: OutOfContextError
    access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxMTU1NTE5MCwianRpIjoiZGRiOTQzMDYtMjg3Yi00MGJlLThjNjYtNTdiMjdiZDVlY2FlIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImNhcmxvc3F1aW50ZXJvMkBnbWFpbC5jb20iLCJuYmYiOjE3MTE1NTUxOTAsImNzcmYiOiI3MGY0NWQ4My1mMTkxLTRkN2YtOGM5MS0xYTUxYTc4YWNiOGUifQ.sQ71faNI47vvA3jJmp8qszVgtVQgRstiJuIUwW_badk"  # create_access_token("carlosquintero2@gmail.com", expires_delta=False)
    headers = {"Authorization": "Bearer {}".format(access_token)}

    response = client.get("/api/emails/inbox/{}".format(primary_key), headers=headers)
    resturned_mail = str(response.data)

    assert response.status_code == 200
    assert (
        "carlosquintero2@gmail.com" in resturned_mail
        and "recipient_folder" in resturned_mail
    )
    # TODO: How to test the contents of the inbox email?


def test_one_get_email_sent(client): #from another email sender.
    primary_key = "66cf8a0f-e8fe-49a6-9a0c-297595beb4da"

    # TODO: This shouldn't be hard coded but accessing with function gives: OutOfContextError

    access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxMTU1NTE5MCwianRpIjoiZGRiOTQzMDYtMjg3Yi00MGJlLThjNjYtNTdiMjdiZDVlY2FlIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImNhcmxvc3F1aW50ZXJvMkBnbWFpbC5jb20iLCJuYmYiOjE3MTE1NTUxOTAsImNzcmYiOiI3MGY0NWQ4My1mMTkxLTRkN2YtOGM5MS0xYTUxYTc4YWNiOGUifQ.sQ71faNI47vvA3jJmp8qszVgtVQgRstiJuIUwW_badk" #create_access_token("carlosquintero2@gmail.com", expires_delta=False)
    headers = {"Authorization": "Bearer {}".format(access_token)}

    response = client.get("/api/emails/sent/{}".format(primary_key), headers=headers)
    resturned_mail = str(response.data)

    assert response.status_code == 200
    assert (
        "carlosquintero2@gmail.com" in resturned_mail
        and "recipient_folder" in resturned_mail
    )
    # TODO: How to test the contents of the inbox email?
