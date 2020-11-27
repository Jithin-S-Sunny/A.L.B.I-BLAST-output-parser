# A.L.B.I

This package is a collection of individual python scripts that can perform data parsing of standalone BLAST+ ouput file. Besides this, SLURM and PBS scripts have been provided to run large BLAST+ inputs. This can be useful in metagenomics runs.


### Installation

Does not require installation, can be run by invokin python in windows or linux. All the scripts were written in Python v.3.8.0

### Usage

For extracting the top similarity hits out of the BLAST+ default 5:
python topscore_headers.py
Input: blast_input
Output: out2.txt

For  



#### HPC job scripts

Make the necessary changes such as the no. of CPUs, threads according to your configuration. Save the file with .slurm, .sh extensions and adjust line breaking styles based on your system requirements. 








### License

GNU General Public License v3.0 (https://www.gnu.org/licenses/gpl-3.0.en.html)
