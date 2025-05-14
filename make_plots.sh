#!/bin/bash

# Controlla che sia stata passata una directory come argomento
if [ "$#" -ne 1 ]; then
  echo "Uso: $0 <nome_directory>"
  exit 1
fi

# Directory di input (es: Run_04_prova)
INPUT_DIR="$1"

# Controllo esistenza directory
if [ ! -d "$INPUT_DIR" ]; then
  echo "La directory $INPUT_DIR non esiste."
  exit 1
fi

# Costante
N_stocks=400

# Crea directory Plots se non esiste
PLOTS_DIR="$INPUT_DIR/Plots"
mkdir -p "$PLOTS_DIR"

echo "Cercando file risultati_rolling_temp.pkl dentro $INPUT_DIR con sottocartelle Q_*/Rolling_*/..."

# Array per salvare i risultati
result_files=()

while IFS= read -r file; do
  result_files+=("$file")
done < <(find "$INPUT_DIR" -type f -path "*/Q_*/Rolling_*/risultati_rolling_temp.pkl")

# Processa ogni file trovato
for f in "${result_files[@]}"; do
  rolling_dir=$(basename "$(dirname "$f")")       # es: Rolling_325
  len_rolling="${rolling_dir#Rolling_}"           # es: 325

  q_dir=$(basename "$(dirname "$(dirname "$f")")")  # es: Q_0.50
  q_value="${q_dir#Q_}"                             # es: 0.50

  # Calcola training_size come N_stocks / Q
  training_size=$(python3 -c "print(int($N_stocks / float($q_value)))")

  echo "Produco Plots: $f | Rolling = $len_rolling | Q = $q_value | training_size = $training_size"

  python3 visualize_data.py "$f" \
    --output Multiple_Boxplot \
    --save True \
    --len_rolling "$len_rolling" \
    --training_size "$training_size" \
    --plots_dir "$PLOTS_DIR" \
    --log_scale True
done

# Elimina Directory Vuote
rm -rf Q_*

# Apri i risultati (solo se non sei su cluster)
cd "$PLOTS_DIR" || exit
open *