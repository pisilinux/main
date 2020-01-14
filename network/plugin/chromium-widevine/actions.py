#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "."
NoStrip = ["/"]

Release = "-1"

def setup():
    shelltools.system("ar xf google-chrome-stable_current_amd64.deb")
    shelltools.system("tar xvf %s/data.tar.xz --exclude=usr/share/gnome-control-center --exclude=usr/bin --exclude=etc" %get.workDIR())
    shelltools.chmod(get.workDIR() + "/opt/google/chrome/*", 0755)

def install():
    pisitools.insinto("/usr/lib/chromium-browser/WidevineCdm", "./opt/google/chrome/WidevineCdm/*")
    pisitools.dosym("/usr/lib/chromium-browser/WidevineCdm", "/usr/lib/chromium-dev/WidevineCdm")
