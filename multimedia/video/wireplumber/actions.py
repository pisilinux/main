#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import mesontools
from pisi.actionsapi import pisitools


def setup():
    mesontools.configure(
        "--buildtype=plain "
        "-D systemd=disabled "
        "-D systemd-system-service=false "
        "-D systemd-user-service=false "
        "-D elogind=disabled "
        "-D system-lua=true"
    )


def build():
    mesontools.build()


def check():
    mesontools.build("test")


def install():

    #shelltools.copytree("%s/usr/share/pkgconfig" % get.installDIR(), "%s/usr/lib/pkgconfig" % get.installDIR())
    #pisitools.removeDir("/usr/share/pkgconfig")
    mesontools.install()
    pisitools.dodoc("LICENSE", "README*")
