#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools, pisitools, get

def setup():
    pisitools.dosed("mk/make_config", "/man", "/share/man")
    autotools.rawConfigure("-prefix /usr -disable-fam")

def build():
    autotools.make("all")

def install():
    autotools.rawInstall("INSTALL_ROOT=%s" % get.installDIR())
