#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import mesontools, pisitools

y = ''.join([
    ' --prefix=/usr',
    ' --buildtype=debugoptimized',
    ' -Dpdf=disabled',
    ' -Ddjvu=disabled',
    ' -Ddoxygen=disabled',
    ' -Dgit=disabled',
    ' -Dhelp_pdf=disabled',
    ' -Dpandoc=disabled',
    ' -Dspell=disabled',
    ' -Dyelp-build=disabled '
    ])

def setup():
    mesontools.configure(y)

def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.dodoc("COPYING", "NEWS")
    pisitools.dosym("NEWS", "/usr/share/doc/geeqie/ChangeLog")
