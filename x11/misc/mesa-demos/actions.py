# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import mesontools

demos_dir = "/usr/lib/mesa/demos"
demos_dir_emul32 = "/usr/lib32/mesa/demos"

def setup():
    # autotools.autoreconf("-fvi")
    options = "-Dwith-system-data-files=true \
               --bindir=%s" % (demos_dir_emul32 if get.buildTYPE() == "emul32" else demos_dir)

    mesontools.configure(options)
    # pisitools.dosed("libtool","( -shared )", " -Wl,--as-needed\\1")

def build():
    mesontools.build()
    # autotools.make()

def install():
    mesontools.install()
    # autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    if get.buildTYPE() == "emul32":
        for util in ("glxgears", "glxinfo"):
            pisitools.domove("%s/%s" % (demos_dir_emul32, util), "/usr/bin/", "%s32" % util)
        return

    for util in ("glxgears", "glxinfo", "eglinfo"):
        pisitools.domove("%s/%s" % (demos_dir, util), "/usr/bin/")
        pisitools.dobin("build/src/egl/opengl/xeglgears")
