#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import python3modules

def setup():
    python3modules.compile()

def build():
    python3modules.build()

def install():
    python3modules.install()

    # Optional: Install license and readme if they are in standard locations
    # pisitools.dodoc("LICENSE", "README.md")
