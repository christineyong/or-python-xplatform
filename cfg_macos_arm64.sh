CONDA_SUBDIR=osx-64 conda create -n or_training
conda activate or_training
conda env config vars set CONDA_SUBDIR=osx-64  # subsequent commands use intel packages
conda env update --file environment.yml --prune
echo "Re-start your shell and run 'conda activate or_training' to use CyLP and Cbc"