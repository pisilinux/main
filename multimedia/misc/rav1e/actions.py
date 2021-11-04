#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def build():
    shelltools.system("cargo build \
                        --release \
                        --manifest-path Cargo.toml")

    shelltools.system("cargo cbuild \
                        --release \
                        --frozen \
                        --prefix=/usr \
                        --manifest-path Cargo.toml")

def install():
    shelltools.system("cargo install --path . \
                        --root='%s'/usr" % get.installDIR())

    shelltools.system("cargo cinstall \
                        --release \
                        --frozen \
                        --prefix /usr \
                        --destdir %s" % get.installDIR())

    pisitools.remove("/usr/lib/librav1e.a")
    pisitools.remove("/usr/.crates.toml")
    pisitools.remove("/usr/.crates2.json")

    pisitools.dodoc("LICENSE", "README*")
