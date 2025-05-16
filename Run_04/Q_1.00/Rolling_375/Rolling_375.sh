#!/bin/bash
#SBATCH --job-name=R_375_T400
#SBATCH --output=Jobs/Q_1.00/Rolling_375/Rolling_375.txt
#SBATCH --partition=short
#SBATCH --mem=6000
cd $SLURM_SUBMIT_DIR

export ENV=cluster
python3 ~/CODE/prova.py --len_rolling 375 --training_size 400 --cluster True

