from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Konfiguracja bazy danych SQLite
DATABASE_URL = "sqlite:///warehouse.db"

Base = declarative_base()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Definicja modelu
class WarehouseItem(Base):
    __tablename__ = 'warehouse_items'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    quantity = Column(Integer)
    description = Column(Text)

# Tworzenie tabeli
Base.metadata.create_all(bind=engine)
