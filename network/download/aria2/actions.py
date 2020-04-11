#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
	autotools.configure("--prefix=/usr \
	--enable-bittorrent \
	--enable-libaria2 \
	--enable-metalink \
	--enable-epoll \
	--enable-nls \
	\
	--disable-rpath \
	--disable-static \
	\
	--with-libz \
	--with-gnutls \
	--with-sqlite3 \
	--with-libxml2 \
	--with-libssh2 \
	--with-libcares \
	--with-ca-bundle=/etc/ssl/certs/ca-certificates.crt \
	--with-bashcompletiondir=/usr/share/bash-completion/completions")

def build():
	autotools.make("-C po update-gmo")
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("AUTHORS", \
	"COPYING", \
	"INSTALL", \
	"LICENSE.OpenSSL", \
	"NEWS", \
	"README*")

