from fastapi import FastAPI
import uvicorn
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static folder
app.mount("/static", StaticFiles(directory="static", html=True), name="static")

# Serve index.html at "/"
@app.get("/")
async def root():
    return FileResponse("static/index.html")

@app.get("/greet/{name}")
def greet(name: str):
    return {
        "greeting": f"Hello {name}",
        "length_of_name": len(name),
        "uppercase_name": name.upper()
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)
