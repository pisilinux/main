#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.export("PYTHON", "/usr/bin/python3")
    shelltools.system("sed -i 's/\$(PERL5_SCRIPT/-I. &/' Examples/Makefile.in")
    shelltools.system("sed -i 's/\$command 2/-I. &/' Examples/test-suite/perl5/run-perl-test.pl")
    shelltools.system("NOCONFIGURE=1 ./autogen.sh")
    autotools.configure("--without-clisp \
                         --with-python3 \
                         --without-maximum-compile-warnings")
    #autotools.configure("--prefix=/usr")

def build():
    autotools.make()

# too much dependency to test
#def check():
#    shelltools.system("make check || warning 'Tests failed'")
    
def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("LICENSE*", "README")
