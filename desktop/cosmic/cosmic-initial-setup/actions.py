#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools


def setup():

    
    # cargo bağımlılıklarını indir
    shelltools.system("cargo fetch --locked --target $(rustc --print host-tuple)")
    
    # Geçici git deposu başlat
    # shelltools.system(
        # "git clone --branch epoch-1.10.0 "
        # "https://github.com/pop-os/cosmic-initial-setup.git "
        # "cosmic-initial-setup"
    # )
    
    # git lfs kurulumu ve dosyaları çek
    # shelltools.system("git lfs install --local")
    # shelltools.system("git remote add network-origin https://github.com/pop-os/cosmic-initial-setup")
    # shelltools.system("git lfs fetch origin")
    # shelltools.system("git lfs checkout")


def build():

    shelltools.system("just build-release")


def install():

    shelltools.system("just rootdir=\"%s\" install" % get.installDIR())
    
    pisitools.dodoc("LICENSE", "README.md")
