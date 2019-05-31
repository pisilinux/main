#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def build():
    shelltools.system("""sed -i '/int Guess/a \
                       int   j = 0;\
                       char* jobs = getenv( "NINJAJOBS" );\
                       if ( jobs != NULL ) j = atoi( jobs );\
                       if ( j > 0 ) return j;\
                       ' src/ninja.cc""")
    
    shelltools.system("python configure.py --bootstrap")
    shelltools.system("asciidoc doc/manual.asciidoc")
    shelltools.system("emacs -Q --batch -f batch-byte-compile misc/ninja-mode.el")

def check():
    #needs new package gtest -> ignore it for now
    shelltools.system("python ./configure.py")
    shelltools.system("./ninja ninja_test")
    shelltools.system("./ninja_test --gtest_filter=-SubprocessTest.SetWithLots")

def install():
    pisitools.dobin("ninja", "/usr/bin")

    pisitools.insinto("/usr/share/bash-completion/completions", "misc/bash-completion", "ninja")
    pisitools.insinto("/usr/share/emacs/site-lisp", "misc/ninja-mode.el")
    pisitools.insinto("/usr/share/emacs/site-lisp", "misc/ninja-mode.elc")
    pisitools.insinto("/usr/share/vim/vimfiles/syntax", "misc/ninja.vim")
    pisitools.insinto("/usr/share/zsh/site-functions", "misc/zsh-completion", "_ninja")

    pisitools.dodoc("HACKING.md", "COPYING", "RELEASING", "README", "doc/manual.asciidoc")

    pisitools.dohtml("doc/manual.html")
