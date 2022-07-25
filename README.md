# Discrete Dipole Approximation with Gaussian Beam Source
The following code is Draine's DDA version 7.3.2 edited to contain a Gaussian beam excitation source. Draine's User-Guide is included in the repo, but note that the certain changes have been made (e.g., lines added in `ddscat.par`) to the code which will make this user guide not applicable in certain cases. See the changes outlined below. 

## Set up
Make sure you have Fortran compilers installed. Once installed, Compile the source code in the folder `source_code` by typing `make all`. This has been done correctly when the file `ddscat` has been created.


## Examples
The folder `example_sphere` contains example scripts to run calculation(s) of the light scattered by a nanosphere.

### A single scattering calculation
To run a single scattering calculation, see the template files in the folder `single_calculation`.
* Step 1: Create input files.
The file `make_sphere.py` will create a shape file of a nanosphere. This will create the file `shape.dat` which will be compatible with DDA.

* Step 2: Create parameter files.
Edit the file `ddscat.par` according to the normal methods defined in Draine's User Guide. The only modifications are to lines 28 - 31, which specify the Gaussian beam parameters.
* Step 3: Run the script.
To run the script, type `bash run_gdda.sh`. For a 5 nm radius sphere of 1 nm dipole spacing, the code should run within seconds on a local computer.


### An entire spectrum
To run many scattering calculations to form an entire spectrum, see the Jupyter notebook and corresponding template files in the folder `calculate_a_spectrum`.
* Step 1: Follow Jupyter Notebook.



### A spectrum on supercomputer
To run an entire spectrum on a supercomputer, I've provided some scripts in the folder `example_sphere/supercomputer_files`.
* Step 1: Make a shape file.
* Step 2: Edit `ddscat.par`.
* Step 3: Edit lines 7-11 of `make_dirs.py` to define the energy or wavelength window of the calculation. This script will make `num` number of folders and  $int(num/howmany)$ number of launch files. The folders will be named after the wavelength / energy of the calculation.
* Step 4: Look over `launch_temp.slurm` to double check the name of the job, time, and partition to see if that's what you'd like. Run `python make_dirs.py` to then make the folders and files.
* Step 5: After double checking that everything was made correctly, submit the jobs by `bash submit_together.sh`.
* Step 6: Once the calculations are all done, collect all the output files using `bash collect_cross_secs.sh`. To plot the results on your local computer, run `python seeSpectrum.py`.