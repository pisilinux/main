#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import mesontools, pisitools

i = ''.join([
    ' --prefix=/usr',
    ' -Denable-apport=false',
    ' -Denable-dbusmenu=yes',
    ' -Dproduction_release=true',
    ' -Denable-docs=false '
    ])

def setup():
	mesontools.configure(i)

def build():
	mesontools.build()

def install():
	mesontools.install()

	pisitools.dodoc("AUTHORS", "COPYING", "COPYRIGHT")
