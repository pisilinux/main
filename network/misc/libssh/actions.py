#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
    # fix unittest error
    pisitools.dosed("tests/unittests/torture_misc.c", "cmocka_unit_test\(torture_path_expand_tilde_unix\),", "")
    pisitools.dosed("tests/unittests/CMakeLists.txt", "torture_config", "")

    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure("-DCMAKE_INSTALL_LIBDIR=lib \
                          -DCMAKE_BUILD_TYPE=Release \
                          -DUNIT_TESTING=ON \
                          -DWITH_NACL=OFF \
                          -DWITH_GSSAPI=OFF", sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()
    autotools.make("docs")
    
def check():
    shelltools.cd("build")
    autotools.make("test")

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    #pisitools.doman("doc/man/*/*")
    pisitools.dohtml("doc/html/*")

    shelltools.cd("..")
    pisitools.dodoc("COPYING", "README*")
