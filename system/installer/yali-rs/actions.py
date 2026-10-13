#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
import os

def setup():
    # Cargo'nun pisi sandbox dışına çıkıp sistem dosyalarına erişmesini engellemek için
    # CARGO_HOME ve hedef dizini kesin olarak workDIR altına sabitliyoruz.
    cargo_home = os.path.join(get.workDIR(), "cargo-home")
    target_dir = os.path.join(get.workDIR(), "target")
    
    os.environ["CARGO_HOME"] = cargo_home
    shelltools.export("CARGO_HOME", cargo_home)
    shelltools.export("CARGO_TARGET_DIR", target_dir)

def build():
    # Eğer Makefile kullanılıyor ve içinde cargo build çalıştırılıyorsa,
    # derleme adımında da CARGO_HOME ortam değişkeninin korunduğundan emin olalım.
    cargo_home = os.path.join(get.workDIR(), "cargo-home")
    shelltools.export("CARGO_HOME", cargo_home)
    
    # Doğrudan Makefile yerine cargo kullanıyorsanız burayı `shelltools.system("cargo build --release --offline")` yapabilirsiniz.
    shelltools.system("make")

def install():
    shelltools.system("make DESTDIR=%s install" % get.installDIR())
    # Dosya isimlerinde hata almamak için var olan dokümanları kontrol edin (örn: TODO.md olmayabilir)
    pisitools.dodoc("README.md")
