"""
WasteGuard AI Service — FastAPI on Port 8000
Handles: YOLOv11 inference, waste knowledge base
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI(title="WasteGuard AI Service", version="2.0.0")

app.add_middleware(CORSMiddleware, allow_origins=["*"],
                   allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

from routes.detection import router
app.include_router(router, prefix="/api/ai")

@app.get("/api/ai/health")
async def health():
    return {"status": "ok", "service": "WasteGuard AI v2.0"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
