#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools, autotools, get

def setup():
    shelltools.system("NOCONFIGURE=1 ./autogen.sh")
    autotools.configure("--enable-fts --enable-datahub")

def build():
    autotools.make()

def install():
    data = "nodist_systemd_user_DATA = ''"
    doc = "zeitgeistdoc_DATA = 'AUTHORS COPYING MAINTAINERS NEWS'"
    autotools.rawInstall("DESTDIR=%s %s %s" % (get.installDIR(), data, doc))
