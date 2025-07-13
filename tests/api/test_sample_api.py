from utils.config_loader import load_config
from utils.http_client import get

def test_status_code():
    config = load_config()
    response = get(config["base_url"])
    assert response.status_code == 200
