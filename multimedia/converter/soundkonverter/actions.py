#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import kde5
from pisi.actionsapi import pisitools

def setup():
    kde5.configure()

def build():
    kde5.make()

def install():
    kde5.install()

    pisitools.dodoc("CHANGELOG", "INSTALL", "README")