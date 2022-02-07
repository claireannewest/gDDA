#!/bin/bash
#SBATCH --mail-user=caw97@cam.ac.uk
#SBATCH --job-name=collect
#SBATCH --nodes=1
#SBATCH --mem-per-cpu=4G
#SBATCH --output=slurm-%j.out

echo "here we are"
bash collect_cross_secs.sh
