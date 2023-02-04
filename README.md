- [last update](#last-update)
- [*WARNING*](#warning)
- [dataset preparation scripts](#dataset-preparation-scripts)
    - [subseting eigen files (subset\_eigen.py)](#subseting-eigen-files-subset_eigenpy)
    - [convert plink \[bed,bim,fam\] to eigen \[geno,snp,ind\] (the script name is b2e)](#convert-plink-bedbimfam-to-eigen-genosnpind-the-script-name-is-b2e)
- [qsub related](#qsub-related)
    - [creating qsub files for running commands in parallel on many nodes (add\_wait\_qsub)](#creating-qsub-files-for-running-commands-in-parallel-on-many-nodes-add_wait_qsub)

# last update
24/02/2023

# *WARNING*

*These scripts may contain some bugs. Please always control your outputs. Use them at your own risk. You may optimize them to be more compatible with your works. I would be grateful if you could report bugs or problems in the scripts. I try to upload the scripts regularly. Most (if not all) of my script contain help (just run script -h)*


# dataset preparation scripts

### subseting eigen files (subset_eigen.py)

subseting eigen dataset with list of population. You must have convertf in the PATH

flags  
  
\-i, --input: prefix of input eigen dataset  
\-o, --output: prefix of output (subsetted) eigen dataset  
\-p, --popfile: a file containing list of populations, one pop per line

example  

```
subset_eigen.py -i dataset_input -p pop_list -o subseted_dataset_output
```
### convert plink [bed,bim,fam] to eigen [geno,snp,ind] (the script name is b2e)

You must have convertf in the PATH  
        
flags

\-e prefix of eigen files  
\-b prefix of plink files (bed,bim,fam)  
\-p par file name  
\-d if want the script to delete ped file (intermediate file of this script) afterwards, type yes 

```
b2e -e prefix_of_eigen_files -b prefix_of_plink_files -p par_file_name -d yes
```

# qsub related 

### creating qsub files for running commands in parallel on many nodes (add_wait_qsub)
  
    
It is a bit hard to explain what this script does. Just imagine that you have to test 80000 genetic models. You need one thread to test each model. There are 80 threads available on each node. You want to run 80 models (max capacity for each node) at a time per node and you want to run them in parallel on 10 nodes. This is the script for you. It will create qsub files for running the commands in parallel. 

> You may need to modify the header for your cluster. See the script.
  
I feel a bit nostalgic about this script. It was one of the first scripts I wrote. Here is how to use the script.

*flags*

\-j [name of job]  
\-i [input file which contains list of commands, you must have empty line as last line]  
\-n [number of nodes you want to run]  
\-t [threads per each node you want to run at a time]  
\-d [working directory]

  
  
You will see commands for running qsub in the file 'command_list_for_qsub' (output of this script)

example

```
add_wait_qsub -j jobname -i input_list_of_command -n 10 -t 80 -d /working/directory
```
