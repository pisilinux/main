#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    shelltools.system("go build \
        -trimpath \
        -ldflags '-extldflags \"%s\" -X github.com/cli/cli/command.Version=v2.64.0 -X github.com/cli/cli/command.BuildDate=2024-12-31' \
        -o 'bin/gh' ./cmd/gh" % get.LDFLAGS())

def install():
    shelltools.cd("../cli-2.64.0")
    pisitools.insinto("/usr/bin", "bin/gh")
    pisitools.dodoc("LICENSE", "README*")
