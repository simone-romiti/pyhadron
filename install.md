Installation instructions:

1. Install the python dependencies:
    ``` bash
    pip install numpy pandas rpy2
     ```

2. Copy the content of this repository into a custom installation folder, e.g.:

    ```
    cp -vr /path/to/pyhadron/source/* /opt/pyhadron/
    ```

3. Create a file named `lib_loc.py` in the installation directory (e.g. `/opt/pyhadron/wrap`), and inside it declare a variable `lib.loc`:

    ``` python
    # lib_loc.py
    hadron = "/path/to/R/hadron/installation/directory/
    ```

4. Generate the `Rhadron.py` file, containing the function wrappers. From the installation directory, give:

    ``` bash
    python3 gen_Rhadron.py
    ```

Done. You've installed `pyhadron` on your system. 

When importing the library in you python script, make sure you add the path to the installation directory to your `sys.path`.
