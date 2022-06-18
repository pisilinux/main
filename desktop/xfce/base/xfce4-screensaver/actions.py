#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

j = ''.join([
    '--enable-pam',
    '--enable-locking',
    '--enable-authentication-scheme=pam',
    '--disable-static',
    '--with-libgl',
    '--with-shadow',
    '--with-mit-ext',
    '--with-elogind',
    '--without-console-kit',
    '--with-pam-auth-type=system',
    '--without-systemd'])

def setup():
#    shelltools.system("patch -Rp1 < 0001-Catch-gs_listener_dbus_init-failures.patch")
    autotools.configure(j)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("COPYING*", "INSTALL", "NEWS", "README.md")

