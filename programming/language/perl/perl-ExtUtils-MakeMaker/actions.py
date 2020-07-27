#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import perlmodules

def setup():
    perlmodules.configure()

def build():
    perlmodules.make()

# tests take long time
#def check():
#    perlmodules.make("test")

def install():
    perlmodules.install()
    # conflict: perl has a binary with the same name
    pisitools.remove("/usr/bin/instmodsh")
    perlmodules.removePodfiles()