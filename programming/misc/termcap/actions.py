#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools, pisitools

i = ''.join([
    ' -DHAVE_STRING_H=1',
    ' -DHAVE_UNISTD_H=1',
    ' -DSTDC_HEADERS=1 '
    ])

def build():
	shelltools.system("gcc -fPIC -c termcap.c %s" % i)
	shelltools.system("gcc -fPIC -c tparam.c %s" % i)
	shelltools.system("gcc -fPIC -c version.c %s" % i)
	shelltools.system("gcc -shared -Wl,-soname,'libtermcap.so' -o 'libtermcap.so.1.3.1' 'termcap.o' tparam.o version.o")

def install():
	pisitools.dolib_so("libtermcap.so.1.3.1")
	pisitools.dosym("libtermcap.so.1.3.1", "/usr/lib/libtermcap.so")
