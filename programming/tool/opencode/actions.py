#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "."
NoStrip = ["/usr/bin/opencode"]

def setup():
    shelltools.system("curl -sL -o LICENSE https://raw.githubusercontent.com/anomalyco/opencode/v%s/LICENSE" % get.srcVERSION())

def build():
    pass

def install():
    pisitools.dobin("opencode")
    pisitools.insinto("/usr/share/licenses/opencode", "LICENSE")

    bindir = "%s/usr/bin/opencode" % get.installDIR()
    home = get.workDIR()
    shelltools.makedirs("%s/usr/share/bash-completion/completions" % get.installDIR())
    shelltools.makedirs("%s/usr/share/zsh/site-functions" % get.installDIR())
    shelltools.system("HOME=%s SHELL=/bin/bash %s completion > %s/usr/share/bash-completion/completions/opencode" % (home, bindir, get.installDIR()))
    shelltools.system("HOME=%s SHELL=/bin/zsh %s completion > %s/usr/share/zsh/site-functions/_opencode" % (home, bindir, get.installDIR()))
    shelltools.chmod("%s/usr/share/bash-completion/completions/opencode" % get.installDIR(), 0644)
    shelltools.chmod("%s/usr/share/zsh/site-functions/_opencode" % get.installDIR(), 0644)
    shelltools.chmod("%s/usr/share/licenses/opencode/LICENSE" % get.installDIR(), 0644)
