""""
Sample_code
"""
import os
from prev import sample


def conda_mk_virtual_env():
    assert sample.mk_virtual_env in {"conda create -n deepsales python=3.8", "conda create -n deepsales python==3.8", 
                                    'conda create -n "deepsales" python=3.8', 'conda create -n "deepsales" python==3.8',
                                    "conda create --name 'deepsales' python=3.8","conda create --name deepsales python=3.8",
                                    "conda create --name 'deepsales' python==3.8","conda create --name deepsales python==3.8"
                                    }

def conda_activate_virtual_env():
    assert sample.activate_virtual_env == "conda activate deepsales"

def conda_virtual_env_list():
    assert sample.virtual_env_list == "conda env list"

