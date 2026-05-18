#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.system("""sed -i 's|Fancy GNU/Linux 2023.3 LTS "Venomous Vole"|Pisi GNU/Linux 2.4.3 LTS "Pisi Linux"|g' src/branding/default/branding.desc""")
    shelltools.system("sed -i 's|2023.3|2.4.3|g' src/branding/default/branding.desc")
    shelltools.system("sed -i 's|FancyGL|Pisilinux|g' src/branding/default/branding.desc")

    shelltools.system("sed -i 's|backend: dummy|backend: pisi|g' src/modules/packages/packages.conf")
    shelltools.system("sed -i 's|systemctl -i reboot|shutdown -r now|g' src/modules/finished/finished.conf")

    shelltools.makedirs("build")
    shelltools.cd("build")
    
    cmaketools.configure("-DCMAKE_BUILD_TYPE=Debug \
                          -DCMAKE_INSTALL_PREFIX=/usr \
                          -DCMAKE_INSTALL_LIBDIR=lib \
                          -DWITH_PYTHONQT=OFF \
                          -DINSTALL_CONFIG=ON \
                          -DWITH_QT6=ON \
                          -DWITH_QT5=OFF \
                          -DWITH_KF5DBus=OFF \
                          -DWITH_CRASHREPORTER=ON", \
                          sourceDir=".." )
                          # -DSKIP_MODULES='bootldr bootloader license mnt notesqml oemid preservefiles partitionq' \

def build():
    shelltools.cd("build")
    
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.install()
    
    #pisitools.insinto("/usr/share/calamares", "../settings.conf")
    #pisitools.insinto("/usr/share/calamares/modules", "src/modules/machineid/machineid.conf")
    
    #dbus configuration for pisi
    pisitools.dosed("%s/usr/share/calamares/modules/machineid.conf" % get.installDIR(), "systemd: true", "systemd: false")
    pisitools.dosed("%s/usr/share/calamares/modules/machineid.conf" % get.installDIR(), "symlink: true", "symlink: false")

    pisitools.dosed("%s/usr/share/calamares/modules/removeuser.conf" % get.installDIR(), "username: live", "username: pisi")

    pisitools.dosym("/usr/share/icons/hicolor/scalable/apps/calamares.svg", "/usr/share/pixmaps/calamares.svg")
    
    
    
    pisitools.dodoc("../README.*")
