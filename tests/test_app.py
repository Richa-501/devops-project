import requests

def test_health():
    response - requests.get("http://localhost:8081/health")
    asset response.status_code == 200
