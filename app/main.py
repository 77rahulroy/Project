from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
import pathlib

app = FastAPI(title="Sample FastAPI App")

# Mount static files (CSS/JS/HTML)
static_dir = pathlib.Path(__file__).parent / "static"
app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")


@app.get("/")
async def serve_ui():
    index_path = static_dir / "index.html"
    return FileResponse(index_path)


@app.get("/api/health")
async def health():
    return JSONResponse({"status": "ok"})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
