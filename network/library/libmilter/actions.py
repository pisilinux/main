#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools, pisitools, get

so = "MILTER_SOVER=1.0.2"
j = ''.join([
    ' INCOWN=root INCGRP=root INCMODE=644',
    ' LIBOWN=root LIBGRP=root LIBMODE=644 UBINMODE=755 '
    ])

def setup():
	pass

def build():
	autotools.make("-C libmilter %s" % so)

def install():
	pisitools.dodir("/usr/lib")
	autotools.rawInstall("-C libmilter DESTDIR=%s %s %s install" % (get.installDIR(), j, so))
