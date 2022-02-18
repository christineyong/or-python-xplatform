# OR in Python with Cbc & CyLP
This repository contains scripts for the easy installation of the [Cbc solver](https://github.com/coin-or/Cbc) and [CyLP](https://github.com/coin-or/CyLP) into a new `conda` environment. CyLP is a Python interface to COIN-OR’s Linear and mixed-integer program solvers.

# Usage
1. Ensure that you have Anaconda or miniconda installed *and* either:
    1. Added to your `PATH` (Unix-like systems), *OR* 
    1. You have Anaconda Prompt installed (Windows systems)
1. Clone this repository by running the following in your command prompt:
    
    ```git clone https://github.com/christineyong/or-python-xplatform.git```
    
1. Descend into the `or-python-xplatform` directory you cloned.  
1. Continue to the relevant section below.

## macOS on M1 Macbooks (ARM64 architecture)
1. In your favourite terminal, run `bash cfg_macos_arm64.sh`.
1. Re-start your terminal and run `conda activate or_training`
1. Run `pytest` to verify that everything has been installed correctly.

## macOS on Intel Macbooks (x86-64 architecture)
1. In your favourite terminal, run `bash cfg_macos_intel.sh`.
1. Re-start your terminal and run `conda activate or_training`
1. Run `pytest` to verify that everything has been installed correctly.

## Windows
Currently under testing.

## Linux
Currently under testing.
