#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import kde6
#from pisi.actionsapi import pisitools

# if pisi can't find source directory, see /var/pisi/kirigami/work/ and:
# WorkDir="kirigami-"+ get.srcVERSION() +"/sub_project_dir/"

def setup():
    kde6.configure()

def build():
    kde6.make()

def install():
    kde6.install()

# Take a look at the source folder for these file as documentation.
#    pisitools.dodoc("AUTHORS", "BUGS", "ChangeLog", "COPYING", "README")

# If there is no install rule for a runnable binary, you can 
# install it to binary directory.
#    pisitools.dobin("kirigami")

# You can use these as variables, they will replace GUI values before build.
# Package Name : kirigami
# Version : 2.2.0
# Summary : A set of QML components for mobile/desktop convergent applications made by KDE

# For more information, you can look at the Actions API
# from the Help menu and toolbar.
