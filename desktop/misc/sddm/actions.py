#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-B build -DCMAKE_INSTALL_PREFIX=/usr \
                          -DCMAKE_BUILD_TYPE=Release \
                          -DDBUS_CONFIG_FILENAME=sddm_org.freedesktop.DisplayManager.conf \
                          -DDBUS_CONFIG_DIR=/usr/share/dbus-1/system.d \
                          -DNO_SYSTEMD=ON \
                          -DUSE_ELOGIND=ON \
                          -DBUILD_WITH_QT6=ON \
                          -DCMAKE_INSTALL_LIBEXECDIR=/usr/lib/sddm \
                          -DBUILD_MAN_PAGES=ON")

    cmaketools.configure("-B build5 -DCMAKE_INSTALL_PREFIX=/usr")

def build():
    cmaketools.make("-C build")

    cmaketools.make("-C build5/src/greeter")
    cmaketools.make("-C build5/components")

def install():
    cmaketools.install("-C build")

    cmaketools.install("-C build5/src/greeter")
    cmaketools.install("-C build5/components")

    shelltools.system('sed -i "s@system-local-login@system-login@" ' + get.installDIR() + "/etc/pam.d/sddm-autologin")

    # pisitools.insinto("/usr/share/sddm/themes/Sweet-Cat", "../Sweet-Cat-0.1/*")
    pisitools.insinto("/usr/share/sddm/themes/pisilinux24", "sddm-pisilinux24-1.2/*")
    # pisitools.dosym("/usr/bin/sddm-greeter-qt6", "/usr/bin/sddm-greeter")

    pisitools.dodoc("LICENSE")

    ## If you don't like to see any character at all not even while being entered set this to true.
    #pisitools.dosed("%s/usr/share/sddm/themes/Sweet-Cat/theme.conf" % get.installDIR(), 'ForceHideCompletePassword="false"', 'ForceHideCompletePassword="true"')
