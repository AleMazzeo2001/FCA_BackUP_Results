#!/bin/bash

# Controlla che sia stata passata una directory come argomento
if [ "$#" -ne 1 ]; then
  echo "Uso: $0 <nome_directory>"
  exit 1
fi

INPUT_DIR="$1"

if [ ! -d "$INPUT_DIR" ]; then
  echo "La directory $INPUT_DIR non esiste."
  exit 1
fi

N_stocks=400
PLOTS_DIR="$INPUT_DIR/Plots"
mkdir -p "$PLOTS_DIR"

RESULT_FILE="$INPUT_DIR/risultati_finali.txt"
echo "Q,len_rolling,strategy,method,mean,variance" > "$RESULT_FILE"

echo "Cercando file Rolling_*.txt dentro $INPUT_DIR con sottocartelle Q_*/Rolling_*/..."

while IFS= read -r f; do
  rolling_dir=$(basename "$(dirname "$f")")
  len_rolling="${rolling_dir#Rolling_}"

  q_dir=$(basename "$(dirname "$(dirname "$f")")")
  q_value="${q_dir#Q_}"

  echo "Processando file: $f (Q=$q_value, len=$len_rolling)"

  tail -n 24 "$f" | while read -r line; do
    # Salta righe vuote o intestazioni
    [[ -z "$line" ]] && continue
    [[ "$line" =~ ^[-]+$ ]] && continue
    [[ "$line" =~ ^STRATEGY ]] && continue

    # Rimuove eventuali pipe "|"
    line_cleaned=$(echo "$line" | tr -d '|')

    # Estrai valori
    strategy=$(echo "$line_cleaned" | awk '{print $1}')
    method=$(echo "$line_cleaned" | awk '{print $2}')
    mean=$(echo "$line_cleaned" | awk '{print $3}')
    variance=$(echo "$line_cleaned" | awk '{print $5}')

    echo "$q_value,$len_rolling,$strategy,$method,$mean,$variance" >> "$RESULT_FILE"
  done

done < <(find "$INPUT_DIR" -type f -path "*/Q_*/Rolling_*/Rolling_*.txt")

echo "File risultati salvato in: $RESULT_FILE"