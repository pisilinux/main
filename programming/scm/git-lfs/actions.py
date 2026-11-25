#!/usr/bin/python2
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

import os

from pisi.actionsapi import get
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

# WorkDir = "git-lfs"

def setup():
    # Go ortam değişkenlerini ayarla
    shelltools.export("CGO_CPPFLAGS", os.environ.get("CPPFLAGS", ""))
    shelltools.export("CGO_CFLAGS", os.environ.get("CFLAGS", ""))
    shelltools.export("CGO_CXXFLAGS", os.environ.get("CXXFLAGS", ""))
    shelltools.export("CGO_LDFLAGS", os.environ.get("LDFLAGS", ""))
    shelltools.export("GOFLAGS", "-buildmode=pie -trimpath -modcacherw -ldflags=-linkmode=external")

    # Go mod vendor ve generate
    shelltools.system("go mod vendor")
    shelltools.system("go generate ./commands")

def build():
    # Go build
    shelltools.system("go build .")

    # Man sayfalarını oluştur
    shelltools.system("make man")

def check():
    # Testleri çalıştır
    shelltools.system("go test -mod=vendor ./...")

def install():
    # Çalıştırılabilir dosya
    pisitools.dobin("git-lfs")

    # Lisans
    pisitools.insinto("/usr/share/licenses/git-lfs/", "LICENSE.md", "LICENSE")

    # Man sayfaları
    pisitools.insinto("/usr/share/man/man1/", "man/man1/*.1")
    pisitools.insinto("/usr/share/man/man5/", "man/man5/*.5")

    # Tamamlama dosyalarını oluşturmak için tam yolu kullan
    lfs_bin = "%s/usr/bin/git-lfs" % get.installDIR()

    # Bash tamamlama
    shelltools.system("%s completion bash > /tmp/git-lfs.bash" % lfs_bin)
    pisitools.insinto("/usr/share/bash-completion/completions/", "/tmp/git-lfs.bash", "git-lfs")

    # Fish tamamlama
    shelltools.system("%s completion fish > /tmp/git-lfs.fish" % lfs_bin)
    pisitools.insinto("/usr/share/fish/vendor_completions.d/", "/tmp/git-lfs.fish", "git-lfs.fish")

    # Zsh tamamlama
    shelltools.system("%s completion zsh > /tmp/_git-lfs" % lfs_bin)
    pisitools.insinto("/usr/share/zsh/site-functions/", "/tmp/_git-lfs", "_git-lfs")
