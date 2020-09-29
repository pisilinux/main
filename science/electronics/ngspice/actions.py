# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools

def setup():
    options_cfg = ''.join([
                  '--prefix=/usr ',
                  '--enable-cider ',
                  '--enable-openmp ',
                  '--enable-xspice ',
                  '--with-ngshared ',
                  '--enable-oldapps ',
                  '--with-readline=yes ',
                  '--mandir=/usr/share/man ',
                  ])
    autotools.configure("%s" % options_cfg)
    
    # fix unused direct dependency analysis
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("COPYING", "README*")
