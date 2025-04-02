# Connection to PostgreSQL database using SQLAlchemy
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Read DB settings from environment variables
user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")
host = os.getenv("POSTGRES_HOST")
port = os.getenv("POSTGRES_PORT")
database = os.getenv("POSTGRES_DB")

# Validate required env vars
if not all([user, password, host, port, database]):
    raise ValueError("Missing one or more required environment variables for DB connection.")

# Ensure port is an int
port = int(port)

# Construct the database URL
DATABASE_URL = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL)