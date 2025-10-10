#!/usr/bin/python
# -*- coding: utf-8 -*-

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import kde5

def setup():
    kde5.configure("-DCMAKE_CXX_STANDARD=17 \
                    -DCMAKE_POLICY_VERSION_MINIMUM=3.5")

def build():
    kde5.make()

def install():
    kde5.install()
