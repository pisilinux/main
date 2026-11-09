#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def build():
    shelltools.system(
        "make FPC=/usr/bin/fpc OPT='-gl -gw -Crtoi' LCL_PLATFORM=qt5 bigide"
    )

    shelltools.move(
        "%s/lazarus" % get.curDIR(),
        "%s/lazarus-qt5" % get.curDIR()
    )
    shelltools.move(
        "%s/startlazarus" % get.curDIR(),
        "%s/startlazarus-qt5" % get.curDIR()
    )

    shelltools.system(
        "make FPC=/usr/bin/fpc OPT='-gl -gw -Crtoi' LCL_PLATFORM=qt6 bigide"
    )

    shelltools.move(
        "%s/lazarus" % get.curDIR(),
        "%s/lazarus-qt6" % get.curDIR()
    )
    shelltools.move(
        "%s/startlazarus" % get.curDIR(),
        "%s/startlazarus-qt6" % get.curDIR()
    )

def install():
    pisitools.dodir("/usr/lib/lazarus")
    pisitools.dodir("/usr/lib/lazarus-qt5")
    pisitools.dodir("/usr/lib/lazarus-qt6")
    pisitools.dodir("/usr/share/doc")
    pisitools.dodir("/usr/share/licenses/lazarus")

    shelltools.system(
        "rsync -a "
        "--exclude='CVS' "
        "--exclude='.cvsignore' "
        "--exclude='*.ppw' "
        "--exclude='*.ppl' "
        "--exclude='*.ow' "
        "--exclude='*.a' "
        "--exclude='*.rst' "
        "--exclude='.#*' "
        "--exclude='*.~*' "
        "--exclude='*.bak' "
        "--exclude='*.orig' "
        "--exclude='*.rej' "
        "--exclude='.xvpics' "
        "--exclude='killme*' "
        "--exclude='.gdb_hist*' "
        "--exclude='COPYING*' "
        "--exclude='*.app' "
        "--exclude='tools/install' "
        "--exclude='/lazarus-qt5' "
        "--exclude='/startlazarus-qt5' "
        "--exclude='/lazarus-qt6' "
        "--exclude='/startlazarus-qt6' "
        "'%s/' '%s/usr/lib/lazarus/'"
        % (get.curDIR(), get.installDIR())
    )

    pisitools.doman("install/man/man1/*")

    shelltools.move(
        "%s/usr/lib/lazarus/docs" % get.installDIR(),
        "%s/usr/share/doc/lazarus" % get.installDIR()
    )

    pisitools.dodir("/usr/lib/lazarus/docs")

    pisitools.dosym(
        "/usr/share/doc/lazarus/chm",
        "/usr/lib/lazarus/docs/html"
    )

    pisitools.dosym(
        "/usr/share/doc/lazarus/lazdoc.css",
        "/usr/lib/lazarus/docs/lazdoc.css"
    )

    pisitools.insinto(
        "/usr/share/licenses/lazarus",
        "COPYING*"
    )

    pisitools.dosym(
        "/usr/lib/lazarus/lazbuild",
        "/usr/bin/lazbuild"
    )

    pisitools.insinto(
        "/usr/lib/lazarus-qt5",
        "lazarus-qt5",
        "lazarus"
    )

    pisitools.insinto(
        "/usr/lib/lazarus-qt5",
        "startlazarus-qt5",
        "startlazarus"
    )

    pisitools.dosym(
        "/usr/lib/lazarus-qt5/lazarus",
        "/usr/bin/lazarus-qt5"
    )

    pisitools.dosym(
        "/usr/lib/lazarus-qt5/startlazarus",
        "/usr/bin/startlazarus-qt5"
    )

    pisitools.insinto(
        "/usr/lib/lazarus-qt6",
        "lazarus-qt6",
        "lazarus"
    )

    pisitools.insinto(
        "/usr/lib/lazarus-qt6",
        "startlazarus-qt6",
        "startlazarus"
    )

    pisitools.dosym(
        "/usr/lib/lazarus-qt6/lazarus",
        "/usr/bin/lazarus"
    )

    pisitools.dosym(
        "/usr/lib/lazarus-qt6/startlazarus",
        "/usr/bin/startlazarus"
    )

    pisitools.dosym(
        "/usr/lib/lazarus-qt6/lazarus",
        "/usr/bin/lazarus-qt6"
    )

    pisitools.dosym(
        "/usr/lib/lazarus-qt6/startlazarus",
        "/usr/bin/startlazarus-qt6"
    )

    pisitools.insinto(
        "/usr/share/applications",
        "install/lazarus.desktop",
        "lazarus-qt5.desktop"
    )

    shelltools.system(
        "sed -i "
        "-e 's|Categories=.*|Categories=IDE;Development;|' "
        "-e 's|Exec=.*|Exec=lazarus-qt5|' "
        "-e 's|Icon=.*|Icon=lazarus-qt5|' "
        "'%s/usr/share/applications/lazarus-qt5.desktop'"
        % get.installDIR()
    )

    pisitools.insinto(
        "/usr/share/pixmaps",
        "images/ide_icon48x48.png",
        "lazarus-qt5.png"
    )

    pisitools.insinto(
        "/usr/share/applications",
        "install/lazarus.desktop",
        "lazarus.desktop"
    )

    shelltools.system(
        "sed -i "
        "-e 's|Categories=.*|Categories=IDE;Development;|' "
        "-e 's|Exec=.*|Exec=lazarus|' "
        "-e 's|Icon=.*|Icon=lazarus|' "
        "'%s/usr/share/applications/lazarus.desktop'"
        % get.installDIR()
    )

    pisitools.insinto(
        "/usr/share/pixmaps",
        "images/ide_icon48x48.png",
        "lazarus.png"
    )