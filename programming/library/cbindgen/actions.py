#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("CYTHON", "/usr/bin/cython3")

def setup():
   shelltools.system("cargo fetch --locked --target x86_64-unknown-linux-gnu")

def build():
    shelltools.system("cargo build --release --frozen --all-targets")
    
def check():
    # shelltools.system("cargo test --release || :")
    shelltools.system("RUSTC_BOOTSTRAP=1 cargo test --release --frozen")

def install():
    pisitools.dobin("target/release/cbindgen")

    pisitools.dodoc("README*")
