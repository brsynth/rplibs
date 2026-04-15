# rplibs

rpLibs, contains:
* rpSBML
* inchikeyMIRIAM
* rpPathway, rpReaction, rpCompound (inheritance from [chemlite](https://github.com/brsynth/chemlite))

## rpSBML
Defines an enriched SBML structure with additional fields relative to [RetroPath2](https://github.com/brsynth/RetroPath2-wrapper) objects.


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


# Installation Guide

## Overview

`rplibs` depends on `cobra`, which requires `python-libsbml`.  
On Apple Silicon (`arm64`) macOS, `python-libsbml` is not available as a native Conda package.

Therefore, installation must be done using an **Intel (`osx-64`) Conda environment under Rosetta**.

---

## General case
```bash
conda install -c conda-forge rplibs
```

---

## Apple Silicon macOS (M1/M2/M3)

### 1. Install Rosetta 2

```bash
softwareupdate --install-rosetta --agree-to-license
```

### 2. Install

```bash
CONDA_SUBDIR=osx-64 conda install -c conda-forge rplibs
```

Or with mamba:

```bash
CONDA_SUBDIR=osx-64 mamba install -c conda-forge rplibs
```

### 3. Persist platform setting

```bash
conda config --env --set subdir osx-64
```

### 4. Verify installation

```bash
python -c "import rplibs; print('rplibs installed successfully')"
```

### 5. (Optional) Dev installation

```bash
CONDA_SUBDIR=osx-64 conda env create -f environment.yaml
```

---

## Troubleshooting

### Solver fails on Apple Silicon

Make sure you are using:

```bash
CONDA_SUBDIR=osx-64
```

### Wrong architecture environment

Check:

```bash
conda config --show subdir
```

Expected output:

```bash
subdir: osx-64
```

### Test
```
python -m pytest tests
```
```

## Authors

* **Joan Hérisson**
* **Melchior du Lac**

## Acknowledgments

* Thomas Duigou


## Licence
rplibs is released under the MIT licence. See the LICENCE file for details.
