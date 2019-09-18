#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import kde5
from pisi.actionsapi import pisitools

# if pisi can't find source directory, see /var/pisi/kphotoalbum/work/ and:
# WorkDir="kphotoalbum-"+ get.srcVERSION() +"/sub_project_dir/"

def setup():
    kde5.configure()

def build():
    kde5.make()

def install():
    kde5.install()

    pisitools.dodoc("ChangeLog", "COPYING", "README*")

