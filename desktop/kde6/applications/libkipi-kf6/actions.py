#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import kde6

def setup():
    kde6.configure("-DBUILD_TESTING=OFF")

def build():
    kde6.make()

def install():
    kde6.install()
