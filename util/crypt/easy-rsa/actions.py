#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt
#

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def install():
	pisitools.insinto("/usr/bin", "easyrsa", "easyrsa")
	pisitools.insinto("/etc/easy-rsa", "openssl-easyrsa.cnf", "openssl-easyrsa.cnf")
	pisitools.insinto("/etc/easy-rsa/x509-types", "x509-types/*")
	     
	pisitools.dodoc("ChangeLog", "COPYING*", "README*")

