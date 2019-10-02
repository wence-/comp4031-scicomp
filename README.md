# COMP4031 Scientific computing

Durham University Michaelmas term 2019

- Lectures: Mondays 11:00 in E245.
- Office hours: Tuesdays 12:00-13:00 (or via email).

## Running the notebooks

Notebooks from class, with questions to answer and things to try are
in the `material` subdirectory.

To install the necessary software, I recommend doing so in a Python
virtual environment. We need Python3. Doing something like:

```shell
$ python3 -m venv sci-comp
$ . sci-comp/bin/activate # Or other script if you use a different shell
$ pip install numpy scipy pandas ipython jupyter
$ cd path/to/repo/material
$ jupyter notebook
```

Will pop up a browser window.
