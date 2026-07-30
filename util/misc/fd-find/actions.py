#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

def build():
    shelltools.system("cargo build --release")

def install():
    pisitools.dobin("target/release/fd")

    pisitools.doman("doc/fd.1")

    pisitools.dodoc("README.md", "LICENSE-MIT", "LICENSE-APACHE")

    pisitools.insinto("/usr/share/zsh/site-functions", "contrib/completion/_fd", "_fd")
    # pisitools.insinto("/usr/share/bash-completion/completions", "contrib/completion/fdfind.bash", "fd")
    # pisitools.insinto("/usr/share/fish/vendor_completions.d", "contrib/completion/fdfind.fish")
