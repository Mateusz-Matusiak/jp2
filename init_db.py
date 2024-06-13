from models import Base, engine

# Tworzenie tabel
Base.metadata.create_all(bind=engine)
print("Database initialized.")
