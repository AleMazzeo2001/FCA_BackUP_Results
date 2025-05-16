#!/bin/bash
#SBATCH --job-name=R_475_T800
#SBATCH --output=Jobs/Q_0.50/Rolling_475/Rolling_475.txt
#SBATCH --partition=short
#SBATCH --mem=6000
cd $SLURM_SUBMIT_DIR

export ENV=cluster
python3 ~/CODE/prova.py --len_rolling 475 --training_size 800 --cluster True

