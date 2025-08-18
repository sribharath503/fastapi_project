from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base,session



load_dotenv()

DATABASE_URL=os.getenv("DATABASE_URL")

engine=create_engine(DATABASE_URL)

SessionLocal=sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base=declarative_base()


def get_db():
    db: session = SessionLocal()
    try:
        yield db
    finally:
        db.close()


