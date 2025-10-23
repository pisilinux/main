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

NoStrip = ["/usr/lib"]

   
def setup():
	autotools.autoreconf("-fiv")
	#shelltools.system("sed '/^#VOXES.*$/d; s/+//g; s/cmu_indic_lex/&\nVOXES = cmu_us_kal16 cmu_us_slt/' config/android.lv >config/pisilinux.lv")
	#shelltools.system("sed -i '/$(INSTALL) -m 755 $(BINDIR)\/flite_time $(DESTDIR)$(INSTALLBINDIR)/d' main/Makefile")
	#shelltools.export("CC", "clang -fuse-ld=lld")
	#shelltools.export("CXX", "clang++ -fuse-ld=lld")
	#shelltools.export("AR", "llvm-ar")
	#shelltools.export("RANLIB", "llvm-ranlib")
	shelltools.export("LDFLAGS", "-lasound -lm")
	autotools.configure("--prefix=/usr \
                         --enable-shared \
                         --with-pic \
                         --with-audio=alsa \
	                     --with-vox=cmu_us_kal16")

def build():
    autotools.make()

def install():
    autotools.install()
    
    #pisitools.remove("/usr/lib/*.a")

    pisitools.dodoc("COPYING", "README*")
