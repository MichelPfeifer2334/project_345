# Schritt 1: Verwende ein Miniconda-Image als Basis
FROM continuumio/miniconda3

# Schritt 2: Setze das Arbeitsverzeichnis auf /backend
WORKDIR /backend

# Schritt 3: Kopiere die Umgebungsdatei in das Image
COPY environment.yaml /backend/

# Schritt 4: Erstelle die Conda-Umgebung
RUN conda env create -f environment.yaml

# Schritt 5: Aktiviere die Conda-Umgebung
RUN echo "conda activate project" >> ~/.bashrc

# Schritt 6: Kopiere alle Backend-Dateien ins Arbeitsverzeichnis
COPY . /backend/

# Schritt 7: Aktiviere die Conda-Umgebung für alle nachfolgenden Befehle
SHELL ["conda", "run", "-n", "project", "/bin/bash", "-c"]

# Schritt 8: Exponiere den Port 8000
EXPOSE 8000

# Schritt 9: Starte den FastAPI-Server
CMD ["conda", "run", "-n", "project", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--log-level", "debug", "--reload"]


