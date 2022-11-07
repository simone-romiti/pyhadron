Installation instructions:

1. Install the python dependencies:
    ``` bash
    pip install numpy pandas rpy2
     ```

2. Copy the content of this repository into a custom installation folder, e.g.:

    ```
    cp -vr /path/to/pyhadron/source/* /opt/pyhadron/
    ```

3. Create a file named `hadron_info.py` in the `wrap` folder of the installation directory (e.g. `/opt/pyhadron/wrap`), and inside it declare a variable `lib.loc`:

    ``` python
    # hadron_info.py
    lib_loc = "/path/to/R/hadron/installation/directory/
    ```

Done. You've installed `pyhadron` on your system. 

When importing the library in you python script, make sure you add the path to the installation directory to your `sys.path`.
