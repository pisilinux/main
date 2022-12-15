#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools, pisitools

def setup():
	shelltools.cd("dictionaries")
	shelltools.system("rename -v - _ *")
	for t in shelltools.ls("*"):
		shelltools.system("find %s -type f -iname 'index*' | sed -e 'p;s:index:%s:' | xargs -n2 mv" % (t, t))
		shelltools.system("find %s -type f -exec chmod 0644 {} \;" % t)

def install():
	shelltools.cd("dictionaries")
	for t in shelltools.ls("*"):
		pisitools.insinto("/usr/share/hunspell", "%s/%s.dic" % (t, t))
		pisitools.insinto("/usr/share/hunspell", "%s/%s.aff" % (t, t))
