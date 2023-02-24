#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import pisitools

def install():
	pisitools.dobin("bin/pandoc")
	pisitools.dosym("pandoc", "/usr/bin/pandoc-lua")
	pisitools.dosym("pandoc", "/usr/bin/pandoc-server")

	pisitools.doman("share/man/man1/pandoc.1.gz")
	pisitools.doman("share/man/man1/pandoc-lua.1.gz")
	pisitools.doman("share/man/man1/pandoc-server.1.gz")
