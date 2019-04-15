#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

# if pisi can't find source directory, see /var/pisi/yarock/work/ and:
# WorkDir="yarock-"+ get.srcVERSION() +"/sub_project_dir/"

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure("-DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DENABLE_VLC=OFF \
    -DENABLE_MPV=ON \
    -DENABLE_PHONON=ON", sourceDir = '..')

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.install()
    shelltools.cd("..")

# Take a look at the source folder for these file as documentation.
    pisitools.dodoc("CHANGES.md", \
    "COPYING", \
    "README.md")

# If there is no install rule for a runnable binary, you can 
# install it to binary directory.
#    pisitools.dobin("yarock")

# You can use these as variables, they will replace GUI values before build.
# Package Name : yarock
# Version : 1.4.0
# Summary : Qt Modern Music Player with collection browse based on cover art

# For more information, you can look at the Actions API
# from the Help menu and toolbar.
