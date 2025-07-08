from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import settings
from .routes import router
import os

app = FastAPI()

#Cors allow origins from environment variable
origins_raw = os.getenv("MOODLE", "")
origins = [o.strip() for o in origins_raw.split(",") if o.strip()]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the routes
app.include_router(router)


