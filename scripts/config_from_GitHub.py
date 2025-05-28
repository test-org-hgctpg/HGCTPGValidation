# This script takes the configuration yaml from the PR comment in GitHub
# and create a new configuration file
# Usage: config_from_GitHub.py --subconfig

import sys
from ruamel.yaml import YAML
from parse_parameters_re import parse_parameters

def new_yaml_config(updates):
    yaml = YAML()
    yaml.explicit_start = True
    yaml.preserve_quotes = True  # Optional: preserve quoting style
    
    index = updates.index("shortName")
    newConfig = updates[index:]
    
    config = yaml.load(newConfig)
    fileName = f'{config["shortName"]}.yaml'
    yaml.dump(config, sys.stdout)
    with open(../HGCTPGValidation/config/fileName, "w") as f:
        yaml.dump(config, f)

def main(subconfig):
    new_yaml_config(subconfig)

if __name__ == "__main__":
    import optparse
    import importlib
    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage)
    parser.add_option('--subconfig', dest='subconfig', help=' ', default='')
    (opt, args) = parser.parse_args()
   
    main(opt.subconfig)
