
# A vscode remote container docker image with conda from
# https://hub.docker.com/_/microsoft-vscode-devcontainers
FROM mcr.microsoft.com/vscode/devcontainers/miniconda:0-3

RUN conda install -c conda-forge mamba

# specifying dagmc version so all the examples work and no mpi to reduce complexity
RUN mamba install -c conda-forge -y "openmc=0.13.0=dagmc*nompi*"

# Jupyter lab installed to run examples
RUN mamba install -c conda-forge jupyterlab

# downloads ENDF/B-VII.1 from https://openmc.org/official-data-libraries/
RUN wget https://anl.box.com/shared/static/9igk353zpy8fn9ttvtrqgzvw1vtejoz6.xz

# extracts the nuclear data
RUN tar -xf 9igk353zpy8fn9ttvtrqgzvw1vtejoz6.xz

ENV OPENMC_CROSS_SECTIONS=/endfb71_hdf5/cross_sections.xml