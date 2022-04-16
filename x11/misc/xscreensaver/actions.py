#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools, pisitools, get

j = ''.join([
    ' --enable-locking',
    ' --with-pam',
    ' --with-shadow',
    ' --with-elogind',
    ' --with-dpms-ext',
    ' --with-xshm-ext',
    ' --with-xdbe-ext',
    ' --with-gl',
    ' --with-xft',
    ' --with-login-manager ',
    ' --without-systemd '
    ])

def setup():
	autotools.configure(j)

def build():
	autotools.make()

def install():
	autotools.rawInstall("install_prefix=%s" % get.installDIR())
	pisitools.insinto("/etc/pam.d", "driver/xscreensaver.pam", "xscreensaver")
