#!/usr/bin/python

from pisi.actionsapi import qt5
from pisi.actionsapi import pisitools

def setup():
    qt5.configure()

def build():
    qt5.make()

def install():
    qt5.install()

    pisitools.dodoc("AUTHORS", "README.md")

