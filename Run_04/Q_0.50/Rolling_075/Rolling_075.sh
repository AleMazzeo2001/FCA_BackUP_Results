#!/bin/bash
#SBATCH --job-name=R_075_T800
#SBATCH --output=Jobs/Q_0.50/Rolling_075/Rolling_075.txt
#SBATCH --partition=short
#SBATCH --mem=6000
cd $SLURM_SUBMIT_DIR

export ENV=cluster
python3 ~/CODE/prova.py --len_rolling 075 --training_size 800 --cluster True

