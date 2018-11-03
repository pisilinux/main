#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

#def setup():
    #autotools.configure()

def build():
    shelltools.system("cargo build --release")
    
def check():
    shelltools.system("cargo test --release")

def install():
    pisitools.dobin("target/release/cbindgen")

    pisitools.dodoc("README*")
