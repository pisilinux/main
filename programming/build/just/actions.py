#!/usr/bin/python2
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

import os

from pisi.actionsapi import get
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

WorkDir = "just-%s" % get.srcVERSION()

def setup():
    # Cargo ortam değişkenlerini ayarla
    shelltools.export("CARGO_HOME", get.workDIR())
    shelltools.export("CARGO_PROFILE_RELEASE_DEBUG", "2")
    shelltools.export("CARGO_PROFILE_RELEASE_STRIP", "false")
    shelltools.export("CARGO_PROFILE_RELEASE_LTO", "true")
    shelltools.export("CARGO_PROFILE_RELEASE_CODEGEN_UNITS", "1")
    shelltools.export("CARGO_PROFILE_RELEASE_OPT_LEVEL", "3")

    # Cargo bağımlılıklarını indir
    shelltools.system("cargo fetch --locked --target host-tuple")

    # Dizinleri oluştur
    shelltools.makedirs("man")
    shelltools.makedirs("completions")

def build():
    # Cargo ortam değişkenlerini tekrar ayarla
    shelltools.export("CARGO_HOME", get.workDIR())
    shelltools.export("CARGO_PROFILE_RELEASE_DEBUG", "2")
    shelltools.export("CARGO_PROFILE_RELEASE_STRIP", "false")
    shelltools.export("CARGO_PROFILE_RELEASE_LTO", "true")
    shelltools.export("CARGO_PROFILE_RELEASE_CODEGEN_UNITS", "1")
    shelltools.export("CARGO_PROFILE_RELEASE_OPT_LEVEL", "3")

    # Release modunda derle
    shelltools.system("cargo build --frozen --release")

    # Man sayfasını oluştur
    shelltools.system("cargo run --frozen --release -- --man > man/just.1")

def check():
    # Cargo ortam değişkenlerini ayarla
    shelltools.export("CARGO_HOME", get.workDIR())

    # Testleri çalıştır
    shelltools.system("cargo check --frozen --release")

def install():
    # Çalıştırılabilir dosya
    pisitools.dobin("target/release/just")

    # Man sayfası
    pisitools.insinto("/usr/share/man/man1/", "man/just.1")

    # Lisans
    pisitools.insinto("/usr/share/doc/just/", "LICENSE")

    # Bash tamamlama
    pisitools.insinto("/usr/share/bash-completion/completions/", "completions/just.bash", "just")

    # Elvish tamamlama
    pisitools.insinto("/usr/share/elvish/lib/", "completions/just.elvish", "just.elv")

    # Fish tamamlama
    pisitools.insinto("/usr/share/fish/vendor_completions.d/", "completions/just.fish")

    # Zsh tamamlama
    pisitools.insinto("/usr/share/zsh/site-functions/", "completions/just.zsh", "_just")
