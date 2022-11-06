# import this module to get access to hadron

from rpy2.robjects.packages import importr
import hadron_info

importr("hadron", lib_loc = hadron_info.lib_loc)
