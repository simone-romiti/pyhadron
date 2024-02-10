# dependencies.R

args <- commandArgs(trailingOnly = TRUE)
# Check if at least one argument is provided
if (length(args) < 1) {
  stop("Usage: Rscript myscript.R <local_R_packages_installation_directory>")
}
# Access the first command line argument
R_LIBS <- as.character(path.expand(args[1]))

update.packages(ask = FALSE, checkBuilt = TRUE, lib.loc = R_LIBS)
installed_packages <- installed.packages(lib.loc = R_LIBS)

inst_pkg <- function(name) {
    if (!(name %in% installed_packages)) {
        print(paste("Installing package: ", name))
        install.packages(name, dependencies = TRUE)
    }
}

inst_pkg("devtools")
require("devtools")
inst_pkg("staplr")
inst_pkg("kableExtra")
inst_pkg("errors")
inst_pkg("pander")
inst_pkg("rJava")
inst_pkg("abind")
inst_pkg("dplyr")
inst_pkg("pbmcapply")
inst_pkg("tikzDevice")
inst_pkg("knitr")
inst_pkg("minpack.lm")
inst_pkg("errors")
inst_pkg("boot")
inst_pkg("pdftools")
inst_pkg("ggrepel")
inst_pkg("reshape2")

# this is necessary: see https://github.com/HISKP-LQCD/hadron/issues/308
devtools::install_github('r-lib/cli')

update.packages(ask = FALSE, checkBuilt = TRUE, lib.loc = R_LIBS)