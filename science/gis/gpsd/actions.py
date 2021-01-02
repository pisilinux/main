#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

shelltools.export("PYTHONDONTWRITEBYTECODE", "1")
i = "/usr/bin/env python3 $(which scons)"

def setup():
	pass

def build():
	shelltools.system("%s target_python=python3 prefix=/usr sbindir=/usr/sbin udevdir=/lib/udev" % i)

def install():
	shelltools.system("DESTDIR=%s %s udev-install prefix=/usr" % (get.installDIR(), i))

	# fix shebang
	shelltools.system("find %s/usr/bin -type f -exec sed -i 's|env\ python$|env python3|g' {} \;" % get.installDIR())

	# Install UDEV files
#	pisitools.insinto("/lib/udev/rules.d", "gpsd.rules", "99-gpsd.rules")
#	pisitools.dobin("gpsd.hotplug", "/lib/udev")

