#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    # There HAS TO BE a way to parse shell commands as variables. Hardcoding target looks too dirty!
    shelltools.system("cargo fetch --locked --target x86_64-unknown-linux-gnu")

def build():
    shelltools.system("cargo build --frozen --release")

def install():
    pisitools.dodir("/usr/lib/helix")
    pisitools.insinto("/usr/lib/helix", "target/release/hx")
    pisitools.dodir("/usr/bin")
    pisitools.dosym("/usr/lib/helix/hx", "/usr/bin/hx")
    pisitools.dosym("/usr/bin/hx", "/usr/bin/helix")
    pisitools.dodoc("README.md")

    pisitools.dodir("/usr/lib/helix/runtime/grammars")
    pisitools.insinto("/usr/lib/helix/runtime", "runtime/queries")
    pisitools.insinto("/usr/lib/helix/runtime", "runtime/themes")
    shelltools.system("find runtime/grammars -type f -name '*.so' -exec install -Dm 755 {} -t %s/usr/lib/helix/runtime/grammars \\;" % get.installDIR())
    pisitools.insinto("/usr/lib/helix/runtime", "runtime/tutor")

    pisitools.dodir("/usr/share/bash-completion/completions")
    pisitools.insinto("/usr/share/bash-completion/completions", "contrib/completion/hx.bash", "hx")
    pisitools.dodir("/usr/share/fish/vendor_completions.d")
    pisitools.insinto("/usr/share/fish/vendor_completions.d", "contrib/completion/hx.fish", "hx.fish")
    pisitools.dodir("/usr/share/zsh/site-functions")
    pisitools.insinto("/usr/share/zsh/site-functions", "contrib/completion/hx.zsh", "_hx")
    pisitools.dodir("/usr/share/applications")
    pisitools.insinto("/usr/share/applications", "contrib/Helix.desktop", "helix.desktop")
    pisitools.dodir("/usr/share/icons/hicolor/256x256/apps")
    pisitools.insinto("/usr/share/icons/hicolor/256x256/apps", "contrib/helix.png")
