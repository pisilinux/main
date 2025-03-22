#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import mesontools, pisitools, shelltools

y = ''.join([
    ' --prefix=/usr',
    ' --buildtype=release',
    ' -Darchive=enabled',
    ' -Dgps-map=enabled',
    ' -Dgtk4=disabled',
    ' -Dpdf=disabled',
    ' -Ddjvu=disabled',
    ' -Devince=disabled',
    ' -Dgit=disabled',
    ' -Dhelp_pdf=disabled',
    ' -Dpandoc=disabled',
    ' -Dspell=disabled',
    ' -Dyelp-build=disabled',
    ' -Dexecinfo=disabled '
    ])

def setup():
    mesontools.configure(y)

def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.dodoc("COPYING", "NEWS")
    pisitools.dosym("NEWS", "/usr/share/doc/geeqie/ChangeLog")
