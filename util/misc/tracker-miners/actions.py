#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import mesontools
from pisi.actionsapi import pisitools

def setup():
    mesontools.configure("-Dtracker_core=system \
                          -Dextract=true \
                          -Dfunctional_tests=false \
                          -Dcue=enabled \
                          -Dexif=enabled \
                          -Dgif=enabled \
                          -Dgsf=enabled \
                          -Diptc=enabled \
                          -Diso=enabled \
                          -Djpeg=enabled \
                          -Dpdf=enabled \
                          -Dplaylist=enabled \
                          -Dpng=enabled \
                          -Draw=enabled \
                          -Dtiff=enabled \
                          -Dxml=enabled \
                          -Dxmp=enabled \
                          -Dxps=enabled \
                          -Dminer_rss=false \
                          -Dbattery_detection=upower \
                          -Dcharset_detection=icu \
                          -Dgeneric_media_extractor=gstreamer \
                          -Dgstreamer_backend=discoverer \
                          -Dnetwork_manager=enabled \
                          -Dsystemd_user_services=false \
                          -Dsystemd_user_services_dir=no")

def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.dodoc("AUTHORS", "COPYING*", "HACKING.md", "MAINTAINERS", "NEWS", "README*")
