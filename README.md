# Analysis of Large Blast Inputs: A.L.B.I

This package is a collection of individual python scripts that can perform data parsing of standalone BLAST+ ouput file. Besides this, SLURM and PBS scripts have been provided to run large BLAST+ inputs which can be useful for metagenomic data analysis.


### Installation

Does not require installation, can be run by invoking python in windows or linux. All the scripts were written in Python v.3.8.0

### Prerequisites

python library: numpy & matplotlib 

### Usage

#### For extracting the top similarity hits out of the BLAST+ default 5:

python topscore_headers.py

Input file: blast_input.txt 

Output file: out2.txt
  
#### For finding relative abundance of a single user defined protien

python relative_abundance.py

Input file: out2.txt

#### For comparing abundance of multiple user defined proteins with graphical output

python protein_graph.py

Input file: out2.txt

#### To convert BLAST+ output file into FASTA file

Keeping im mind the various requirements a user may have  


#### HPC job scripts

Make the necessary changes such as the no. of CPUs, threads according to your configuration. Save the file with .slurm, .sh extensions and adjust line breaking styles based on your system requirements. 

### Support

SRM-IST HPC systems

### License

GNU General Public License v3.0 (https://www.gnu.org/licenses/gpl-3.0.en.html)


### Project status


