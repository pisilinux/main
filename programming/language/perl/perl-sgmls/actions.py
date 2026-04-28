#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import perlmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="SGMLSpm-%s" % get.srcVERSION()

def setup():
    perlmodules.configure("--skipdeps")

def build():
    perlmodules.make()

def check():
    perlmodules.make("test")

def install():
    perlmodules.install()
    shelltools.system("ln -sv /usr/bin/vendor_perl/sgmlspl.pl sgmlspl")

    pisitools.dodoc("README", "COPYING")
