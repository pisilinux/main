#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import qt5
#from pisi.actionsapi import pisitools

# if pisi can't find source directory, see /var/pisi/ktageditor/work/ and:
# WorkDir="ktageditor-"+ get.srcVERSION() +"/sub_project_dir/"

def setup():
    qt5.configure()

def build():
    qt5.make()

def install():
    qt5.install()

# Take a look at the source folder for these file as documentation.
#    pisitools.dodoc("AUTHORS", "BUGS", "ChangeLog", "COPYING", "README")

# If there is no install rule for a runnable binary, you can 
# install it to binary directory.
#    pisitools.dobin("ktageditor")

# You can use these as variables, they will replace GUI values before build.
# Package Name : ktageditor
# Version : 0.2.0
# Summary : KTag Editor is an Audio tag editor developed in Qt5 framework.

# For more information, you can look at the Actions API
# from the Help menu and toolbar.
