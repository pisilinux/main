#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

VERSION = "3.2.2"
BOOTSTRAP_DIR = "bootstrap"
BOOTSTRAP_COMPILER = (
    BOOTSTRAP_DIR + "/lib/fpc/" + VERSION + "/ppcx64"
)
INSTALL_DIR = get.installDIR()


def setup():
    shelltools.system("mkdir -p %s" % BOOTSTRAP_DIR)

    shelltools.system(
        'BINARY_ARCHIVE="$(find .. -type f '
        '-name binary.x86_64-linux.tar -print -quit)"; '
        'test -n "$BINARY_ARCHIVE"; '
        'tar -xf "$BINARY_ARCHIVE" -C %s'
        % BOOTSTRAP_DIR
    )

    shelltools.system(
        'for archive in %s/*.tar.gz; do '
        'tar -xzf "$archive" -C %s; '
        'done'
        % (BOOTSTRAP_DIR, BOOTSTRAP_DIR)
    )

    shelltools.system(
        "test -x %s" % BOOTSTRAP_COMPILER
    )


def build():
    shelltools.cd("fpcsrc/utils/fpcm")

    shelltools.system(
        'UNITDIRS="$(find ../../../%s/lib/fpc/%s/units/x86_64-linux '
        '-mindepth 1 -maxdepth 1 -type d -printf \'-Fu%%p \')"; '
        '../../../%s/lib/fpc/%s/ppcx64 -n $UNITDIRS -Fu. fpcmake.pp'
        % (
            BOOTSTRAP_DIR,
            VERSION,
            BOOTSTRAP_DIR,
            VERSION
        )
    )

    shelltools.cd("../../compiler")

    shelltools.system(
        "../utils/fpcm/fpcmake -Tall"
    )

    shelltools.cd("../..")

    shelltools.system(
        'make -j1 NOGDB=1 PP="$(pwd)/%s" build'
        % BOOTSTRAP_COMPILER
    )


def install():
    shelltools.system(
        'make -j1 NOGDB=1 PP="$(pwd)/%s" PREFIX=%s/usr install'
        % (BOOTSTRAP_COMPILER, INSTALL_DIR)
    )

    shelltools.system(
        'if [ -d "%s/usr/share/fpc-%s" ]; then '
        'mv "%s/usr/share/fpc-%s" "%s/usr/share/fpc"; '
        'fi'
        % (
            INSTALL_DIR,
            VERSION,
            INSTALL_DIR,
            VERSION,
            INSTALL_DIR
        )
    )

    shelltools.system(
        "mkdir -p %s/etc" % INSTALL_DIR
    )

    samplecfg = (
        INSTALL_DIR + "/usr/lib/fpc/" + VERSION + "/samplecfg"
    )

    shelltools.system(
        '"%s" "%s/usr/lib/fpc/%s" "%s/etc"'
        % (
            samplecfg,
            INSTALL_DIR,
            VERSION,
            INSTALL_DIR
        )
    )

    shelltools.system(
        'find "%s/etc" -type f -exec '
        'sed -i "s|%s||g" {} \\;'
        % (INSTALL_DIR, INSTALL_DIR)
    )

    pisitools.dosym(
        "/usr/lib/fpc/%s/ppcx64" % VERSION,
        "/usr/bin/ppcx64"
    )

    pisitools.insinto(
        "/usr/share/doc/fpc-3.2.2",
        "fpcsrc/rtl/COPYING.FPC"
    )

    shelltools.system(
        'if [ -d "%s/usr/man" ]; then '
        'mkdir -p "%s/usr/share"; '
        'mv "%s/usr/man" "%s/usr/share/"; '
        'fi'
        % (
            INSTALL_DIR,
            INSTALL_DIR,
            INSTALL_DIR,
            INSTALL_DIR
        )
    )