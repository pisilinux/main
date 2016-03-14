#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt
from pisi.actionsapi import shelltools
from pisi.actionsapi import perlmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "%s-%s" % (get.srcNAME()[5:], get.srcVERSION())



def build():
    shelltools.system("perl Makefile.PL INSTALLDIRS=vendor")

def check():
    perlmodules.make("test")

def install():
    perlmodules.install(" DESTDIR=${startdir}/pkg")

    pisitools.dodoc("ChangeLog", "README")
