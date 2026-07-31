#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "kotlinc"

def setup():
    if shelltools.can_access_file("bin/kotlinc"):
        pisitools.dosed(
            "bin/kotlinc",
            '^KOTLIN_HOME=.*',
            'KOTLIN_HOME=/usr/share/kotlin'
        )

def install():
    pisitools.dobin("bin/kotlin")
    pisitools.dobin("bin/kotlinc")
    pisitools.dobin("bin/kotlinc-js")
    pisitools.dobin("bin/kotlinc-jvm")

    pisitools.insinto("/usr/share/kotlin/lib", "lib/*")
    pisitools.insinto("/usr/share/kotlin", "build.txt")

    pisitools.dodoc("license/LICENSE.txt", "license/NOTICE.txt")
    pisitools.insinto("/usr/share/doc/kotlin/third_party", "license/third_party/*")
