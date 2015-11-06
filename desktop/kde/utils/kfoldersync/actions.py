#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import kde5
from pisi.actionsapi import pisitools

# if pisi can't find source directory, see /var/pisi/kfoldersync/work/ and:
# WorkDir="kfoldersync-"+ get.srcVERSION() +"/sub_project_dir/"

def setup():
    kde5.configure()

def build():
    kde5.make()

def install():
    kde5.install()

# Take a look at the source folder for these file as documentation.
    pisitools.dodoc("COPYING", "README")

# If there is no install rule for a runnable binary, you can 
# install it to binary directory.
#    pisitools.dobin("kfoldersync")

# You can use these as variables, they will replace GUI values before build.
# Package Name : kfoldersync
# Version : 3.0.0
# Summary : Folder synchronization and backup tool for KDE

# For more information, you can look at the Actions API
# from the Help menu and toolbar.
