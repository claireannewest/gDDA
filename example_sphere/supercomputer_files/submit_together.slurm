#!/bin/bash
#SBATCH --mail-user=caw97@cam.ac.uk
#SBATCH --job-name=submit
#SBATCH --nodes=1
#SBATCH --mem-per-cpu=4G
#SBATCH --output=slurm-%j.out

module load anaconda3
python make_dirs.py
wait

for file in launch_part*;
do
  sbatch $file
done

wait

sbatch --dependency=singleton --job-name=eel collect.slurm
