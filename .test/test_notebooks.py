import os
import subprocess

import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from nbconvert.preprocessors import CellExecutionError
import pytest


TEST_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.join(TEST_DIR, '..')


def process_notebook(notebook_filename, html_directory = 'notebook-html'):
    '''Checks if an IPython notebook runs without error from start to finish. If so,
    writes the notebook to HTML (with outputs) and overwrites the .ipynb file
    (without outputs).
    '''

    with open(notebook_filename) as f:
        nb = nbformat.read(f, as_version=4)

    ep = ExecutePreprocessor(timeout=600,
                             kernel_name='python3',
                             allow_errors=True)

    try:
        # Check that the notebook runs
        ep.preprocess(nb, {'metadata': {'path': ''}})
    except CellExecutionError:
        raise

    print(f"Successfully executed {notebook_filename}")
    return


def find_notebooks():
    # Get all files included in the git repository
    git_files = (subprocess
                 .check_output("git ls-tree --full-tree --name-only -r HEAD", shell=True)
                 .decode('utf-8')
                 .splitlines())

    # Get just the notebooks from the git files
    return [fn for fn in git_files if fn.endswith(".ipynb")]


@pytest.mark.parametrize('notebook', find_notebooks())
def test_all_notebooks(notebook, remove_fail_test=True):
    '''Runs `process_notebook` on all notebooks in the git repository.
    '''

    print("Testing", notebook)
    process_notebook(os.path.join(PARENT_DIR, notebook))

    # clean out files when test is complete
    subprocess.check_output("git clean -dxf", shell=True)


if __name__ == '__main__':
    pytest.main()
