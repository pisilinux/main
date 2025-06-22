#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools, autotools, get, pisitools

def setup():
    shelltools.system("NOCONFIGURE=1 ./autogen.sh")
    autotools.configure("--disable-systemd-services \
            --without-systemd \
            --enable-fts \
            --enable-datahub")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
        # unneeded systemd service file
    pisitools.removeDir("/usr/lib/systemd")

    # data = "nodist_systemd_user_DATA = ''"
    # doc = "zeitgeistdoc_DATA = 'AUTHORS COPYING MAINTAINERS NEWS'"
    # autotools.rawInstall("DESTDIR=%s %s %s" % (get.installDIR(), data, doc))
