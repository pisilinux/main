#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools

j = ''.join([
    ' --enable-pinentry-tty',
    ' --enable-pinentry-curses',
    ' --enable-pinentry-gnome3',
    ' --enable-pinentry-qt5 '
    ])

def setup():
    autotools.configure(j)

def build():
    autotools.make()

def install():
    autotools.install()

    # We're using pinentry-wrapper as additional file instead of upstream pinentry symlink.
    pisitools.remove("/usr/bin/pinentry")

    pisitools.dodoc("AUTHORS", "NEWS", "THANKS")
