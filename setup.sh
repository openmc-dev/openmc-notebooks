#!/usr/bin/env bash
# setup.sh - prepare a conda environment to run the openmc notebooks
# Usage: bash setup.sh

set -euo pipefail
ENV_NAME=openmc-notebooks-env
PY_VER=3.11

echo "Creating conda environment '${ENV_NAME}' with Python ${PY_VER}..."
# Create environment with OpenMC and essentials from conda-forge
conda create -n "${ENV_NAME}" -c conda-forge python=${PY_VER} openmc numpy matplotlib h5py jupyterlab -y

echo "To activate the environment run:"
echo "  conda activate ${ENV_NAME}"

echo "If you prefer pip, after activating a virtualenv run:"
echo "  pip install -r requirements.txt"

echo "Setup complete. Note: OpenMC is best installed through conda-forge for binary compatibility."