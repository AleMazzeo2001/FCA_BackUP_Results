#!/bin/bash
#SBATCH --job-name=Rolling_10.sh
#SBATCH --output=Jobs/Rolling_10.txt
#SBATCH --partition=short
#SBATCH --mem=6000
cd $SLURM_SUBMIT_DIR

python3 ~/CODE/prova.py --len_rolling 10 
