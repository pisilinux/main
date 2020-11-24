#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
import os

WorkDir="libdbusmenu-%s" % get.srcVERSION()
ver = get.srcVERSION()

options = "--disable-dumper  \
           --disable-static  \
           --enable-vala=no  \
           --enable-gtk-doc  \
           --disable-silent-rules \
            --disable-scrollkeeper \
            --enable-introspection=yes \
            --disable-tests \
            --disable-tests"
           


def setup():
        shelltools.cd("%s/libdbusmenu-%s" %(get.workDIR(), ver))
        shelltools.system("sed -i 's/-Werror//' libdbusmenu-*/Makefile.{am,in}")
        shelltools.cd("..")
        shelltools.system("mkdir libdbusmenu-gtk2")
        shelltools.system("mkdir libdbusmenu-gtk3")
        shelltools.system("cp -ra libdbusmenu-16.04.0/* /var/pisi/libdbusmenu-16.04.0-1/work/libdbusmenu-gtk2")
        shelltools.system("cp -ra libdbusmenu-16.04.0/* /var/pisi/libdbusmenu-16.04.0-1/work/libdbusmenu-gtk3")
   
   
def build():
    shelltools.export("HAVE_VALGRIND_TRUE", "#")
    shelltools.export("HAVE_VALGRIND_FALSE", " ")
    shelltools.cd("%s/libdbusmenu-%s" %(get.workDIR(), ver))
    autotools.configure("%s" % options)
    
    shelltools.cd("%s/libdbusmenu-%s" % (get.workDIR(), 'gtk3'))
    autotools.configure("%s --with-gtk=3" % options)

    shelltools.cd("%s/libdbusmenu-%s" % (get.workDIR(), 'gtk2'))
    autotools.configure("%s --with-gtk=2" % options)
    
def install():
    shelltools.cd("%s/libdbusmenu-%s" %(get.workDIR(), ver))
    autotools.rawInstall("-C libdbusmenu-glib DESTDIR=%s" % get.installDIR())
    autotools.rawInstall("-C tools DESTDIR=%s" % get.installDIR())
    
    shelltools.cd("%s/libdbusmenu-%s" %(get.workDIR(), 'gtk2'))
    autotools.rawInstall("-C libdbusmenu-glib DESTDIR=%s" % get.installDIR())
    autotools.rawInstall("-C libdbusmenu-gtk DESTDIR=%s" % get.installDIR())
    
    
    shelltools.cd("%s/libdbusmenu-%s" %(get.workDIR(), 'gtk3'))
    autotools.rawInstall("-C libdbusmenu-glib DESTDIR=%s" % get.installDIR())
    autotools.rawInstall("-C libdbusmenu-gtk DESTDIR=%s" % get.installDIR())
    
    shelltools.cd("%s/libdbusmenu-%s" % (get.workDIR(), ver))
    pisitools.dodoc("AUTHORS", "COPYING*", "README", "NEWS")
