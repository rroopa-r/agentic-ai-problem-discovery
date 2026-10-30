import os
from dotenv import load_dotenv

# This must come BEFORE you try to access settings
load_dotenv() 

class Settings:
    PROJECT_NAME: str = "Agentic Problem Discovery"
    ANTHROPIC_API_KEY: str = os.getenv("ANTHROPIC_API_KEY")
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
    DATABASE_URL: str = os.getenv("DATABASE_URL")

settings = Settings()

# --- THE TEST CODE ---
print(f"Project: {settings.PROJECT_NAME}")
print(f"Database URL is set: {bool(settings.DATABASE_URL)}")
print(f"OpenAI Key is set: {bool(settings.OPENAI_API_KEY)}")