import uvicorn
from fastapi import FASTAPI

app = FASTAPI()

def main():
    uvicorn.run(
        "app.main.app",
        host = settings.host_address,
        port = settings.port,
        log_level = "debug",
    )
