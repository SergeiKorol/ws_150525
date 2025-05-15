import requests


def test_new_tasks():
    body = {
        "title": "generated-ALLA",
        "completed": True}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    response_body = response.json()
    id = response.json()["id"]
    print(id)

    response = requests.get("https://todo-app-sky.herokuapp.com/")
    assert response.status_code == 200
    assert id > 0
    assert response_body['completed'] == True
