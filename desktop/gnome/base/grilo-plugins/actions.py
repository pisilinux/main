#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import mesontools, pisitools

def setup():
    mesontools.configure("-Denable-shoutcast=no \
                            -Denable-bookmarks=yes \
                            -Denable-dleyna=yes \
                            -Denable-dmap=yes \
                            -Denable-filesystem=yes \
                            -Denable-flickr=yes \
                            -Denable-freebox=yes \
                            -Denable-gravatar=yes \
                            -Denable-lua-factory=yes \
                            -Denable-metadata-store=yes \
                            -Denable-podcasts=yes \
                            -Denable-tmdb=yes \
                            -Denable-youtube=yes \
                            -Denable-tracker=no \
                            -Denable-youtube=no \
                            -Denable-tracker3=yes")

def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.dodoc("AUTHORS", "COPYING", "README*", "NEWS")
