#!/bin/bash

# Controlla che sia stata passata una directory come argomento
if [ "$#" -ne 1 ]; then
  echo "Uso: $0 <nome_directory>"
  exit 1
fi

# Directory di input (es: Run_01_copia)
INPUT_DIR="$1"

# Controllo esistenza directory
if [ ! -d "$INPUT_DIR" ]; then
  echo "La directory $INPUT_DIR non esiste."
  exit 1
fi

# Trova tutti i file risultati_rolling_temp.pkl all'interno della directory specificata
echo "Cercando file risultati_rolling_temp.pkl dentro $INPUT_DIR..."

# Array per salvare i risultati
result_files=()

while IFS= read -r file; do
  result_files+=("$file")
done < <(find "$INPUT_DIR" -type f -name "risultati_rolling_temp.pkl")

# Stampa o usa le variabili trovate
for f in "${result_files[@]}"; do
  echo "Trovato file: $f"
done