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
    shelltools.system('export RUSTUP_TOOLCHAIN=stable')
    shelltools.system("""cargo fetch --locked --target "$(rustc -vV | sed -n 's/host: //p')" """)

def build():
    shelltools.system('export RUSTFLAGS+=" -C link-arg=-fuse-ld=mold"')
    shelltools.system('just build-release --frozen')


def install():
    shelltools.system("nice just rootdir='%s' install" % get.installDIR())

    pisitools.dodoc("LICENSE*")
