import requests
from utils.logger import create_logger

logger = create_logger(__name__)

def get(url, headers=None, timeout=10):
    try:
        logger.info(f"GET Request: {url}")
        response = requests.get(url, headers=headers, timeout=timeout)
        response.raise_for_status()
        logger.info(f"GET Success: {url} | Status: {response.status_code}")
        return response

    except requests.exceptions.Timeout:
        logger.error(f"Timeout on GET: {url}")
        raise AssertionError(f"GET request to {url} timed out.")

    except requests.exceptions.ConnectionError:
        logger.error(f"Connection error on GET: {url}")
        raise AssertionError(f"GET request to {url} failed: connection error.")

    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error on GET: {url} | {http_err}")
        raise AssertionError(f"GET request to {url} failed with HTTP error: {http_err}")

    except Exception as e:
        logger.exception(f"Unexpected error on GET: {url}")
        raise AssertionError(f"Unexpected error during GET request to {url}: {e}")


def post(url, data=None, json=None, headers=None, timeout=10):
    try:
        logger.info(f"POST Request: {url} | Payload: {json or data}")
        response = requests.post(url, data=data, json=json, headers=headers, timeout=timeout)
        response.raise_for_status()
        logger.info(f"POST Success: {url} | Status: {response.status_code}")
        return response

    except requests.exceptions.RequestException as e:
        logger.error(f"POST failed: {url} | {e}")
        raise AssertionError(f"POST request to {url} failed: {e}")


def put(url, data=None, json=None, headers=None, timeout=10):
    try:
        logger.info(f"PUT Request: {url} | Payload: {json or data}")
        response = requests.put(url, data=data, json=json, headers=headers, timeout=timeout)
        response.raise_for_status()
        logger.info(f"PUT Success: {url} | Status: {response.status_code}")
        return response

    except requests.exceptions.RequestException as e:
        logger.error(f"PUT failed: {url} | {e}")
        raise AssertionError(f"PUT request to {url} failed: {e}")


def delete(url, headers=None, timeout=10):
    try:
        logger.info(f"DELETE Request: {url}")
        response = requests.delete(url, headers=headers, timeout=timeout)
        response.raise_for_status()
        logger.info(f"DELETE Success: {url} | Status: {response.status_code}")
        return response

    except requests.exceptions.RequestException as e:
        logger.error(f"DELETE failed: {url} | {e}")
        raise AssertionError(f"DELETE request to {url} failed: {e}")
