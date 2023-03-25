#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools, autotools, pisitools, get

i = ''.join([
    ' --enable-nls',
    ' --enable-posix',
    ' --enable-regex',
    ' --with-threads',
    ' --with-modules',
    ' --disable-rpath',
    ' --disable-static',
    ' --enable-networking',
    ' --program-suffix=3.0',
    ' --disable-error-on-warning '
    ])

def setup():
    autotools.configure(i)

    # fix unused direct dependency analysis
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def check():
    autotools.make("check")
    #pass

def install():
    autotools.install()

    # remove scm file
    pisitools.remove("/usr/lib/libguile-3.0.so.*.scm")

    # rename some info files to avoid conflicts
    pisitools.remove("/usr/share/info/r5rs.info")
    for t in shelltools.ls("%s/usr/share/info" % get.installDIR()):
        pisitools.rename("/usr/share/info/%s" % t, t.replace("guile", "guile3"))

    pisitools.dodoc("AUTHORS", "NEWS", "THANKS")
