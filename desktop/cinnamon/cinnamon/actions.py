#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt


from pisi.actionsapi import mesontools, shelltools, pisitools

def setup():
    pisitools.dosed("files/usr/share/cinnamon/cinnamon-settings/modules/cs_notifications.py", "0.7", "0.8")
    #shelltools.system("sed -i 's/mintinstall.desktop/org.gnome.Software.desktop/' data/org.cinnamon.gschema.xml")
    #shelltools.system("sed -i 's/'REQUIRED', '/&polkit-cinnamon-authentication-agent-1;/' meson.build || die")
    #shelltools.system("sed -i 's/RequiredComponents=\(.*\)$/RequiredComponents=\1polkit-gnome-authentication-agent-1;/' \
      #cinnamon*.session.in")
    #pisitools.dosed("cinnamon*.session.in","=cinnamon","=polkit-gnome-authentication-agent-1;cinnamon")
    mesontools.configure("--prefix=/usr \
                          --sysconfdir=/etc \
                          --libexecdir=/usr/lib/cinnamon \
                          --localstatedir=/var")

def build():
    mesontools.build()
    
def check():
    mesontools.build("test")

def install():
    mesontools.install()
    #pisitools.remove("/etc/xdg/menus/cinnamon-applications-merged")
    pisitools.dodoc("AUTHORS", "COPYING", "README*")
