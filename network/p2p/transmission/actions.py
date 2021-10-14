#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import qt5

j = ''.join([
    ' --enable-cli',
    ' --enable-utp',
    ' --enable-lightweight',
    ' --enable-daemon',
    ' --disable-static',
    ' --disable-mac',
    ' --with-gtk',
    ' --with-crypto=openssl',
    ' --without-systemd '
    ])

def setup():
	autotools.configure(j)

	# transmission with qt gui configure.
	shelltools.cd("qt")
	qt5.configure()

def build():
	autotools.make()

	# transmission with qt gui make.
	shelltools.cd("qt")
	qt5.make()
	qt5.make("translations")

def install():
	# qt
	qt5.install("-C qt INSTALL_ROOT=%s/usr" % get.installDIR())
	pisitools.insinto("%s/%s" % (get.docDIR(), get.srcNAME()), "qt/README.txt", "README-QT")
	pisitools.insinto("%s/applications" % get.dataDIR(), "qt/transmission-qt.desktop")

	# gtk
	autotools.rawInstall("-C gtk DESTDIR=%s" % get.installDIR())
	autotools.rawInstall("-C po DESTDIR=%s" % get.installDIR())

	# cli, web, deamon
	for _dir in ["cli", "web", "utils"]:
		autotools.rawInstall("-C %s DESTDIR=%s" % (_dir, get.installDIR()))

	# For daemon config files.
	pisitools.dodir("/etc/transmission-daemon")

	pisitools.dodoc("AUTHORS", "COPYING", "NEWS.md", "README.md")

