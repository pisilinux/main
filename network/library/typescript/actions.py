#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import mesontools
from pisi.actionsapi import get
import os

pkgname = get.srcNAME()
work_dir = get.workDIR()
src_name = get.srcNAME()

def setup():
    shelltools.system("/usr/bin/npm ci")
    # mesontools.configure()

def build():
    shelltools.system("/usr/bin/npx hereby LKG")
    # mesontools.build()

def install():
    mod_dir = "/usr/lib/node_modules/%s" % pkgname

    # Çalışma dizinini ayarla
    # os.chdir(os.path.join(work_dir, src_name))

    # Dizin yapısını oluştur
    pisitools.dodir("/usr/bin")
    pisitools.dodir(mod_dir)

    # Dosyaları kopyala
    for item in ["bin", "lib", "package.json"]:
        if os.path.exists(item):
            if os.path.isdir(item):
                pisitools.insinto("%s/%s" % (mod_dir, item), "%s/*" % item)
            else:
                pisitools.insinto(mod_dir, item)

    # Sembolik linkler
    pisitools.dosym("%s/bin/tsc" % mod_dir, "/usr/bin/tsc")
    pisitools.dosym("%s/bin/tsserver" % mod_dir, "/usr/bin/tsserver")

    # Dokümantasyon
    # pisitools.dodoc("README.md", "SECURITY.md")

    # Lisans
    pisitools.insinto("/usr/share/doc/licenses/%s" % pkgname, "ThirdPartyNoticeText.txt")

    pisitools.dodoc("SECURITY*", "SUPPORT*", "CONTRIBUTING*", "README*")
