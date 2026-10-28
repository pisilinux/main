#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import python3modules, autotools, get

def build():
    python3modules.compile(pyVer="3")
    autotools.make("lazy-extractors yt-dlp.1 completions")

def install():
    python3modules.install(pyVer="3")
    autotools.rawInstall(
        "DESTDIR=%s PREFIX=/usr MANDIR=/usr/share/man"
        % get.installDIR()
    )