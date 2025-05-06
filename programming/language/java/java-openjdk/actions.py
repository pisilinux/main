#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

import subprocess
from pisi.actionsapi import shelltools, pisitools, autotools
from pisi.actionsapi import get
from pisi.util import join_path

_, _, _, update = get.srcVERSION().split('.')
#jobs = "-j"+ subprocess.check_output("nproc 2>/dev/null", shell=True).rstrip("\n")
# jobs = subprocess.check_output("nproc 2>/dev/null", shell=True).rstrip("\n")
jobs = "-j" + subprocess.check_output("nproc 2>/dev/null", shell=True).decode().strip()

jvm_dir = '/usr/lib/jvm/java-openjdk'
img_dir = 'build/linux-%s-server-release/images' % get.ARCH()

cflags = get.CFLAGS()
cxxflags = get.CXXFLAGS()
ldflags = get.LDFLAGS()

pisitools.cflags.reset()
pisitools.cxxflags.reset()
pisitools.ldflags.reset()


def setup():
    shelltools.system(
        'bash configure \
        --with-version-build="%s" \
        --with-version-pre="" \
        --with-version-opt="" \
        --with-stdc++lib=dynamic \
        --with-extra-cflags="%s -fcommon" \
        --with-extra-cxxflags="%s -fcommon" \
        --with-extra-ldflags="%s" \
        --with-libjpeg=system \
        --with-giflib=system \
        --with-libpng=system \
        --with-lcms=system \
        --with-zlib=system \
        --with-jvm-features=zgc \
        --with-boot-jdk="%s" \
        --enable-unlimited-crypto \
        --disable-warnings-as-errors \
        --with-num-cores="%s"' % (update, cflags, cxxflags, ldflags, jvm_dir, jobs)
    )


def build():
    shelltools.system("make JOBS=%s images legacy-jre-image docs" % jobs)
    shelltools.system("find '%s' -iname '*.so' -exec chmod +x {} \\;" % img_dir)


# def check():
#     shelltools.system("make JOBS=%s -k check" % jobs)


def install():
    # Binaries
    pisitools.insinto(jvm_dir, join_path(img_dir, 'jdk/bin'))

    # Libraries
    # pisitools.insinto(jvm_dir, join_path(img_dir, 'jre/lib'))
    pisitools.insinto(jvm_dir, join_path(img_dir, 'jdk/lib'))

    # Headers
    pisitools.insinto(jvm_dir, join_path(img_dir, 'jdk/include'))

    # Others
    pisitools.insinto(jvm_dir, join_path(img_dir, 'jdk/release'))
    pisitools.insinto(join_path(jvm_dir, 'lib'), join_path(img_dir, 'jdk/lib/modules'))
    pisitools.insinto(jvm_dir, join_path(img_dir, 'jdk/demo'))
    pisitools.insinto(jvm_dir, join_path(img_dir, 'jdk/jmods'))

    # Configurations
    pisitools.insinto('/etc/java-openjdk', join_path(img_dir, 'jre/conf/*'))
    pisitools.dosym('/etc/java-openjdk', join_path(jvm_dir, 'conf'))

    # Man pages
    pisitools.doman(join_path(img_dir, 'jdk/man/man1/*'))

    # Change man page file names to prevent conflict with other Java packages.
    for man_file in shelltools.ls(join_path(get.installDIR(), 'usr/share/man/man1')):
        pisitools.domove(
            '/usr/share/man/man1/%s' % man_file,
            '/usr/share/man/man1',
            '%s-openjdk24.0' % man_file.replace('.1', '')
        )

    # Documentations
    pisitools.insinto(join_path('/', get.docDIR(), 'java-openjdk'), join_path(img_dir, 'docs/*'))

    # Licenses
    pisitools.insinto('/usr/share/licenses/java-openjdk', join_path(img_dir, 'jre/legal/*'))
    pisitools.dosym('/usr/share/licenses/java-openjdk', join_path(jvm_dir, 'legal'))

    pisitools.remove("%s/lib/security/cacerts" % jvm_dir)
    pisitools.dosym("/etc/ssl/certs/java/cacerts", "%s/lib/security/cacerts" % jvm_dir)
    
    shelltools.system("rm -rf %s/%s/bin/*.debuginfo" %(get.installDIR(), jvm_dir))

    # Icons
    for size in [16, 24, 32, 48]:
        pisitools.insinto(
            "/usr/share/icons/hicolor/{size}x{size}/apps/".format(size=size),
            "src/java.desktop/unix/classes/sun/awt/X11/java-icon%s.png" % size,
            "java-openjdk.png"
        )
