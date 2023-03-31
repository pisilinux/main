#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools, autotools, get

def build():
    autotools.make("PREFIX='/usr'")
    #shelltools.system("sed -n '4,25p' include/ffnvcodec/nvEncodeAPI.h > LICENSE")
    #shelltools.system("sed -i '1,22s/^.\{,3\}//' LICENSE")

def install():
    autotools.rawInstall("PREFIX='/usr' DESTDIR=%s" % get.installDIR())
