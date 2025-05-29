#!/bin/bash
#SBATCH --job-name=R_125_T140
#SBATCH --output=Jobs/Q_2.86/Rolling_125/Rolling_125.txt
#SBATCH --partition=short
#SBATCH --mem=6000
cd $SLURM_SUBMIT_DIR

export ENV=cluster
python3 ~/CODE/prova.py --len_rolling 125 --training_size 140 --cluster True

