#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file https://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools, get, pisitools, shelltools

#def setup():
    #autotools.configure()

def build():
    autotools.make()

def install():
    pisitools.insinto("/etc/X11/Xsession.d","%s/%s-%s/70im-config_launch" % (get.workDIR(), get.srcNAME(), get.srcVERSION()))
    pisitools.insinto("/usr/share/im-config/data","%s/%s-%s/data/*" % (get.workDIR(), get.srcNAME(), get.srcVERSION()))
    pisitools.insinto("/etc/default","%s/%s-%s/default/im-config-Ubuntu" % (get.workDIR(), get.srcNAME(), get.srcVERSION()), "im-config")
    pisitools.insinto("/usr/bin","%s/%s-%s/im-config" % (get.workDIR(), get.srcNAME(), get.srcVERSION()))
    pisitools.insinto("/usr/share/applications","%s/%s-%s/im-config.desktop" % (get.workDIR(), get.srcNAME(), get.srcVERSION()))
    pisitools.insinto("/etc/profile.d","%s/%s-%s/im-config_wayland.sh" % (get.workDIR(), get.srcNAME(), get.srcVERSION()))
    pisitools.insinto("/usr/bin","%s/%s-%s/im-launch" % (get.workDIR(), get.srcNAME(), get.srcVERSION()))
    pisitools.insinto("/etc/xdg/autostart","%s/%s-%s/im-launch.desktop" % (get.workDIR(), get.srcNAME(), get.srcVERSION()))
    pisitools.insinto("/usr/share/locale","%s/%s-%s/po/locale/*" % (get.workDIR(), get.srcNAME(), get.srcVERSION()))
    pisitools.insinto("/usr/share/im-config","%s/%s-%s/share/im-config.common" % (get.workDIR(), get.srcNAME(), get.srcVERSION()))
    pisitools.insinto("/usr/share/im-config","%s/%s-%s/share/xinputrc.common" % (get.workDIR(), get.srcNAME(), get.srcVERSION()))
    pisitools.insinto("/etc/X11/xinit","%s/%s-%s/xinputrc" % (get.workDIR(), get.srcNAME(), get.srcVERSION()))
