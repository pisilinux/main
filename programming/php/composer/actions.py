#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

def setup():
    pass

def build():
    pass

def install():
    pisitools.insinto("/usr/bin", "composer.phar", "composer")
    #shelltools.chmod("/usr/bin/composer", mode=0o755)