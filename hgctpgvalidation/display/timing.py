#######################################################################################################################
# Read a file with the information from MemoryCheck and Time and fill corresponding histo (Nbr/Time/event)
# for each producer HGCalVFEProducer, HGCalConcentratorProducer, HGCalBackendLayer1Producer, HGCalBackendLayer2Producer,
# HGCalTowerMapProducer and HGCalTowerProducer

import os
import sys

from ROOT import TCanvas, TFile, TProfile, TNtuple, TH1F, TH2F
from ROOT import gROOT, gBenchmark, gRandom, gSystem, Double

def readFileStatement(logfile):
    print('1 name = ', logfile)
    # Remove the extension .txt of logfile
    rootFileName = logfile[:-3] + 'root'
    hFile = TFile( rootFileName, 'RECREATE', 'Check timer histograms' )
    hVFE = TH1F( 'hVFE', 'HGCalVFEProducer: Time/event distribution', 1000, 0, 1.5 )
    hConc = TH1F( 'hConc', 'HGCalConcentratorProducer: Time/event distribution', 1000, 0, 0.5 )
    hBackendL1 = TH1F( 'hBackendL1', 'HGCalBackendLayer1Producer: Time/event distribution', 1000, 0, 1.5 )
    hBackendL2 = TH1F( 'hBackendL2', 'HGCalBackendLayer2Producer: Time/event distribution', 1000, 0, 0.5 )
    hTowerMap = TH1F( 'hTowerMap', 'HGCalTowerMapProducer: Time/event distribution', 1000, 0, 0.5 )
    hTower = TH1F( 'hTower', 'HGCalTowerProducer: Time/event distribution', 1000, 0, 0.5 )
    # list of histograms
    listHistos = [hVFE, hConc, hBackendL1, hBackendL2, hTowerMap, hTower]

    # list containing all name if producers
    listProducers=['HGCalVFEProducer', 'HGCalConcentratorProducer','HGCalBackendLayer1Producer','HGCalBackendLayer2Producer', 'HGCalTowerMapProducer','HGCalTowerProducer']
 
    with open(logfile) as file:
        data = file.readlines()
        for line in data:
            words=line.split()
            #print("line = ", words[4], words[5])
            for i in range(len(listProducers)):
                if words[4]==listProducers[i]:
                    print("Fill ", i, words[5], listProducers[i])
                    listHistos[i].Fill(float(words[5]))

    hFile.Write()

def main(reffile, testfile):
    print("Read file!")
    readFileStatement(reffile)
    readFileStatement(testfile)
  
if __name__== "__main__":
    import optparse
    import importlib
    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage)
    parser.add_option('--reffile', dest='reffile', help=' ', default='')
    parser.add_option('--testfile', dest='testfile', help=' ', default='')
    (opt, args) = parser.parse_args()

    main(opt.reffile, opt.testfile)
