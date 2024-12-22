#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
import os

i = ''.join([
    ' -prefix /usr',
    ' -bindir /usr/bin',
    ' -libdir /usr/lib/ocaml',
    ' -mandir /usr/share/man',
    ' --disable-installing-bytecode-programs '
    ])

def setup():
	autotools.rawConfigure(i)

def build():
	autotools.make("world.opt")

def check():
	autotools.make("ocamltest")
	autotools.make("-C testsuite parallel")

def install():
	destdir = get.installDIR()
	autotools.rawInstall("DESTDIR=%s" % destdir)

	pisitools.remove("/usr/bin/ocamldoc")
	pisitools.dosym("ocamldoc.opt", "/usr/bin/ocamldoc")

	dir__t = "%s/usr/lib/ocaml" % destdir
	for dir__t, dirs, files in os.walk(dir__t):
		for l in files:
			if l.endswith((".cmt", ".cmti", ".ml")):
				shelltools.unlink(os.path.join(dir__t, l))

	pisitools.dodoc("LICENSE")
