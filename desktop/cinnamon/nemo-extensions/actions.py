#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import get, mesontools, pisitools, pythonmodules, shelltools
#nemo-seahorse
pkgs_meson = "nemo-python nemo-dropbox nemo-fileroller nemo-image-converter nemo-preview nemo-repairer nemo-share nemo-seahorse".split()

pkgs_python = "nemo-audio-tab nemo-compare nemo-emblems nemo-media-columns nemo-pastebin nemo-terminal".split()
def setup():
    for i in pkgs_meson:
        shelltools.cd(i)
        mesontools.configure("--libexecdir=/usr/share/%s" % i)
        shelltools.cd("..")

def build():
    for i in pkgs_meson:
        shelltools.cd(i)
        mesontools.build()
        shelltools.cd("..")
    
    for i in pkgs_python:
        shelltools.cd(i)
        pythonmodules.compile(pyVer = '3')
        shelltools.cd("..")

def install():
    for i in pkgs_meson:
        shelltools.cd(i)
        mesontools.install()
        shelltools.cd("..")

    for i in pkgs_python:
        shelltools.cd(i)
        pythonmodules.install(pyVer = '3')
        shelltools.cd("..")
    pisitools.removeDir("/usr/share/doc")
    pisitools.removeDir("/usr/lib/pkgconfig")
