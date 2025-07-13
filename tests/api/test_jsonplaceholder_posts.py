from utils.http_client import get
from utils.logger import create_logger

logger = create_logger(__name__)

def test_get_all_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = get(url)

    # Assert status code
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    data = response.json()

    # Assert at least 10 items
    assert len(data) >= 10, f"Expected at least 10 posts, got {len(data)}"

    # Assert required fields exist in each post
    for post in data:
        assert "userId" in post, f"Missing 'userId' in post: {post}"
        assert "id" in post, f"Missing 'id' in post: {post}"
        assert "title" in post, f"Missing 'title' in post: {post}"
        assert "body" in post, f"Missing 'body' in post: {post}"

def test_get_user_posts():
    url = "https://jsonplaceholder.typicode.com/posts?userId=1"

    try:
        logger.info(f"Sending GET request to: {url}")
        response = get(url)
        logger.info(f"Response status code: {response.status_code}")
    except Exception as e:
        logger.exception("GET request failed")
        raise AssertionError(f"Test failed due to request error: {e}")

    try:
        posts = response.json()
        assert isinstance(posts, list), f"Expected a list, got {type(posts)}"
        logger.info(f"Number of posts returned: {len(posts)}")

        for post in posts:
            assert post.get("userId") == 1, f"Expected userId=1, got {post.get('userId')}"
            for key in ["id", "title", "body"]:
                assert key in post, f"Missing field '{key}' in post: {post}"

    except Exception as e:
        logger.exception("Failed while validating response content")
        raise AssertionError(f"Validation error: {e}")


