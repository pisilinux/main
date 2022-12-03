#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools, pisitools, get

j = ''.join([
    ' --with-aspell',
    ' --with-hunspell',
    ' --with-nuspell',
    ' --with-hspell',
    ' --with-voikko',
    ' --with-zemberek',
    ' --with-hunspell-dir=/usr/share/hunspell',
    ' --with-hspell-dir=/usr/share/hspell',
    ' --with-voikko-dir=/usr/share/voikko',
    ' --disable-static '
    ])

def setup():
    autotools.configure(j)

    #fix unused direct dependency analysis
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.rename("/usr/share/enchant/enchant.ordering", "enchant.ordering-2")
    pisitools.dodoc("AUTHORS", "NEWS")
