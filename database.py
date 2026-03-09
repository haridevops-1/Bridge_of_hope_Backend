from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic_settings import BaseSettings
import os

from dotenv import load_dotenv
import os

# 1. Configuration Setup
# It first looks at Windows Environment, then checks your .env file
load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))
DATABASE_URL = os.getenv("DATABASE_URL")

# If it can't find the link, it gives a clear message
if not DATABASE_URL:
    print("LOG: ERROR - No DATABASE_URL found!")
    SQLALCHEMY_DATABASE_URL = "sqlite:///./fallback.db" # Local temp DB so it doesn't crash
else:
    SQLALCHEMY_DATABASE_URL = DATABASE_URL

# 2. Database Engine Setup
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    pool_pre_ping=True, 
    pool_recycle=3600,
    connect_args={"connect_timeout": 10}
)

# 3. Session and Base Factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
