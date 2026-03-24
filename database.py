from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///./blog.db"
# SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://postgres:Bee@08088@localhost:5432/blog_db"
connect_args = {"check_same_thread": False}
engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args=connect_args,
    echo=True,
)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False,
)


class Base(DeclarativeBase):
    pass


async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
