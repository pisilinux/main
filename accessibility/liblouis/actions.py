#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools


def setup():
    autotools.configure(
        "--prefix=/usr "
        "--enable-ucs4 "
        "--disable-static"
    )


def build():
    autotools.make()


def install():
    autotools.rawInstall(
        "DESTDIR=%s" % get.installDIR()
    )

    pisitools.dodoc(
        "AUTHORS",
        "COPYING",
        "COPYING.LESSER"
    )
