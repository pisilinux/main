#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
  autotools.rawConfigure("--prefix=/usr")
 
def build():
  autotools.make()
  
def install():
  autotools.install()
  pisitools.dodoc("AUTHORS","ChangeLog","COPYING","INSTALL","NEWS","README")
