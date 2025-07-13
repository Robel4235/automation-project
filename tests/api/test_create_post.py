from utils.config_loader import load_config
from utils.http_client import post
from utils.json_loader import load_json
from utils.json_loader import get_all_json_files
import pytest
import os
from pathlib import Path

#def test_create_post():
    #url = "https://jsonplaceholder.typicode.com/posts"
    #data = load_json(r"C:\Users\avrah\PycharmProjects1\PythonProject\Api_ui_practice\data\create_post.json")
    #response = post(url, json=data)
    #assert response.status_code == 201 , f"Expected 201, got {response.status_code}"
    #assert data["title"] == response.json()["title"] , f"Expected {response.json()['title']}, got {response.json()['title']}"
    #assert data["body"] == response.json()["body"], f"Expected {response.json()['body']}, got {response.json()['body']}"
    #assert data["userId"] == response.json()["userId"], f"Expected {response.json()['userId']}, got {response.json()['userId']}"
    #assert "id" in response.json()
DATA_DIR = Path(__file__).resolve().parent.parent.parent / "data" / "create_post"


@pytest.mark.parametrize("json_file", get_all_json_files(str(DATA_DIR)))
def test_create_post_with_multiple_dataload(json_file):
    url = "https://jsonplaceholder.typicode.com/posts"
    data = load_json(json_file)
    response = post(url, json=data)
    assert response.status_code == 201 , f"Expected 201, got {response.status_code}"
    assert data["title"] == response.json()["title"] , f"Expected {response.json()['title']}, got {response.json()['title']}"
    assert data["body"] == response.json()["body"], f"Expected {response.json()['body']}, got {response.json()['body']}"
    assert data["userId"] == response.json()["userId"], f"Expected {response.json()['userId']}, got {response.json()['userId']}"
    assert "id" in response.json()



