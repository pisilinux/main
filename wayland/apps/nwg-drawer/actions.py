#!/usr/bin/env python3

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    shelltools.export("GOPATH", get.workDIR())
    shelltools.export("GO111MODULE", "on")
    shelltools.system("make build")

def install():
    # Binary dosyayı yükle
    pisitools.dobin("bin/nwg-drawer")
    
    # CSS dosyasını kopyala
    pisitools.insinto("/usr/share/nwg-drawer", "drawer.css")
    
    # Kategori dizinlerini kopyala
    if shelltools.isDirectory("desktop-directories"):
        pisitools.insinto("/usr/share/nwg-drawer/desktop-directories", "desktop-directories/*")
        
    # Görsel simgeler dizini varsa kopyala
    if shelltools.isDirectory("img"):
        pisitools.insinto("/usr/share/nwg-drawer/img", "img/*")

    # Dokümantasyon
    pisitools.dodoc("README.md", "LICENSE")