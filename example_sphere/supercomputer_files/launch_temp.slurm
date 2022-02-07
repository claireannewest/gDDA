#!/bin/bash
#SBATCH --mail-user=caw97@cam.ac.uk
#SBATCH --job-name=eel
#SBATCH --nodes=1
#SBATCH --mem-per-cpu=4G
##SBATCH --mail-type=START,FAIL,END
#SBATCH --output=slurm-%j.out

module load anaconda3

#################################################

# array of calculations goes here # 

#################################################

for ((i=0;i<${#array[@]};++i)); do
    file=${array[i]}
    cd ${file}
    /home/caw97/source_code/g-dda/source_code/ddscat &> ${file}.out &
    cd ..
done; wait



