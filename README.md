# OR in Python with Cbc & CyLP
This repository contains scripts for the easy installation of the [Cbc solver](https://github.com/coin-or/Cbc) and [CyLP](https://github.com/coin-or/CyLP) into a new `conda` environment. CyLP is a Python interface to COIN-OR’s Linear and mixed-integer program solvers. To use this repository, we will expect you to know how to open Terminal in macOS or Command Prompt or Anaconda Powershell in Windows, and how to use git in the command line.

# Usage
1. Ensure you have git SCM installed.
1. Ensure that you have Anaconda or miniconda installed *and* either:
    1. Added to your `PATH` (Unix-like systems), *OR* 
    1. You have Anaconda Powershell Prompt installed (Windows systems)
1. Clone this repository into your working directory by running the following in your command prompt:
    
    ```git clone https://github.com/christineyong/or-python-xplatform.git```
    
1. Continue to the relevant section below.

## macOS on M1 Macbooks (ARM64 architecture)
1. In your favourite terminal, run `cd or-python-xplatform` to descend into the directory you cloned.
1. Run `bash cfg_macos_arm64.sh`.
1. Re-start your terminal and run `conda activate or_training`.
1. Run `pytest` in the `or-python-xplatform` directory to verify that everything has been installed correctly.

## macOS on Intel Macbooks (x86-64 architecture)
1. In your favourite terminal, run `cd or-python-xplatform` to descend into the directory you cloned.
1. Run `bash cfg_macos_intel.sh`.
1. Re-start your terminal and run `conda activate or_training`.
1. Run `pytest` in the `or-python-xplatform` directory to verify that everything has been installed correctly.

## Linux
Installation on Linux is the simplest, so I have not created the scripts or instructions for installation on this OS.

Please consult the [Cbc solver](https://github.com/coin-or/Cbc) and [CyLP](https://github.com/coin-or/CyLP) GitHub pages for instructions.

## Windows
1. In the Anaconda Powershell Prompt, run `cd or-python-xplatform` to descend into the directory you cloned.
1. Run `.\cfg_win32.bat`. If prompted for a password, press Enter to skip. The `bat` file will download and run the latest COIN-OR installer at the time of writing. Complete the installation using all defaults and click "Yes" to all pop-ups. The script will continue after COIN-OR installation is done.
1. Re-start Anaconda Powershell Prompt and run `conda activate or_training`.
1. Run `pytest` in the `or-python-xplatform` directory to verify that everything has been installed correctly.
