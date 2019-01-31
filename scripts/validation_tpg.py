#! /usr/bin/env python3

# To run use:
# python3 validation_tpg.py --cfg python.user_parameters_cfg.py
# Create a test validation directory at the same level as HGCTPGValidation package, from this new directory run the validation code
# python ../HGCTPGValidation/scripts/validation_tpg.py --cfg HGCTPGValidation.config.user_parameters_cfg.py
    
from datetime import date
import os
import sys
import subprocess
import pprint
import shlex
import time
import glob

from os import environ
from subprocess import Popen, PIPE

sys.path.append('../')
for p in sys.path:
    print(p)

from HGCTPGValidation.hgctpgvalidation.parameters import ConfigFileParameters
from HGCTPGValidation.config.user_parameters_cfg import generate_configFileParameters


def launch_commands(command, logfile):
    print('Subprocess starts')
    sourceCmd = ['bash', '-c', command]
    sourceProc = subprocess.Popen(sourceCmd, stdout=logfile, stderr=logfile)
    (out, err) = sourceProc.communicate() # wait for subprocess to finish
    print('Subprocess finished')
    print (logfile, 'Subprocess finished')
  
# setup Python 2.7 and ROOT 6, call tool to compare histos and create web pages
def launchPlotHistos(parameters, logfile):
    # setup Python 2.7 and ROOT 6
    currentWorkingRefDir = os.getcwd() + '/' + parameters.workingRefDir + '/src'
    currentWorkingTestDir = os.getcwd() + '/' + parameters.workingTestDir + '/src'
    webDir = parameters.webDirPath
    print('currentWorkingRefDir=', currentWorkingRefDir)
    command = '../HGCTPGValidation/scripts/displayHistos.sh ' + currentWorkingRefDir + ' ' + currentWorkingTestDir + ' ' + webDir
    sourceCmd = ['bash', '-c', command]
    subproc = subprocess.Popen(sourceCmd, stdout=logfile, stderr=logfile)
    subproc.communicate()
    print (logfile, 'Finished plot')
    
def main(parameters):
    logfile = open('logfile', 'w')
    # Perform simulation for the reference release
    print('Step 1')
    print (logfile, 'Step 1')
    #configParametersRef = parameters.installWorkingRefDir()
    #launch_commands(configParametersRef, logfile)
    # Perform simulation for the test releases
    print('Step 2')
    #configParametersTest = parameters.installWorkingTestDir()
    #launch_commands(configParametersTest, logfile)
    # Call compare histos and create web pages tool
    print('Step 3')
    launchPlotHistos(parameters, logfile)
    print('Simulation finished!')

if __name__=='__main__':
    import optparse
    import importlib
    itertools = importlib.import_module('itertools')
    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage)
    parser.add_option('--cfg', dest='parameter_file', help='Python file containing the definition of parameters ', default='pars.py')
    parser.add_option('--log', dest='log_file', help='Write log file ', default='log.txt')
    (opt, args) = parser.parse_args()
    current_dir = os.getcwd();
    print('current_dir = ',current_dir)
    sys.path.append(current_dir)
    # Remove the extension of the python file before module loading
    if opt.parameter_file[-3:]=='.py': opt.parameter_file = opt.parameter_file[:-3]
    parameters = importlib.import_module(opt.parameter_file).generate_configFileParameters
    main(parameters)
