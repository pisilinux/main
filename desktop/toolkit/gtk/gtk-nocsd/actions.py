#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools, get

i = ''.join([
    ' PREFIX=/usr',
    ' LIBDIR=/usr/lib',
    ' LICENSEDIR=%s' % get.docDIR(),
    ' NOOPT=1',
    ' NODOC=1 '
    ])

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s %s" % (get.installDIR(), i))
