from fastapi import FastAPI, File, Form, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn, time, os

SECRET = os.getenv("DEMO_SECRET", "default123")

app = FastAPI()

# Allow GitHub Pages domain
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # tighten later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/test")
async def test(secret: str = Form(...), audio: UploadFile = File(...)):
    if secret != SECRET:
        return "Invalid secret"

    # We can ignore the audio for now
    return f"pong {time.time()}"

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
