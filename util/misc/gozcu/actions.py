#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

def build():
    # Rust projesini release modunda derler
    shelltools.system("cargo build --release --locked")

def install():
    # 1. Derlenen ikili dosyayı (binary) /usr/bin altına kurar
    pisitools.dobin("target/release/gozcu")

    # 2. .desktop kısayol dosyasını /usr/share/applications altına kurar
    pisitools.insinto("/usr/share/applications", "gozcu.desktop")

    # 3. SVG ikonu hicolor scalable ikon dizinine kurar
    pisitools.insinto("/usr/share/icons/hicolor/scalable/apps", "assets/gozcu.svg")

    # 4. Dokümantasyon ve Lisans dosyalarını kurar
    pisitools.dodoc("README.md", "LICENSE*")
