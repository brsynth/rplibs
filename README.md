# rplibs

Libraries for rpTools, contains:
* rpSBML
* inchikeyMIRIAM
* rpPathway, rpReaction, rpCompound (inheritance from [chemlite](https://github.com/brsynth/chemlite))

## rpSBML
Defines an enriched SBML structure with additional fields relative to [RetroPath2](https://github.com/brsynth/RetroPath2-wrapper) objects.


## Install
```sh
[sudo] conda install -c conda-forge rplibs
```

### Test
```
python -m pytest tests
```

### Merging
rpSBML class allows the merging between two rpSBML objects. This method is using to integrate an heterologu pathway within a model.

#### Compartments
The compartment of the pathway to each compartment of the model. The comparison is done by ID, name or MIRIAM annotations. If a model compartment matches, then we rename the compartment of each species of the pathway to the name of the model matched compartment. Otherwise, the pathway compartment is added to the model.

## inchikeyMIRIAM
Uses the rrCache to parse an SBML file to find all the chemical species, and try to recover the inchikey and add it to the MIRIAM annotation.

## Statisticis
To print statistics on pathways, type:
```
python -m rplibs.stats --pathways <Pathway_1> <Pathway_2>
```

## Authors

* **Melchior du Lac**
* **Joan Hérisson**

## Acknowledgments

* Thomas Duigou


## Licence
rplibs is released under the MIT licence. See the LICENCE file for details.
