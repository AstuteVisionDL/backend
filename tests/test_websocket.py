from fastapi.testclient import TestClient
CORRECT_IMAGE_URL = "data:image/jpeg;base64,/9j/4AAQSkZJ"


def test_websocket(client: TestClient) -> None:
    with client.websocket_connect("/ws") as websocket:
        websocket.send_text(CORRECT_IMAGE_URL)
        data = websocket.receive_json()
        websocket.close()
        assert "items" in data
        assert isinstance(data["items"], list)
