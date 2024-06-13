# Wybieramy obraz bazowy
FROM python:3.9-slim

# Ustawiamy zmienną środowiskową
ENV PYTHONUNBUFFERED=1

# Ustawiamy katalog roboczy
WORKDIR /app

# Kopiujemy plik requirements.txt do katalogu roboczego
COPY requirements.txt /app/

# Instalujemy wymagane pakiety
RUN pip install --no-cache-dir -r requirements.txt

# Kopiujemy całą zawartość katalogu roboczego do obrazu
COPY . /app/

# Otwieramy port 5000
EXPOSE 5000

# Dodajemy skrypt inicjalizujący bazę danych
RUN python init_db.py

# Definiujemy komendę startową
CMD ["flask", "run", "--host=0.0.0.0"]
