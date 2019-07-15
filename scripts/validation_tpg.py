#! /usr/bin/env python3

# To run use:
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

def checkSubprocessStatus(subProc, logfile):
    if subProc.wait() != 0:
       print('------------------------------------------------------------------------')
       print('=> Execution failed! There were some errors. Please, check the logfile.')
       print('------------------------------------------------------------------------')
       logfile.write('=> Execution failed! There were some errors.\n')
       sys.exit()
    else:
       print('Subprocess completed successfully!')
       logfile.write('=> Subprocess completed successfully!\n')

def launch_commands(command, logfile):
    print('Subprocess starts')
    logfile = open('logfile', 'a+')
    logfile.write('Subprocess starts\n')
    sourceCmd = ['bash', '-c', command]
    sourceProc = subprocess.Popen(sourceCmd, stdout=logfile, stderr=logfile)
    (out, err) = sourceProc.communicate() # wait for subprocess to finish
    checkSubprocessStatus(sourceProc, logfile)
    logfile.close()
    
# setup Python 2.7 and ROOT 6, call tool to compare histos and create web pages
def launchPlotHistos(parameters, logfile):
    # setup Python 2.7 and ROOT 6
    currentWorkingRefDir = os.getcwd() + '/' + parameters.workingRefDir + '/src'
    currentWorkingTestDir = os.getcwd() + '/' + parameters.workingTestDir + '/src'
    webDir = parameters.webDirPath
    print('currentWorkingRefDir=', currentWorkingRefDir)
    command = '../HGCTPGValidation/scripts/displayHistos.sh ' + currentWorkingRefDir + ' ' + currentWorkingTestDir + ' ' + webDir
    sourceCmd = ['bash', '-c', command]
    logfile = open('logfile', 'a+')
    subProc = subprocess.Popen(sourceCmd, stdout=logfile, stderr=logfile)
    subProc.communicate()
    checkSubprocessStatus(subProc, logfile)
    print('Plots were created.')
    #logfile = open('logfile', 'a+')
    #logfile.write('Finished creating plots.')
    logfile.close()
    
def main(parameters):
    logfile = open('logfile', 'w')
    logfile.write('=== Main programme starts!\n')
    logfile.close()

    # Perform simulation for the reference release
    if parameters.validationRef == 'yes':
       print('Simulation with the reference release ', parameters.workingRefDir)
       logfile = open('logfile', 'a+')
       logfile.write('Simulation with the reference release.\n')
       logfile.close()
       # Perform simulation for the reference release
       if parameters.installStep == 'yes':
          print('Start installing working reference directory ', parameters.workingRefDir)
          logfile = open('logfile', 'a+')
          logfile.write('Start installing working reference directory.\n')
          logfile.close()
          configParametersRef = parameters.installWorkingRefDir()
          launch_commands(configParametersRef, logfile)
       else:
          print('Will not perform installStep')
          logfile = open('logfile', 'a+')
          logfile.write('Will not perform installStep.\n')
          logfile.close()
	  
       if parameters.compileStep == 'yes':
          print('Will perform compileStep')
          logfile = open('logfile', 'a+')
          logfile.write('Will perform compileStep.\n')
          logfile.close()
          configParametersRef = parameters.runCompileRefStep()
          launch_commands(configParametersRef, logfile)
       else:
          print('Will not perform compileStep')
          logfile = open('logfile', 'a+')
          logfile.write('Will not perform compileStep.\n')
          logfile.close()
	  
       if parameters.simulationStep == 'yes':
          print('Will perform runSimulationStep')
          logfile = open('logfile', 'a+')
          logfile.write('Will perform runSimulationStep.\n')
          logfile.close()
          configParametersRef = parameters.runSimulationRefStep()
          launch_commands(configParametersRef, logfile)
       else:
          print('Will not perform runSimulationStep')
          logfile = open('logfile', 'a+')
          logfile.write('Will not perform runSimulationStep.\n')
          logfile.close()  	  
    else:
       print('The validation of the reference release will not be performed.')
       logfile = open('logfile', 'a+')
       logfile.write('The validation of the reference release will not be performed!\n')
       logfile.close()
       
    # Perform simulation for the test releases   
    if parameters.validationTest == 'yes':
       print('Simulation with the test release ', parameters.workingTestDir)
       logfile = open('logfile', 'a+')
       logfile.write('Simulation with the test release.\n')
       logfile.close()
       # Perform simulation for the test releases
       if parameters.installStep == 'yes':
          print('Start installing working test directory ', parameters.workingTestDir)
          logfile = open('logfile', 'a+')
          logfile.write('Start installing working test directory.\n')
          logfile.close()  
          configParametersTest = parameters.installWorkingTestDir()
          launch_commands(configParametersTest, logfile)
       else:
          print('Will not perform installStep')
          logfile = open('logfile', 'a+')
          logfile.write('Will not perform installStep.\n')
          logfile.close()

       if parameters.compileStep == 'yes':
          print('Will perform compileStep')
          logfile = open('logfile', 'a+')
          logfile.write('Will perform compileStep.\n')
          logfile.close()
          configParametersTest = parameters.runCompileTestStep()
          launch_commands(configParametersTest, logfile)
       else:
          print('Will not perform compileStep')
          logfile = open('logfile', 'a+')
          logfile.write('Will not perform compileStep.\n')
          logfile.close()

       if parameters.simulationStep == 'yes':
          print('Will perform runSimulationStep')
          logfile = open('logfile', 'a+')
          logfile.write('Will perform runSimulationStep.\n')
          logfile.close()
          configParametersTest = parameters.runSimulationTestStep()
          launch_commands(configParametersTest, logfile)
       else:
          print('Will not perform runSimulationStep')
          logfile = open('logfile', 'a+')
          logfile.write('Will not perform runSimulationStep.\n')
          logfile.close()

    else:
       print('The validation of the test release will not be performed.')
       logfile = open('logfile', 'a+')
       logfile.write('The validation of the test release will not be performed!\n')
       logfile.close()
    
    # Call compare histos and create web pages tool
    print('Compare histos and create web pages tool')
    logfile = open('logfile', 'a+')
    logfile.write('Compare histos and create web pages tool.\n')
    logfile.close()
    launchPlotHistos(parameters, logfile)
    print('Simulation finished!')
    logfile = open('logfile', 'a+')
    logfile.write('Simulation finished!\n')    
    logfile.close()

if __name__=='__main__':
    import optparse
    import importlib
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
