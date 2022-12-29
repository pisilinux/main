#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import perlmodules, shelltools, pisitools, get

shelltools.export("CONTACT_ADDRESS", "root@localhost")
shelltools.export("ENABLE_SSL", "yes")
shelltools.export("PERL_USE_UNSAFE_INC", "1")
shelltools.export("CFLAGS", "%s -DSPAMC_SSL -lssl -lcrypto" % get.CFLAGS())

def setup():
	perlmodules.configure()
	#shelltools.cd("spamc")
	#shelltools.system("./configure.pl && ./configure --enable-ssl=yes")

def build():
	perlmodules.make()

def check():
	pass
#	perlmodules.make("test")

def install():
	perlmodules.install()

	pisitools.dodir("/var/lib/spamd")

