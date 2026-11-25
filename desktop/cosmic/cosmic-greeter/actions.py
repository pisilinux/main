#!/usr/bin/python2
# -*- coding: utf-8 -*-# -*- coding: utf-8 -*-
#
# Licensed under the terms of the GNU General Public License, v3 or later.
#

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
import os

def setup():
    # .git yoksa depo oluştur ve HEAD oluşması için geçici bir ilk commit at
    if not os.path.exists(".git"):
        shelltools.system("git init")
        shelltools.system("git config user.name 'Pisi Build'")
        shelltools.system("git config user.email 'build@pisilinux.org'")
        shelltools.system("git add -A")
        shelltools.system("git commit -m 'Initial build commit' --allow-empty")
    
    shelltools.system("git lfs install --local")
    
    # Rust bağımlılıklarını çevrimdışı önbellekleme
    shelltools.system("cargo fetch --locked")

def build():
    # LLD bağlayıcı desteği ile release inşası
    shelltools.export("RUSTFLAGS", "-C link-arg=-fuse-ld=lld")
    
    # Projeyi build etme
    shelltools.system("just build-release --frozen")

def install():
    # Paket çıktısını pisi pkgdir dizinine kurma
    shelltools.system("just rootdir={} install".format(get.installDIR()))
    
    # Konfigürasyon ve systemd servis dosyalarının kopyalanması
    pisitools.insinto("/etc/greetd/", "cosmic-greeter.toml")
    pisitools.insinto("/usr/lib/systemd/system/", "debian/cosmic-greeter.service")
    pisitools.insinto("/usr/lib/systemd/system/", "debian/cosmic-greeter-daemon.service")