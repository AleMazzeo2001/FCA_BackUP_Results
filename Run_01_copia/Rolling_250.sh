#!/bin/bash
#SBATCH --job-name=Rolling_250.sh
#SBATCH --output=Jobs/Rolling_250.txt
#SBATCH --partition=short
#SBATCH --mem=6000
cd $SLURM_SUBMIT_DIR

python3 ~/CODE/prova.py --len_rolling 250 
