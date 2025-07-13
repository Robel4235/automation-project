from utils.config_loader import load_config
from utils.http_client import get

def is_valid_email(email):
    return "@" in email and "." in email

def test_status_code_comments():
    url = "https://jsonplaceholder.typicode.com/comments"
    config = load_config()
    response = get(f"{url}?postId=1")
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    for comment in response.json():
        assert "postId" in comment , "missing postId"
        assert comment["postId"] == 1, f"expected 1, got {comment['postId']}"
        for field in ["id","name","email","body"]:
            assert field in comment, f"missing {field}"
        assert is_valid_email(comment["email"]), f"invalid email {comment['email']}"



