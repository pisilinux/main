#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
import subprocess

WorkDir = "esbuild-%s" % get.srcVERSION()

def setup():
    # Go derleme ortam değişkenlerini ayarla
    shelltools.export("CGO_CPPFLAGS", "-I/usr/include")
    shelltools.export("CGO_CFLAGS", "-O2")
    shelltools.export("CGO_CXXFLAGS", "-O2")
    shelltools.export("CGO_LDFLAGS", "-L/usr/lib")
    shelltools.export("GOFLAGS", "-buildmode=pie -trimpath -ldflags=-linkmode=external -mod=readonly -modcacherw")

def build():
    # Go ile esbuild derle
    shelltools.system("go build \
        -trimpath \
        -buildmode=pie \
        -mod=readonly \
        -modcacherw \
        -ldflags \"-linkmode external -extldflags \\\"-Wl,-z,relro -Wl,-z,now\\\"\" \
        ./cmd/esbuild")

    # Node.js modüllerini oluştur
    shelltools.system("node scripts/esbuild.js ./esbuild --neutral")

def install():
    # esbuild ikili dosyasını kur
    pisitools.dobin("esbuild")
    shelltools.chmod(get.installDIR() + "/usr/bin/esbuild")
    # shelltools.system("chmod 755 %s/usr/bin/esbuild" % get.installDIR())

    # Node.js modüllerini kur
    # Node platform adını tespit et (örn. "linux-x64")
    node_platform = subprocess.check_output(
        ["node", "-p", "process.platform + '-' + process.arch"]
    ).strip()
    node_dir = "/usr/lib/node_modules"
    npm_dir = "%s/esbuild" % node_dir

    # npm/esbuild dizinini oluştur
    pisitools.insinto(npm_dir + "/lib", "npm/esbuild/lib/main.d.ts")
    pisitools.insinto(npm_dir + "/lib", "npm/esbuild/lib/main.js")
    pisitools.insinto(npm_dir + "/lib", "npm/esbuild/package.json")

    # @esbuild/platform modülünü kur
    esbuild_platform_dir = "%s/@esbuild/%s/bin" % (node_dir, node_platform)
    shelltools.system("mkdir -p %s%s" % (get.installDIR(), esbuild_platform_dir))
    pisitools.dosym("/usr/bin/esbuild", "%s/esbuild" % esbuild_platform_dir)

    pisitools.dodoc("LICENSE.md", "CHANGELOG-*", "README.md")
