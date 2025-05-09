#!/bin/bash

# Controlla che sia stato passato un argomento
if [ -z "$1" ]; then
    echo "Utilizzo: $0 nome_archivio_senza_estensione"
    exit 1
fi

# Nome base passato da linea di comando
NOME="$1"
FILE="${NOME}.tgz"
REMOTE_PATH="mazzeo@neowulf.pv.infn.it:~/CODE/${FILE}"

# Scarica il file tramite scp
echo "Scaricamento di $FILE da neowulf..."
scp "$REMOTE_PATH" .

# Controlla se lo scp ha avuto successo
if [ $? -ne 0 ]; then
    echo "Errore durante il download di $FILE"
    exit 1
fi

echo "Download completato. Estrazione in corso..."

# Estrai il file .tgz
tar -xvzf "$FILE"

# Controllo finale
if [ $? -eq 0 ]; then
    echo "Estrazione completata."
else
    echo "Errore durante l'estrazione di $FILE"
    exit 1
fi