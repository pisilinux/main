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
    shelltools.system('cargo fetch --locked --target "x86_64-unknown-linux-gnu"')
    # autotools.configure()

def build():
    shelltools.system('cargo build --release --frozen')
    # autotools.make()

def install():
    shelltools.system("cargo install --path . --root='%s'/usr" % get.installDIR())

    pisitools.remove("/usr/.crates.toml")
    pisitools.remove("/usr/.crates2.json")

    pisitools.dodoc("LICENSE", "README*")
