#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import pythonmodules, mesontools, pisitools

i = ''.join([
    ' --prefix=/usr',
    ' --with-{boost,bzip2,lzma,sqlite3,zlib}',
    ' --with-python-versions=3.11',
    ' --with-os-feature=getrandom',
    ' --disable-static-library',
    ' --build-tool=ninja',
    ' ',
    ])

def setup():
    pythonmodules.run("configure.py %s" % i, pyVer = "3")

def build():
    mesontools.build("-C .")

def check():
    mesontools.build("-C . check")

def install():
    mesontools.install("-C .")
