#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

i = ''.join([
    ' --enable-xft',
    ' --enable-perl',
    ' --enable-frills',
    ' --enable-fading',
    ' --enable-pixbuf',
    ' --enable-unicode3',
    ' --enable-iso14755',
    ' --enable-256-color',
    ' --enable-combining',
    ' --enable-mousewheel',
    ' --enable-everything',
    ' --enable-text-blink',
    ' --enable-rxvt-scroll',
    ' --enable-next-scroll',
    ' --enable-font-styles',
    ' --enable-xterm-scroll',
    ' --enable-transparency',
    ' --enable-slipwheeling',
    ' --enable-smart-resize',
    ' --enable-pointer-blank',
    ' --enable-keepscrolling',
    ' --enable-selectionscrolling '
    ])

def setup():
    autotools.configure(i)

def build():
    autotools.make()
    pisitools.dosed("doc/rxvt-tabbed", "RXVT_BASENAME = \"rxvt\"", "RXVT_BASENAME = \"urxvt\"")

def install():
    shelltools.export("TERMINFO", "%s/usr/share/terminfo" % get.installDIR())
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dobin("doc/rxvt-tabbed")

    pisitools.insinto("/usr/share/terminfo/r", "doc/etc/rxvt-unicode.terminfo", "rxvt-unicode")
    pisitools.insinto("/etc", "doc/etc/rxvt-unicode.termcap")

    shelltools.chmod("%s/usr/share/terminfo/r/rxvt-unicode" % get.installDIR(), 0644)
    shelltools.chmod("%s/etc/rxvt-unicode.termcap" % get.installDIR(), 0644)

    pisitools.dodoc("README.FAQ", "Changes", "doc/README.xvt")

    # Should be provided by ncurses
    pisitools.remove("/usr/share/terminfo/r/rxvt-unicode")
