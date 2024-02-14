
# Installation of `hadron`

Information on how to install the [`hadron`](https://github.com/HISKP-LQCD/hadron) library on your machine.
The scripts will install also `R` packages commond in the analysis of ETMC ensembles.

## Package dependencies

- `r-base` `r-base-core` (check that you don't have 2 or more versions installed)
- `libpoppler-cpp-dev`
- `libxml2-dev`
- `libmagick++-dev`
- `openjdk-11-jdk` `openjdk-11-jre`

On your personal machine, you can use `sudo apt-get install`. After the installation run the command:
`sudo R CMD javareconf`.

If working on a cluster, check with your admin how to load the necessary modules first, with e.g. `module load`.

## `python dependencies`

The installation of `hadron` uses `python` scripts parsing the `info.yaml` file. You need to install the following:

```python
pip install pyyaml
```

## `R` dependencies and `hadron`

- `R 4.1` (or above) is required.

- Modify the `info.yaml` file in this directory and run the script `install.py`:

    ```python3
    python3 gen_scripts.py # generation of installation scripts
    ```

- Run the installation scripts (in order):

    ```bash
    bash deps.sh # dependencies (some are unnecessary, but useful for .Rmd files)
    bash hadron_inst.sh # installation
    bash manual.sh # documentation
    ```

## Troubleshooting

If the installation hangs at `"testing if installed package can be loaded"`, 
reinstall R as follows:

1. Run the command `R -e ".libPaths()"` and see which directories contain the R packages.
2. Delete them all and reinstall

