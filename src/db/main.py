from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel, create_engine, text
from sqlmodel.ext.asyncio.session import AsyncSession

from src.config import Config

async_engine = AsyncEngine(create_engine(url=Config.DATABASE_URL))

async def init_db():
    async with async_engine.begin() as conn:
        from src.db.models import Book

        await conn.run_sync(SQLModel.metadata.create_all)

async def get_session() ->AsyncSession:
    
    Session = sessionmaker(
        bind=async_engine,
        class_=AsyncSession,
        expire_on_commit=False
    )

    async with Session() as session:
        yield session