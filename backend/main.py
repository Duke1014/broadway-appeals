import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from supabase import create_client, Client
from dotenv import load_dotenv

from models import ShowResponse, ShowBase

load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("Supabase credentials not found in the .env file")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Change this to your Vercel URL later for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

# @app.get("/shows", response_model=list[ShowResponse])
# def get_shows():
#     response = supabase.table("shows").select("*").execute()
#     if response.data:
#         return response.data
#     return []

# # --- Example Endpoint: Create a show ---
# @app.get("/shows/create", response_model=ShowResponse) # Just for testing; normally a POST request!
# def create_test_show():
#     test_show = {
#         "title": "The Phantom of the Opera",
#         "theatre": "Majestic Theatre",
#         "show_time": "8:00 PM"
#     }
#     response = supabase.table("shows").insert(test_show).execute()
    
#     if response.data:
#         return response.data[0]
#     raise HTTPException(status_code=400, detail="Failed to create show")

# def getAssignments():
#     return "Here is some data"