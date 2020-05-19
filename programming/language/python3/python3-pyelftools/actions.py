#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules

def build():
    pythonmodules.compile(pyVer="3")
    
def check():
    pythonmodules.run("test/run_all_unittests.py",pyVer="3")
    pythonmodules.run("test/run_examples_test.py",pyVer="3")

def install():
    pythonmodules.install(pyVer="3")