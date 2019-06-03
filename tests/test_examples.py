# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 12:10:05 2019

@author: Artesia
"""
import os
import matplotlib.pyplot as plt
import pytest

pathname = 'examples'
# get list of examples to run
files = [f for f in os.listdir(pathname) if f.endswith('.py')]

@pytest.mark.parametrize("file", files)
def test_example(file):
    cwd = os.getcwd()
    
    os.chdir(pathname)
    # TODO: fix example_recharge.py
    if file not in ["example_recharge.py"]:
        try:
            # run each example
            exec(open(file).read())
            plt.close('all')
        except Exception as e:
            os.chdir(cwd)
            msg = 'could not run {}'.format(file)
            raise Exception(msg) from e
    os.chdir(cwd)

if __name__ == '__main__':
    for file in files:
        test_example(file)