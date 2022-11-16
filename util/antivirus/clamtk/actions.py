#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools, pisitools

def install():
	for lib in shelltools.ls("lib/*"):
		shelltools.chmod(lib, mode = 0644)
		pisitools.insinto("/usr/lib/perl5/vendor_perl/5.32.0/ClamTk", lib)

	for mo in shelltools.ls("po/*.po"):
		shelltools.chmod(lib, mode = 0644)
		pisitools.domo(mo, shelltools.baseName(mo).replace(".po", ""), "clamtk.mo")

	pisitools.dobin("clamtk")
	pisitools.insinto("/usr/share/applications", "clamtk.desktop")
	pisitools.dopixmaps("images/*")
	pisitools.doman("clamtk.1.gz")

	pisitools.insinto("/usr/share/appdata", "com.github.davetheunsub.clamtk.appdata.xml")
