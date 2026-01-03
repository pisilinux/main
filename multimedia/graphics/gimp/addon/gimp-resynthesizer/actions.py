#!/usr/bin/python
# -*- coding: utf-8 -*-


from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import mesontools
from pisi.actionsapi import get


# WorkDir = "resynthesizer-0.16"

def setup():
	mesontools.configure()

def build():
	mesontools.build()

def install():
	mesontools.install()

	# pisitools.insinto("/usr/share/gimp/2.0/scripts","smart-enlarge.scm")
	# pisitools.insinto("/usr/share/gimp/2.0/scripts","smart-remove.scm")
	# pisitools.insinto("/usr/lib/gimp/2.0/plug-ins","resynth")
	pisitools.dodoc("COPYING","README*")
