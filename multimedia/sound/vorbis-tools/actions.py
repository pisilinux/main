#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

j = ''.join([
    ' --enable-nls',
    ' --enable-vcut',
    ' --enable-ogg123',
    ' --with-flac',
    ' --with-kate',
    ' --with-speex',
    ' --docdir=/%s/%s' % (get.docDIR(), get.srcNAME())
    ])

def setup():
    autotools.configure(j)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/usr/share/doc")

    pisitools.dodoc("CHANGES", "COPYING", "AUTHORS", "README", "ogg123/ogg123rc-example")
