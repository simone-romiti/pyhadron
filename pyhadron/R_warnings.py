
import rpy2

def disable():
    rpy2.rinterface_lib.callbacks.logger.setLevel(50)  # 50 suppresses all warnings
####

def enable():
    rpy2.rinterface_lib.callbacks.logger.setLevel(30)  # 30 resets to the default warning behavior
####