import os
import numpy as np
from shutil import copyfile

#######################################################################################

intermsof = 'eV' # Either 'eV' or 'um' (pick which unit the name of folders to be in.)
start = 0.25   	 # Starting wavelength or energy of spectrum 
finish = 2.5	 # Highest wavelength or energy of spectrum (must be > start)
num = 101      	 # Number of wavelengths / energy points in spectrum
howmany = 51	 # How many wavelenghts / energy points per job 

#######################################################################################

def make_directories(intermsof, start, finish, num):
	if intermsof == 'eV':
		points = np.linspace(start, finish, num)
		for i in points:
			name = str("%.3f" % i) + str('_eV')
			os.mkdir(name)
			copyfile('ddscat.par', str(name)+str('/ddscat.par'))
			new_ddscatpar = open(str(name)+str('/ddscat.par'))
			lines = new_ddscatpar.readlines()
			new_wavelength = np.round(1.240/i,4)	
			new_string = str(' ') + str("%.4f" % new_wavelength) + str(' ') + str("%.4f" % new_wavelength) + str(" 1 'INV' = wavelengths (first,last,how many,how=LIN,INV,LOG)" + '\n')
			lines[23] = new_string
			new_ddscatpar = open(str(name)+str('/ddscat.par'), "w")
			new_ddscatpar.writelines(lines)
			new_ddscatpar.close()
			copyfile('shape.dat', str(name)+str('/shape.dat'))

	if intermsof == 'um':
		points = np.linspace(start, finish, num)
		for i in points:
			name = str("%.3f" % i) + str('_um')
			os.mkdir(name)
			copyfile('ddscat.par', str(name)+str('/ddscat.par'))
			new_ddscatpar = open(str(name)+str('/ddscat.par'))
			lines = new_ddscatpar.readlines()
			new_wavelength = np.round(i,4)	
			new_string = str(' ') + str("%.4f" % new_wavelength) + str(' ') + str("%.4f" % new_wavelength) + str(" 1 'INV' = wavelengths (first,last,how many,how=LIN,INV,LOG)" + '\n')
			lines[23] = new_string
			new_ddscatpar = open(str(name)+str('/ddscat.par'), "w")
			new_ddscatpar.writelines(lines)
			new_ddscatpar.close()
			copyfile('shape.dat', str(name)+str('/shape.dat'))




def make_submissionscripts(intermsof, start, finish, num, howmany):
	if intermsof == 'eV':
		points = np.linspace(start, finish, num)
		folders = []
		for i in points:
			name = str("%.3f" % i) + str('_eV')
			folders = np.append(folders, name)
		num_files = int(num/howmany)+1

	if intermsof == 'um':
		points = np.linspace(start, finish, num)
		folders = []
		for i in points:
			name = str("%.3f" % i) + str('_um')
			folders = np.append(folders, name)
		num_files = int(num/howmany)+1

	for j in range(0, num_files):
		copyfile('launch_temp.slurm', str('launch_part')+str(j)+str('.slurm'))
		new_launch = open(str('launch_part')+str(j)+str('.slurm'))
		lines = new_launch.readlines()
		thepoints = folders[j*howmany : (j+1)*howmany]
		new_string = str('array=( ')+' '.join(repr(i) for i in thepoints).replace("'", '"') + str(' )') + str('\n')
		# lines[2] = str('#SBATCH --job-name=eel')+str(j)+str('\n')
		lines[12] = new_string
		new_launch = open(str('launch_part')+str(j)+str('.slurm'),"w")
		new_launch.writelines(lines)
		new_launch.close()

	file = open(str('collect_cross_secs.sh'),'w')
	file.write(str('#!/bin/bash') + '\n')
	file.write(str('# Collect all the files and write it to a file named Spectrum') + '\n')
	if intermsof == 'eV':
		file.write(str('for i in *eV ;do') + '\n')
	if intermsof == 'um':
		file.write(str('for i in *um ;do') + '\n')
	file.write('\t' + str('cd $i; cp gammatable temp') + '\n')
	file.write('\t' + str('sed -i -e "1,14d" temp') + '\n')
	file.write('\t' + str('cat temp >>../Spectrum') + '\n')
	file.write('\t' + str('rm temp') + '\n')
	file.write('\t' + str('rm shape.dat') + '\n')
	file.write('\t' + str('rm w000r000.avg') + '\n')
	file.write('\t' + str('cd ../') + '\n')
	file.write(str('done') + '\n')

make_directories(intermsof=intermsof, start=start, finish=finish, num=num)
make_submissionscripts(intermsof=intermsof, start=start, finish=finish, num=num,howmany=howmany)
