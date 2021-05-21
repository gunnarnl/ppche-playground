import re
import os
import csv

fnameprog = "D:/corpus-work/stanford-tregex/prog-vbgbef.txt"
fnameimpf = "D:/corpus-work/stanford-tregex/impf-vf.txt"
progcsv = "D:/corpus-work/progs.csv"
impfcsv = "D:/corpus-work/impfs.csv"

def composeProgCSV(fname, progcsv):
    with open(fname, 'r', encoding='utf-16-le') as f:
        lines = f.readlines()
        filepaths = lines[::3]
        filenames = stripFN(filepaths)
        vbgs = [l.rstrip() for l in lines[1::3]]
        bes = [l.rstrip() for l in lines[2::3]]
        rows = zip(vbgs, bes, filenames)
        with open(progcsv, 'w') as fc:
            writer = csv.writer(fc)
            for row in rows:
                writer.writerow(row)

def composeImpfCSV(fname, impfcsv):
    with open(fname, 'r', encoding='utf-16-le') as f:
        lines = f.readlines()
        filepaths = lines[::2]
        filenames = stripFN(filepaths)
        impfs = [l.rstrip() for l in lines[1::2]]
        rows = zip(impfs, filenames)
        with open(impfcsv, 'w') as fc:
            writer = csv.writer(fc)
            for row in rows:
                writer.writerow(row)

def stripFN(lines):
    fname = []
    pattern = r'\\([a-z0-9-.]*)\.psd'
    regex = re.compile(pattern)
    for l in lines:
        fname.append(regex.search(l).group(1))
    return fname

composeProgCSV(fnameprog, progcsv)
composeImpfCSV(fnameimpf, impfcsv)
