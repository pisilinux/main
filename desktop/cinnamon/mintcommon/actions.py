#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file https://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get, pisitools

def setup():
    pass

def build():
    pass

def install():
    pisitools.insinto("/usr","%s/%s-%s/usr/*" % (get.workDIR(), get.srcNAME(), get.srcVERSION()))
