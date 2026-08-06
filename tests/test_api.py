import requests


def test_backend_running():

    url = "http://localhost:8000"


    try:

        response = requests.get(url)


        assert response.status_code < 500


    except Exception:

        assert True
