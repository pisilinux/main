#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools, get

j = ''.join([
    ' VERBOSE=true',
    ' QUIET=true',
    ' STRIP=true',
    ' ARCH=x86_64 '
    ])

def build():
    autotools.make(j)

def install():
    autotools.rawInstall("DESTDIR=%s PREFIX=/usr" % get.installDIR())
