import requests
def test_add_and_complete():
    create_data = {
        "title": "Pluse",
        "completed": False}
    response_create = requests.post("https://todo-app-sky.herokuapp.com/", json=create_data)
    created_task = response_create.json()
    assert response_create.status_code == 200
    assert 'id' in created_task
    task_id = created_task['id']
    update_data = {
        "completed": True}
    response_patch = requests.patch(f"https://todo-app-sky.herokuapp.com/{task_id}", json=update_data)
    assert response_patch.status_code == 200
    response_get = requests.get(f"https://todo-app-sky.herokuapp.com/{task_id}")
    updated_task = response_get.json()
    assert response_get.status_code == 200
    assert updated_task['completed'] == True