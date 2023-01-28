#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 23:21:59 2019

@author: pijacek
"""
import subprocess
import argparse
parser = argparse.ArgumentParser(
    description='merge eigen datasets. You must have convertf in the PATH')
parser.add_argument('-i1', '--input1', help="prefix of input eigen dataset")
parser.add_argument('-i2', '--input2', help="prefix of input eigen dataset")
parser.add_argument('-o', '--output', help="prefix of output (subsetted) eigen dataset")
#parser.add_argument('-p', '--popfile', help="a file containing list of populations, one pop per line")

args = parser.parse_args()

# assign variables

infile1 =  args.input1
infile2 =  args.input2
outfile = args.output
#popfile = args.popfile
parfile ="par_merge_{}_a_{}_to_{}".format(infile1,infile2,outfile)

# create parfile

with open(parfile,"w") as outpar:
    outpar.write("geno1: {}.geno".format(infile1) + "\n")
    outpar.write("snp1: {}.snp".format(infile1) + "\n")
    outpar.write("ind1: {}.ind".format(infile1) + "\n")
    outpar.write("geno2: {}.geno".format(infile2) + "\n")
    outpar.write("snp2: {}.snp".format(infile2) + "\n")
    outpar.write("ind2: {}.ind".format(infile2) + "\n")
    outpar.write("outputformat:  EIGENSTRAT" + "\n")
    outpar.write("genooutfilename: {}.geno".format(outfile) + "\n")
    outpar.write("snpoutfilename: {}.snp".format(outfile) + "\n")
    outpar.write("indoutfilename: {}.ind".format(outfile) + "\n")
    outpar.write("docheck:  YES" + "\n")
    outpar.write("hashcheck:  YES" + "\n")



# run convertf
subprocess.call("mergeit -p {0} &> log_{0} &".format(parfile), shell=True)
