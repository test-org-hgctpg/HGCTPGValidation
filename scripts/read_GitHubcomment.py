# This script takes the comment from GitHub and split it into two yaml files.
# The first one is the new configuration yaml
# The second one is the new subsets configuration file
# Usage: python read_GitHubcomment.py --fileGitHub comment.tmp --fileSubset default_multi_subset.yaml

def new_yaml_config(tmpFile, defaultSubsetFile):
    
    # use ruamel.yaml because it keeps the formatting 
    # when using dump function
    from ruamel.yaml import YAML
    yaml = YAML()
    yaml.explicit_start = True
    yaml.preserve_quotes = True  # Optional: preserve quoting style
    yaml.indent(mapping=4, sequence=6, offset=4)
    
    # Read the comment from GitHub
    with open(f"../{tmpFile}", "r") as file:
        config = file.read()
    
    # Remove the ``` at the end of the string
    fc=config.strip("\n```")
    
    # Split the comment in two parts
    # The first contain the new configuration
    # The second contain the subset to add to the set of configurations
    two_fileConfig = fc.split('---', 2)
    _, new_config, new_subset = two_fileConfig
    
    # Get the shortName of the new config
    newConfig = yaml.load(new_config)
    shortName = newConfig.get("shortName")
    
    # Get the name of the new subset file
    newSubsetFile = yaml.load(new_subset)
    newSubsetName = newSubsetFile.get("subsetName")
    newSubsetDescription = newSubsetFile.get("description")
    
    # Get the new couple of subsets
    newSubset = newSubsetFile.get("configuration")
    
    # Get all the configuration defined in default_multi_subset.yaml
    with open(f"../HGCTPGValidation/config/{defaultSubsetFile}", "r") as file:
        defaultConfig = yaml.load(file)
        defaultConfig["subsetName"] = newSubsetName
        defaultConfig["description"] = newSubsetDescription
    
    # Write the new config in a new file
    if shortName:
        with open(f"../HGCTPGValidation/config/{shortName}.yaml", "w") as f:
            yaml.dump(newConfig, f)
    
    # Write the subset file
    if newSubsetName:
        with open(f"../HGCTPGValidation/config/{newSubsetName}.yaml","w") as f:
            yaml.dump(defaultConfig, f)
            yaml.explicit_start = False # Needed in order to not use --- before the new set of configurations
            yaml.dump(newSubset, f)

def main(tmpFile, defaultSubsetFile):
    new_yaml_config(tmpFile, defaultSubsetFile)
    
if __name__ == "__main__":
    import optparse
    import importlib
    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage)
    parser.add_option('--fileGitHub', dest='fileGitHub', help=' ', default='')
    parser.add_option('--fileSubset', dest='fileSubset', help=' ', default='')
    (opt, args) = parser.parse_args()
    
    main(opt.fileGitHub, opt.fileSubset)

