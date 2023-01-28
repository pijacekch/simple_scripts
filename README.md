- [*WARNING*](#warning)
- [dataset preparation scripts](#dataset-preparation-scripts)
    - [subseting eigen files](#subseting-eigen-files)

# *WARNING*

*These scripts may contain some bugs. Please always control your outputs. Use them at your own risk. You may optimize them to be more compatible with your works. I would be grateful if you could report bugs or problems in the scripts.*


# dataset preparation scripts

### subseting eigen files

subseting eigen dataset with list of population. You must have convertf in the PATH

flags  
  
\-i, --input: prefix of input eigen dataset  
\-o, --output: prefix of output (subsetted) eigen dataset  
\-p, --popfile: a file containing list of populations, one pop per line

example  

```
subset_eigen.py -i dataset_input -p pop_list -o subseted_dataset_output
```
