from setuptools import setup, find_packages

setup(
    name='pyhadron',
    version='0.1.0',    
    description='A python wrapper for the `R` library `hadron`',
    url='https://github.com/simone-romiti/pyhadron',
    author='Simone Romiti',
    author_email='simone.romiti.1994@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=['rpy2', 'pandas', 'numpy', 'matplotlib', "pyyaml"],
    package_data={"pyhadron": ['info.yaml']},
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: MIT',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 3.4',
    ],
)

