import requests

# создать задачу,
def test_add_new():
    body = {"title": "new_vvv2", "completed": False}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)

# удалить созданную задачу,
    id_add = response.json()["id"]
    response = requests.delete(f'https://todo-app-sky.herokuapp.com/{id_add}')

# проверить что гет по удалённой задаче == 404
    assert response.status_code == 404




