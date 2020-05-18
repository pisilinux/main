# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
import glob

def setup():
    pisitools.dosed("setup.py", "etc/bash_completion.d", "../etc/bash_completion.d")
    pisitools.dosed("setup.py", "etc/fish/completions", "../etc/fish/completions")

def install():
    pythonmodules.install(pyVer = "3")