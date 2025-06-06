# Schritt 1: Verwende ein Node.js-Image als Basis
FROM node:18
# Schritt 2: Setze das Arbeitsverzeichnis auf /vue-project
WORKDIR /vue-project
# Schritt 3: Kopiere die package.json und package-lock.json in das Image
COPY package*.json ./
# Schritt 4: Installiere die Abhängigkeiten
RUN npm install
# Schritt 5: Kopiere alle Vue-Dateien ins Arbeitsverzeichnis
COPY . .
# Schritt 6: Baue die Vue-Anwendung
RUN npm run build
# Schritt 7: Exponiere den Port 8080
EXPOSE 8081
# Schritt 8: Starte den Vue-Server
CMD ["npm", "run", "dev"]