#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

targets = "x86_64-softmmu,i386-softmmu,aarch64-softmmu,arm-softmmu,riscv64-softmmu,x86_64-linux-user,aarch64-linux-user"

cfgparams = " ".join([
    "--prefix=/usr",
    "--sysconfdir=/etc",
    "--libexecdir=/usr/lib/qemu",
    "--target-list=%s" % targets,
    "--disable-werror",
    "--disable-docs",
])

def setup():
    # pisi kernel-headers paketi kernel UAPI sound/asound.h icermez; linux-user
    # hedefi icin gerekli. Kaynak paketteki files/sound/asound.h Source
    # AdditionalFile ile kopyalanir; pisi os.path.join quirk'u yuzunden dosya
    # /sound/asound.h konumuna duser. Kernel-spesifik sparse makrolari build
    # basarili olsun diye temizlenir.
    shelltools.makedirs("linux-headers/sound")
    shelltools.copy("/sound/asound.h", "linux-headers/sound/")
    shelltools.system("sed -i 's/__user//g; s/__force//g; s/__packed/__attribute__((packed))/g' linux-headers/sound/asound.h")
    shelltools.system("./configure %s" % cfgparams)

def build():
    shelltools.system("ninja -C build")

def install():
    shelltools.system("meson install -C build --destdir %s" % get.installDIR())

    # QEMU localstatedir nedeniyle bos /var/run dizini olusturur; bu dizin
    # paketlenirse hedef sistemdeki /var/run -> /run symlink'ini ezer.
    shelltools.system("rmdir %s/var/run %s/var 2>/dev/null || true" % (get.installDIR(), get.installDIR()))

    pisitools.dodoc("LICENSE", "README.rst")
