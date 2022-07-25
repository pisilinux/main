#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import mesontools, pisitools

def setup():
    mesontools.configure("--prefix=/usr \
                          --sysconfdir=/etc \
                          --libexecdir=/usr/lib/cinnamon-control-center \
                          --localstatedir=/var \
                          --buildtype=plain")

    #pisitools.dosed("libtool", "( -shared )", " -Wl,-O1,--as-needed\\1")
    #pisitools.dosed("libtool", '(    if test "\$export_dynamic" = yes && test -n "\$export_dynamic_flag_spec"; then)', '      func_append compile_command " -Wl,-O1,--as-needed"\n      func_append finalize_command " -Wl,-O1,--as-needed"\n\\1')

def build():
    mesontools.build()

def install():
    mesontools.install()

    pisitools.dodoc("AUTHORS", "ChangeLog", "README*", "NEWS")
