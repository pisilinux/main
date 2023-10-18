#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import python3modules
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="blinker-%s" % get.srcVERSION()

def build():
    python3modules.compile()
    
# def check():
    # shelltools.system("nosetests3")

def install():
    python3modules.install()
