#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools


def setup():
    autotools.configure("--prefix=/usr \
                        --libexecdir=/usr/lib \
                        --sbindir=/usr/bin \
                        --mandir=/usr/share/man \
                        --docdir=/usr/share/doc/dosfstools \
                        --enable-compat-symlinks")

def build():
    #autotools.autoreconf("--enable-compat-symlinks")
    autotools.make()

def install():
    autotools.install()
