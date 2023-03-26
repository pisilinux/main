#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import pythonmodules, autotools, pisitools, get

def build():
    pythonmodules.compile(pyVer = "3")
    autotools.make("PREFIX=/usr MANDIR=/usr/share/man")

def install():
    pythonmodules.install(pyVer = "3")
    #pisitools.removeDir("/usr/share/bin")
    pisitools.removeDir("/usr/share/doc")
    autotools.rawInstall("DESTDIR=%s PREFIX=/usr MANDIR=/usr/share/man" % get.installDIR())
    pisitools.removeDir("/usr/share/fish")

    pisitools.dodoc("Changelog.md")
