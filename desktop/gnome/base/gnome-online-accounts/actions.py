#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-documentation \
                         --enable-backend \
                         --enable-google \
                         --enable-kerberos \
                         --enable-flickr \
                         --enable-facebook \
                         --disable-static \
                         --enable-exchange \
                         --enable-imap-smtp \
                         --enable-owncloud \
                         --enable-windows-live \
                         --enable-pocket \
                         --enable-lastfm \
                         --enable-media-server \
                         --enable-foursquare \
                         --enable-twitter \
                         --enable-yahoo")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("COPYING", "NEWS", "README")
