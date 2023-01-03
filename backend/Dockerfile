# # Base python package
# FROM python:3.8-slim-buster

# # Set up ENV
# ENV FLASK_APP=app.py
# ENV FLASK_RUN_HOST=0.0.0.0
# ENV FLASK_RUN_PORT=5025

# # Working directory
# WORKDIR /app
    
# # Copy the dependencies
# COPY requirements.txt requirements.txt

# # Install the dependencies
# RUN pip3 install -r requirements.txt

# # Copy the files
# # COPY js js
# COPY sqlFolder sqlFolder
# COPY templates templates 
# COPY app.py app.py

# # Expose a port
# EXPOSE 5025

# # Executable commands
# CMD [ "flask", "run"]
# # CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]



## ----------------
## Départ de Ubuntu
FROM ubuntu:18.04
ENV DEBIAN_FRONTEND=noninteractive


## Installation de FreeTDS FreeTDS et ses dépendences
RUN apt-get update

## ----------------------------------------------------------------------------------------------------------
##  Installation de Python3 (--no-install-recommends build-essential limite l'installation au strict minimum)
RUN apt-get install -y --no-install-recommends build-essential \
python3 \
python3-pip \
python3-setuptools \
python3-dev

RUN pip3 install --upgrade pip

RUN apt-get update && apt-get install -y \
wget && \
rm -rf /var/lib/apt/lists/*


## ---------------------------------------------------
## Lien vers les variables d'environnements manquantes
ENV PYTHONPATH "${PYTHONPATH}:/app"
WORKDIR /app

## -----------------------------------------------
## Copie + installation des libraries R et Python
COPY requirements.txt .
RUN pip install -r requirements.txt 

## --------------------------------------------------------------------------------------------------------------
## Copie du dossier src (qui contient le code Python et R nécessaire pour runner l'API) dans le working directory
# COPY sqlFolder sqlFolder
COPY sqlFolder sqlFolder
COPY templates templates 
COPY app.py app.py


## ---------------------------------------------------------------------------------------------------------------
## Donne les permissions d'écriture pour pouvoir updater les fichiers csv plus tard (à faire après la copy de src)
RUN chmod -R 777 /app
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

## --------------------------------------------------------
## Démarre le serveur web python qui permet d'appeler l'API
EXPOSE 5025
CMD ["python3", "app.py"]