#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools, pisitools, get

i = "PREFIX=/usr"

def setup():
	pass

def build():
	autotools.make(i)

def install():
	autotools.rawInstall("DESTDIR=%s %s" % (get.installDIR(), i))
	pisitools.insinto("/usr/share/bash-completion/completions", "misc/auto-completion/bash/nnn-completion.bash", "nnn")
	pisitools.insinto("/usr/share/zsh/functions/Completion/Unix", "misc/auto-completion/zsh/_nnn")
	pisitools.insinto("/usr/share/applications", "misc/desktop/nnn.desktop")
