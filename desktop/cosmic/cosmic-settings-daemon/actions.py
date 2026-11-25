#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def setup():
    shelltools.system('cargo fetch --locked')

    # shelltools.system("sed 's/libexec/lib/g' -i Makefile src/main.rs")
    shelltools.system("sed 's/sudo/wheel/g' -i data/polkit-1/rules.d/cosmic-settings-daemon.rules")

def build():
    shelltools.system('export RUSTFLAGS+=" -C link-arg=-fuse-ld=mold"')
    shelltools.system('just build-release --frozen')


def install():
    shelltools.system("just rootdir='%s' install" % get.installDIR())

    pisitools.dodoc("LICENSE")
