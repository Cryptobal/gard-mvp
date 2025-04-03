from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()

@app.get('/health')
def health():
    return {'status': 'ok'}

if __name__ == "__main__":
    client = TestClient(app)
    response = client.get('/health')
    print(response.json()) 