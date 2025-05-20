#!/bin/bash
#SBATCH --job-name=R_025_T200
#SBATCH --output=Jobs/Q_2.00/Rolling_025/Rolling_025.txt
#SBATCH --partition=short
#SBATCH --mem=6000
cd $SLURM_SUBMIT_DIR

export ENV=cluster
python3 ~/CODE/prova.py --len_rolling 025 --training_size 200 --cluster True

