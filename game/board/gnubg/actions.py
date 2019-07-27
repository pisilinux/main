#!/usr/bin/env python
#-*- coding:utf-8 -*-

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools


def setup():
	shelltools.system("./autogen.sh")
	autotools.configure("--enable-simd=sse2 -enable-threads --disable-dependency-tracking")

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())
	pisitools.dodoc("ABOUT-NLS","ChangeLog", "COPYING","NEWS","README","TODO")
	pisitools.dosym("/usr/share/fonts/bitstream-vera","/usr/share/gnubg/fonts/bitstream-vera")
	#pisitools.dosym("/usr/share/pixmaps/gnubg-big.png","/usr/share/gnubg/pixmaps/gnubg-big.png")
