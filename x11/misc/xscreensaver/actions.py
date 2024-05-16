#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools, pisitools, get, shelltools

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
    ' --with-jpeg',
    ' --with-login-manager ',
    ' --enable-pam-check-account-type',
    ' --without-systemd '
    ])
shelltools.export("LC_ALL", "en_US.UTF-8")

def setup():
	pisitools.dosed("driver/Makefile.in", "UPDATE_ICON_CACHE", deleteLine = True)
	# shelltools.system("sed -i 's/-lsystemd/-lelogind/' driver/Makefile.in")
	autotools.configure(j)


def build():
	autotools.make()

def install():
	autotools.rawInstall("install_prefix=%s" % get.installDIR())
	pisitools.insinto("/etc/pam.d", "driver/xscreensaver.pam", "xscreensaver")
