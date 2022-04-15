#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools, pisitools, get

t = ''.join([
    'netstatus ',
    'netstat ',
    'volume ',
    'deskno ',
    'kbled ',
    'batt ',
    'xkb ',
    'cpufreq ',
    'monitors ',
    'indicator'
    ])

def setup():
	pisitools.cflags.add("-fcommon -Wno-deprecated-declarations")
	autotools.configure("--enable-gtk3 --with-plugins='%s'" % t)

	pisitools.dosed("libtool", " -shared ", " -Wl,-O2,--as-needed -shared ")

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("AUTHORS", "ChangeLog", "README", "TODO")

