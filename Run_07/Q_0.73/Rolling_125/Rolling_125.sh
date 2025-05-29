#!/bin/bash
#SBATCH --job-name=R_125_T550
#SBATCH --output=Jobs/Q_0.73/Rolling_125/Rolling_125.txt
#SBATCH --partition=short
#SBATCH --mem=6000
cd $SLURM_SUBMIT_DIR

export ENV=cluster
python3 ~/CODE/prova.py --len_rolling 125 --training_size 550 --cluster True

