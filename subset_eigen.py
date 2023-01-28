#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 23:21:59 2019

@author: pijacek
"""
import subprocess
import argparse
parser = argparse.ArgumentParser(
    description='subset eigen dataset with list of population. You must have convertf in the PATH')
parser.add_argument('-i', '--input', help="prefix of input eigen dataset")
parser.add_argument('-o', '--output', help="prefix of output (subsetted) eigen dataset")
parser.add_argument('-p', '--popfile', help="a file containing list of populations, one pop per line")

args = parser.parse_args()

# assign variables

infile =  args.input
outfile = args.output
popfile = args.popfile
parfile ="par_subset_{}_to_{}".format(infile,outfile)

# create parfile

with open(parfile,"w") as outpar:
    outpar.write("genotypename: {}.geno".format(infile) + "\n")
    outpar.write("snpname: {}.snp".format(infile) + "\n")
    outpar.write("indivname: {}.ind".format(infile) + "\n")
    outpar.write("outputformat:  EIGENSTRAT" + "\n")
    outpar.write("genotypeoutname: {}.geno".format(outfile) + "\n")
    outpar.write("snpoutname: {}.snp".format(outfile) + "\n")
    outpar.write("indivoutname: {}.ind".format(outfile) + "\n")
    outpar.write("poplistname:  {}".format(popfile))


# run convertf
subprocess.call("convertf -p {0} &> log_{0} &".format(parfile), shell=True)
