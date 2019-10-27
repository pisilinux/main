#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

#WorkDir = "flite-%s-current" % get.srcVERSION()
   
def setup():
	#shelltools.system("sed '/^#VOXES.*$/d; s/+//g; s/cmu_indic_lex/&\nVOXES = cmu_us_kal16 cmu_us_slt/' config/android.lv >config/pisilinux.lv")
	#shelltools.system("sed -i '/$(INSTALL) -m 755 $(BINDIR)\/flite_time $(DESTDIR)$(INSTALLBINDIR)/d' main/Makefile")
	shelltools.export("LDFLAGS", "-lasound -lm")
	autotools.configure("--prefix=/usr \
						 --with-audio=alsa \
	                     --with-vox=cmu_us_kal16")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("COPYING", "README.md")
