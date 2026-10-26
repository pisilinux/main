#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import python3modules, shelltools, pisitools, get



WorkDir="matplotlib-%s" % get.srcVERSION()

shelltools.export("SETUPTOOLS_SCM_PRETEND_VERSION","%s" % get.srcVERSION())

def setup():
    shelltools.system("""sed -i 's|"setuptools_scm>=7,<10"|"setuptools_scm"|' pyproject.toml""")
    # dodoc method cannot move LICENSE named dir, so i delete the directory
    # shelltools.unlinkDir("LICENSE")
    # pisitools.dosed("pyproject.toml", "LICENSE/LICENSE", deleteLine = True)

def build():
    # suppress compiler warnings:
    pisitools.cflags.add("-Wno-unused-but-set-variable -Wno-misleading-indentation -Wno-stringop-truncation -Wno-unused-function")
    # fix unused direct dependency analysis
    shelltools.export("LDSHARED", "x86_64-pc-linux-gnu-gcc -Wl,-O1,--as-needed -shared -lpthread -lbz2")
    python3modules.compile()

def install():
    shelltools.system("python3 -m installer --destdir='%s' dist/*.whl" % get.installDIR())
    pisitools.dodoc("LICENSE/*")
    # python3modules.install()
