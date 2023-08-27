#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

# if pisi can't find source directory, see /var/pisi/libaacs/work/ and:
# WorkDir="libaacs-"+ get.srcVERSION() +"/sub_project_dir/"

def setup():
    autotools.autoreconf("-fiv")
    autotools.configure("--disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

# Take a look at the source folder for these file as documentation.
    pisitools.dodoc("COPYING", "README.md")

# If there is no install rule for a runnable binary, you can 
# install it to binary directory.
#    pisitools.dobin("libaacs")
