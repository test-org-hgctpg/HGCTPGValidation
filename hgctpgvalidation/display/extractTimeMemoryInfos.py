# Extract Memory Check information and global Time information
# This program is called in HGCTPGValidation/scripts/displayHistos.sh
# python ../HGCTPGValidation/hgctpgvalidation/display/extractTimeMemoryInfos.py --reffile out_ref.log --testfile out_test.log --refdir $1 --testdir $2
# where $1 and $2 are the directories for ref and test releases.

import os
import sys
from itertools import islice

def extractInfos(namefile, dirname):
    # Output file MemoryReport_ref.log or MemoryReport_test.log
    indicator = namefile.split("_")
    outputfile = "MemoryReport_" + indicator[1]

    # Input file out_ref.log or out_test.log
    nfile = dirname + '/' + namefile
    # Number of lifes to be read starting from the line " Time Summary:"
    number_of_lines = 18
    # Open the file to read
    with open(nfile) as f:
        # Open the file to fill with the extracted information
        with open(outputfile, "a+") as f1:
            for line in f:
                # Read Memory report information
                if "MemoryReport>" in line:
                    f1.writelines(line)
                # Read Time summary information
                if " Time Summary:" in line:
                    f1.writelines(line)
                    # Read 18 lines starting from " Time Summary:"
                    lines_cache = islice(f, number_of_lines)
                    for current_line in lines_cache:
                        f1.write(current_line)

def main(reffile, testfile, refdir, testdir):
    print(reffile, testfile)
    extractInfos(reffile, refdir)
    extractInfos(testfile, testdir)

if __name__== "__main__":
    import optparse
    import importlib
    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage)
    parser.add_option('--reffile', dest='reffile', help=' ', default='')
    parser.add_option('--testfile', dest='testfile', help=' ', default='')
    parser.add_option('--refdir', dest='refdir', help=' ', default='')
    parser.add_option('--testdir', dest='testdir', help=' ', default='')
    (opt, args) = parser.parse_args()

    main(opt.reffile, opt.testfile, opt.refdir, opt.testdir)
