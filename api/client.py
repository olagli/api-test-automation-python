import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def get_users():
    return requests.get(f"{BASE_URL}/users")


def create_post(payload):
    return requests.post(f"{BASE_URL}/posts", json=payload)


def update_post(post_id, payload):
    return requests.put(f"{BASE_URL}/posts/{post_id}", json=payload)


def delete_post(post_id):
    return requests.delete(f"{BASE_URL}/posts/{post_id}")