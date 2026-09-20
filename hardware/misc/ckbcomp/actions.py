#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import pisitools

def install():
    pisitools.dobin("Keyboard/ckbcomp")
    #pisitools.doman("Keyboard/ckbcomp.1")
