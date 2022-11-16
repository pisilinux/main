#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools, cmaketools, pisitools, get

j = ''.join([
    ' -DENABLE_EXAMPLES=ON',
    ' -DENABLE_MILTER=OFF',
    ' -DENABLE_SYSTEMD=OFF',
    ' -DAPP_CONFIG_DIRECTORY=/etc/clamav',
    ' -DDATABASE_DIRECTORY=/var/lib/clamav',
    ' -G Ninja',
    ' -B_build -L '
    ])

def setup():
    cmaketools.configure(j)

def build():
    shelltools.system("ninja -C _build")

def check():
    #pass
    shelltools.system("ninja -C _build test")

def install():
    shelltools.system("DESTDIR=%s ninja -C _build install" % get.installDIR())

    #pisitools.dodir("/run/clamav")
    pisitools.dodir("/var/lib/clamav")
    #pisitools.dodir("/var/log/clamav")

    shelltools.system("find %s/etc/clamav -type f | sed -e 'p;s:.sample::' | xargs -n2 mv" % get.installDIR())
