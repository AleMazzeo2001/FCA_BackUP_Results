#!/bin/bash
#SBATCH --job-name=Rolling_70.sh
#SBATCH --output=Jobs/Rolling_70.txt
#SBATCH --partition=short
#SBATCH --mem=6000
cd $SLURM_SUBMIT_DIR

python3 ~/CODE/prova.py --len_rolling 70 
