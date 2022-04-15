#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools, pisitools, get

j = ''.join([
    ' PREFIX=/usr',
    ' SYSCONFDIR=/etc',
    ' SYSTEMD=0',
    ' WAYLAND=0',
    ' SERVICEDIR_DBUS=/usr/share/dbus-1/services '
    ])

def setup():
	pass

def build():
	autotools.make(j)

def install():
	autotools.rawInstall("DESTDIR=%s %s" % (get.installDIR(), j))

	pisitools.dodoc("AUTHORS", "CHANGELOG.md", "HACKING.md", "README.md", "RELEASE_NOTES")

