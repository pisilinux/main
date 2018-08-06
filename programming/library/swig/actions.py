#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.system("sed -i 's/\$(PERL5_SCRIPT/-I. &/' Examples/Makefile.in")
    shelltools.system("sed -i 's/\$command 2/-I. &/' Examples/test-suite/perl5/run-perl-test.pl")
    autotools.configure("--without-clisp \
                         --without-maximum-compile-warnings")

def build():
    autotools.make()
    
def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("ANNOUNCE", "CHANGES*", "LICENSE", "README", "TODO")
