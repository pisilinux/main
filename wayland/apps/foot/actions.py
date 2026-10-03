#!/usr/bin/env python3

import os
from pisi.actionsapi import shelltools
from pisi.actionsapi import mesontools
from pisi.actionsapi import pisitools

def setup():
    # pkgconfig arama yollarını tüm ortamlara zorunlu olarak ekliyoruz
    pkg_paths = "/usr/lib/pkgconfig:/usr/share/pkgconfig:/usr/lib64/pkgconfig"
    
    os.environ["PKG_CONFIG_PATH"] = pkg_paths
    os.environ["PKG_CONFIG_LIBDIR"] = pkg_paths
    
    shelltools.export("PKG_CONFIG_PATH", pkg_paths)
    shelltools.export("PKG_CONFIG_LIBDIR", pkg_paths)

    # meson konfigürasyonu
    mesontools.configure("-Ddocs=enabled -Dgrapheme-clustering=disabled", build_dir="build")

def build():
    mesontools.build(build_dir="build")

def install():
    mesontools.install(build_dir="build")
    pisitools.dodoc("README.md", "LICENSE")