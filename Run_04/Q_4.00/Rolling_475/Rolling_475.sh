#!/bin/bash
#SBATCH --job-name=R_475_T100
#SBATCH --output=Jobs/Q_4.00/Rolling_475/Rolling_475.txt
#SBATCH --partition=short
#SBATCH --mem=6000
cd $SLURM_SUBMIT_DIR

export ENV=cluster
python3 ~/CODE/prova.py --len_rolling 475 --training_size 100 --cluster True

