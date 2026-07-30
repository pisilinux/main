#!/usr/bin/python3

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():

    pisitools.dosed("AppImage/com.github.d4nj1.tlpui.appdata.xml", 
                    "com.github.d4nj1.tlpui.desktop", 
                    "tlpui.desktop")

def build():

    shelltools.system("python3 -m build --wheel --no-isolation")

def install():

    shelltools.system("python3 -m installer --destdir=%s dist/*.whl" % get.installDIR())

    pisitools.insinto("/usr/share/applications", "tlpui.desktop")
    pisitools.insinto("/usr/share/metainfo", "AppImage/com.github.d4nj1.tlpui.appdata.xml")

    sizes = ["16", "32", "48", "64", "96", "128", "256"]
    for s in sizes:
        pisitools.insinto("/usr/share/icons/hicolor/%sx%s/apps" % (s, s), 
                          "tlpui/icons/themeable/hicolor/%sx%s/apps/tlpui.png" % (s, s))

    pisitools.insinto("/usr/share/icons/hicolor/scalable/apps", "tlpui/icons/themeable/hicolor/scalable/apps/tlpui.svg")

    pisitools.dodoc("README.md", "LICENSE.md", "COPYING.md")
