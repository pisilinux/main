#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools, cmaketools, mesontools

subdirs = ["libyui",
           "libyui-bindings",
           "libyui-ncurses",
           "libyui-qt",
           "libyui-qt-graph"]

setupopt = ''.join([
           ' -DBUILD_SRC=ON',
           ' -DBUILD_DOC=ON',
           ' -DWERROR=OFF',
           ' -DWITH_MGA=OFF',
           ' -Bbuild -G Ninja -L '
           ])

def setup():
    for subdir in (tuple(subdirs)):
        shelltools.cd(subdir)
        cmaketools.configure(setupopt)
        shelltool.cd("..")

def build():
    for subdir in (tuple(subdirs)):
        shelltools.cd(subdir)
        mesontools.build()
        shelltools.cd("..")

def install():
    for subdir in (tuple(subdirs)):
        shelltools.cd(subdir)
        mesontools.install()
        shelltools.cd("..")
