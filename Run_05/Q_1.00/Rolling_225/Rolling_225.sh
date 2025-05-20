#!/bin/bash
#SBATCH --job-name=R_225_T400
#SBATCH --output=Jobs/Q_1.00/Rolling_225/Rolling_225.txt
#SBATCH --partition=short
#SBATCH --mem=6000
cd $SLURM_SUBMIT_DIR

export ENV=cluster
python3 ~/CODE/prova.py --len_rolling 225 --training_size 400 --cluster True

