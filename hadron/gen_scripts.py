import yaml
import os
import subprocess


yaml_file_path = "info.yaml"

with open(yaml_file_path, "r") as yaml_file:
    nd = yaml.safe_load(yaml_file)
####

src_dir = nd["src_dir"]+"hadron_github"
inst_dir = nd["inst_dir"]
R_LIBS_USER = nd["R_LIBS_USER"]

if(inst_dir == "" or R_LIBS_USER==""):
    raise ValueError("Invalid installation path: \"{inst_dir}\"".format(inst_dir=inst_dir))
####

src_dir = os.path.abspath(os.path.expanduser(src_dir))
inst_dir = os.path.abspath(os.path.expanduser(inst_dir))
R_LIBS_USER = os.path.abspath(os.path.expanduser(R_LIBS_USER))

cmd1 = """Rscript ./dependencies.R {R_LIBS_USER}""".format(R_LIBS_USER=R_LIBS_USER)

with open('deps.sh', 'w') as deps:
    deps.write(cmd1)
####

cmd2 = """
# cloning the repository

mkdir -p {src_dir}/
git clone https://github.com/HISKP-LQCD/hadron {src_dir}/

cd {src_dir}/

old_R_LIBS=$(echo $R_LIBS) # saving previous value
export R_LIBS={inst_dir}/
./install # installing hadron
export R_LIBS=$old_R_LIBS # restoring the old value

""".format(src_dir=src_dir, inst_dir=inst_dir)

with open('hadron_inst.sh', 'w') as hadron_inst:
    hadron_inst.write(cmd2)
####

cmd3 = """
# generate pdf documentation    
Rscript -e "devtools::build_manual(pkg=\\"{src_dir}\\", path=\\"{inst_dir}\\")"

""".format(src_dir=src_dir, inst_dir=inst_dir)

with open('manual.sh', 'w') as manual:
    manual.write(cmd3)
####


if nd["clean_up"]:
    cmd4 = """
    # cleaning up
    rm -rf {src_dir} 
    rm deps.sh hadron_inst.sh manual.sh

    """.format(src_dir=src_dir)

    with open('clean_up.sh', 'w') as clean_up:
        clean_up.write(cmd4)
    ####
####




