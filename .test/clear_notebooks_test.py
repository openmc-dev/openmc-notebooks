import os
import subprocess

import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from nbconvert.preprocessors import CellExecutionError

import pytest
TEST_DIR = os.path.dirname(os.path.abspath(__file__))




def process_notebook(notebook_filename, html_directory = 'notebook-html'):
    '''Checks if an IPython notebook runs without error from start to finish. If so, writes the notebook to HTML (with outputs) and overwrites the .ipynb file (without outputs).
    '''
    with open(notebook_filename) as f:
        nb = nbformat.read(f, as_version=4)
    
    ep = ExecutePreprocessor(timeout=600, kernel_name='python3')

    try:
        # Check that the notebook runs
        ep.preprocess(nb, {'metadata': {'path': ''}})
    except CellExecutionError:
        msg = f'Error executing the notebook {notebook_filename}.\n\n'
        msg += f'See notebook "{notebook_filename}" for the traceback.'
        #print(msg)
        raise
         
    print(f"Successfully executed {notebook_filename}")
    return
    
def test_process_notebook():

    with pytest.raises(CellExecutionError):
        process_notebook(os.path.join(TEST_DIR,'notebook-fails'))

    assert(process_notebook(os.path.join(TEST_DIR,'notebook-pass')) is None)

if __name__ == '__main__':
    test_process_notebook()