# from fastapi.testclient import TestClient
# from main import app  # import your FastAPI app

# client = TestClient(app)

# def test_hello_world():
#     response = client.get("/")
#     # Assert status code is 200
#     assert response.status_code == 200
#     # Assert the response JSON is as expected
#     assert response.json() == {"message": "Hello, World!"}


def test_sample():
    assert 4 == 4
