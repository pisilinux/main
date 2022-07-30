#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
    shelltools.system("sed -i 's|$(datadir)/pixmaps|$(datadir)/icons/hicolor/64x64/apps|' src/mime/Makefile.{am,in}")
    shelltools.system("sed -i 's|$(datarootdir)/appdata|$(datarootdir)/metainfo|' Makefile.{am,in} src/plugins/contrib/appdata/Makefile.{am,in}")
    shelltools.system("./bootstrap")
    #shelltools.system("./bootstrap")
    #autotools.autoreconf("-vif")
    #plugins = "AutoVersioning,BrowseTracker,byogames,Cccc,CppCheck,cbkoders,codesnippets,codestat,copystrings,dragscroll,envvars,headerfixup,help,hexeditor,incsearch,keybinder,MouseSap,profiler,regex,exporter,symtab,Valgrind"
    # suppress compiler warnings
    pisitools.cflags.add("-Wno-unused-result")
    pisitools.cxxflags.add("-Wno-unused-result -Wno-deprecated-declarations -Wno-stringop-overflow")
    autotools.configure("--with-wx-config=/usr/bin/wx-config-gtk3 \
                         --with-contrib-plugins=all \
                         --enable-unicode\
                        ")

    # disable rpath
    pisitools.dosed("libtool", "^hardcode_libdir_flag_spec=.*", "hardcode_libdir_flag_spec=\"\"")
    pisitools.dosed("libtool", "^runpath_var=LD_RUN_PATH", "runpath_var=DIE_RPATH_DIE")
    
    # fix unused direct dependency analysis
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")


def build():    
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("COPYING", "README")
