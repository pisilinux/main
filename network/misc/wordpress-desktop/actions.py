#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

# Electron/Chromium ikilileri strip edilmemeli
NoStrip = ["/"]

YARN = "node .yarn/releases/yarn-4.0.2.cjs"
YARN_FLAGS = "YARN_ENABLE_GLOBAL_CACHE=0 YARN_CACHE_FOLDER=.yarn/cache"


def setup():
    # Yarn 4 kaynak ağacında geliyor (.yarn/releases). Sadece masaüstü
    # uygulamasının bağımlılıklarını kur; husky/tsc gibi gereksiz
    # lifecycle script'lerini çalıştırma. Önbellek, Pisi sandbox'ı dışına
    # yazmamak için proje içinde tutuluyor.
    shelltools.system(
        "YARN_ENABLE_SCRIPTS=0 %s %s workspaces focus WordPressDesktop"
        % (YARN_FLAGS, YARN)
    )


def build():
    # Electron ana süreç paketini (dist/index.js) üret
    shelltools.system(
        "CONFIG_ENV=release NODE_ENV=production %s %s "
        "workspace WordPressDesktop run build:main" % (YARN_FLAGS, YARN)
    )

    # deb/AppImage yerine sadece açılmış Linux dizinini üret.
    # npmRebuild=false: yerel modüllerin yeniden derlenmesini atla;
    # uygulamanın ihtiyaç duyduğu modüller saf JS.
    shelltools.system(
        "YARN_ENABLE_SCRIPTS=0 "
        "XDG_CACHE_HOME=\"$PWD/.cache\" "
        "ELECTRON_BUILDER_CACHE=\"$PWD/.cache/electron-builder\" "
        "%s workspace WordPressDesktop exec electron-builder"
        " --dir --publish never -c.npmRebuild=false" % YARN
    )


def install():
    # electron-builder çıktısı: desktop/release/linux-unpacked
    pisitools.insinto("/usr/share/wpcom/", "desktop/release/linux-unpacked/*")
    pisitools.dodoc("README.md")
    pisitools.newdoc("desktop/README.md", "README.desktop.md")

    # electron-builder çıktısındaki izinleri normalize et. Özellikle
    # chrome-sandbox setuid olmalı; aksi halde Electron sandbox'ı açılmaz.
    # Not: /var/pisi gerçek bir Linux dosya sisteminde olmalı; FUSE/NTFS
    # üzerinde chmod/chown etkisiz kalır ve paket 0777 olarak üretilir.
    install_dir = get.installDIR()
    app_dir = "%s/usr/share/wpcom" % install_dir
    shelltools.system("chown -R root:root %s" % app_dir)
    shelltools.system("find %s -type d -exec chmod 0755 {} +" % app_dir)
    shelltools.system("find %s -type f -exec chmod 0644 {} +" % app_dir)
    shelltools.system(
        "chmod 0755 %s/wpcom %s/chrome_crashpad_handler" % (app_dir, app_dir)
    )
    shelltools.system("chmod 4755 %s/chrome-sandbox" % app_dir)

    doc_dir = "%s/usr/share/doc/wordpress-desktop" % install_dir
    shelltools.system("chown -R root:root %s" % doc_dir)
    shelltools.system("chmod -R u=rwX,go=rX %s" % doc_dir)
