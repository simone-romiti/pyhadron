import yaml
import os
import subprocess


yaml_file_path = "info.yaml"

with open(yaml_file_path, "r") as yaml_file:
    nd = yaml.safe_load(yaml_file)
####

hadron_src_dir = nd["hadron_src_dir"]+"hadron_github"
hadron_inst_dir = nd["hadron_inst_dir"]
R_LIBS_USER = nd["R_LIBS_USER"]

if(hadron_inst_dir == ""):
    raise ValueError("Invalid installation path: \"{hadron_inst_dir}\"".format(hadron_inst_dir=hadron_inst_dir))
####
elif(R_LIBS_USER==""):
    raise ValueError("Invalid R packages installation path: \"{R_LIBS_USER}\"".format(R_LIBS_USER=R_LIBS_USER))
####

hadron_src_dir = os.path.abspath(os.path.expanduser(hadron_src_dir))
hadron_inst_dir = os.path.abspath(os.path.expanduser(hadron_inst_dir))
R_LIBS_USER = os.path.abspath(os.path.expanduser(R_LIBS_USER))

cmd1 = """Rscript ./dependencies.R {R_LIBS_USER}""".format(R_LIBS_USER=R_LIBS_USER)

with open('deps.sh', 'w') as deps:
    deps.write(cmd1)
####

cmd2 = """
# cloning the repository

mkdir -p {hadron_src_dir}/
git clone https://github.com/HISKP-LQCD/hadron {hadron_src_dir}/

cd {hadron_src_dir}/

old_R_LIBS=$(echo $R_LIBS) # saving previous value
export R_LIBS={hadron_inst_dir}/
./install # installing hadron
export R_LIBS=$old_R_LIBS # restoring the old value

""".format(hadron_src_dir=hadron_src_dir, hadron_inst_dir=hadron_inst_dir)

with open('hadron_inst.sh', 'w') as hadron_inst:
    hadron_inst.write(cmd2)
####

cmd3 = """
# generate pdf documentation    
Rscript -e "devtools::build_manual(pkg=\\"{hadron_src_dir}\\", path=\\"{hadron_inst_dir}\\")"

""".format(hadron_src_dir=hadron_src_dir, hadron_inst_dir=hadron_inst_dir)

with open('manual.sh', 'w') as manual:
    manual.write(cmd3)
####


if nd["clean_up"]:
    cmd4 = """
    # cleaning up
    rm -rf {hadron_src_dir} 
    rm deps.sh hadron_inst.sh manual.sh clean_up.sh

    """.format(hadron_src_dir=hadron_src_dir)

    with open('clean_up.sh', 'w') as clean_up:
        clean_up.write(cmd4)
    ####
####




