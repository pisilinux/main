#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

import os

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "rustdesk-1.4.9"

FLUTTER_VERSION = "3.24.5"
HBB_COMMIT = "7e1c392c62d39c364127307cd408421dd5f8cfb0"
FRB_VERSION = "1.80.1"
VCPKG_COMMIT = "120deac3062162151622ca4860575a33844ba10b"

AUX_CACHE = "/var/tmp/rustdesk-aux"

MKVPARSER_PATCH = """--- mkvparser.cc.old	2025-05-05 16:41:32.480450346 -0400
+++ mkvparser.cc	2025-05-05 16:44:56.578245385 -0400
@@ -16,6 +16,7 @@
 #include <cfloat>
 #include <climits>
 #include <cmath>
+#include <cstdint>
 #include <cstring>
 #include <memory>
 #include <new>
"""


def _aux(name, url):
    shelltools.makedirs(AUX_CACHE)
    if not os.path.exists(os.path.join(AUX_CACHE, name)):
        shelltools.system("curl -L -o %s/%s %s" % (AUX_CACHE, name, url))


def setup():
    # hbb_common submodule (not included in the tag tarball)
    _aux("hbb_common.tar.gz", "https://github.com/rustdesk/hbb_common/archive/%s.tar.gz" % HBB_COMMIT)
    shelltools.system("tar xf %s/hbb_common.tar.gz -C libs/" % AUX_CACHE)
    shelltools.system("rm -rf libs/hbb_common")
    shelltools.system("mv libs/hbb_common-%s libs/hbb_common" % HBB_COMMIT)

    # Flutter SDK -- extract as a SIBLING of the source tree. The rustdesk app
    # lives in a directory named "flutter" too; extracting the SDK into the
    # source root would merge the SDK files into the app package and break
    # build_runner/freezed analysis.
    _aux("flutter.tar.xz", "https://storage.googleapis.com/flutter_infra_release/releases/stable/linux/flutter_linux_%s-stable.tar.xz" % FLUTTER_VERSION)
    shelltools.system("tar xf %s/flutter.tar.xz -C %s" % (AUX_CACHE, get.workDIR()))

    # flutter_rust_bridge
    _aux("frb.tar.gz", "https://github.com/fzyzcjy/flutter_rust_bridge/archive/refs/tags/v%s.tar.gz" % FRB_VERSION)
    shelltools.system("tar xf %s/frb.tar.gz" % AUX_CACHE)
    shelltools.system("ln -sf flutter_rust_bridge-%s flutter_rust_bridge" % FRB_VERSION)

    # vcpkg + rustdesk overlay ports
    _aux("vcpkg.tar.gz", "https://github.com/microsoft/vcpkg/archive/%s.tar.gz" % VCPKG_COMMIT)
    shelltools.system("tar xf %s/vcpkg.tar.gz" % AUX_CACHE)
    shelltools.system("mv vcpkg-%s vcpkg" % VCPKG_COMMIT)
    shelltools.system("cp -pr res/vcpkg/* vcpkg/ports/")

    # git in the extracted flutter SDK is owned by a foreign uid; git refuses
    # to operate on it, which breaks flutter's SDK version detection
    shelltools.system("git config --global --add safe.directory '*'")

def build():
    cur = get.curDIR()
    sdk = os.path.join(get.workDIR(), "flutter")
    vc = "VCPKG_ROOT=%s/vcpkg" % cur
    shelltools.makedirs("/var/tmp/rustdesk-cargo")
    export = "export %s CARGO_HOME=/var/tmp/rustdesk-cargo CPATH=\"$(clang -v 2>&1 | grep 'Selected GCC installation: ' | cut -d' ' -f4-)/include\" PATH=%s/bin:/var/tmp/rustdesk-cargo/bin:$PATH" % (vc, sdk)

    # bootstrap vcpkg
    shelltools.system("%s && cd vcpkg && ./bootstrap-vcpkg.sh -disableMetrics" % export)
    # classic-mode install run from outside the source tree (a parent vcpkg.json manifest
    # would otherwise force manifest mode and reject package arguments)
    shelltools.system("%s && cd %s && $VCPKG_ROOT/vcpkg install --triplet x64-linux libvpx libyuv opus aom --disable-metrics --x-install-root=$VCPKG_ROOT/installed" % (export, get.workDIR()))

    # codegen bridge
    shelltools.system("%s && cargo install --path flutter_rust_bridge/frb_codegen --locked" % export)
    shelltools.system("%s && dart pub global activate ffigen --version 5.0.1" % export)
    shelltools.system("%s && cd flutter && flutter --disable-analytics && flutter --no-version-check clean && flutter --no-version-check pub get && cd .." % export)
    shelltools.system("%s && flutter_rust_bridge_codegen --rust-input ./src/flutter_ffi.rs --dart-output ./flutter/lib/generated_bridge.dart" % export)

    # fetch all crates, then fix the webm crate's missing <cstdint> include
    shelltools.system("%s && cargo fetch --locked" % export)
    patch = os.path.join(get.workDIR(), "mkvparser.patch")
    with open(patch, "w") as fh:
        fh.write(MKVPARSER_PATCH)
    shelltools.system("find /var/tmp/rustdesk-cargo/git -type f -name mkvparser.cc -execdir sh -c 'patch --no-backup-if-mismatch -Nup0 -i %s; rm -f mkvparser.cc.rej; true' ';'" % patch)

    # build rust lib + flutter bundle; neutralize the deb-packaging step of
    # build.py (dpkg-deb is not available on PisiLinux); pre-create the deb
    # file so build.py's final rename does not fail
    shelltools.system("sed -i 's/dpkg-deb/true/g' build.py")
    shelltools.system("touch flutter/rustdesk.deb")
    shelltools.system("%s && ./build.py --flutter" % export)

def install():
    # flutter bundle
    pisitools.insinto("/usr/lib/rustdesk", "flutter/build/linux/x64/release/bundle/*")
    pisitools.dosym("/usr/lib/rustdesk/rustdesk", "/usr/bin/rustdesk")

    # systemd service
    pisitools.insinto("/usr/lib/systemd/system", "res/rustdesk.service")

    # icons
    pisitools.insinto("/usr/share/icons/hicolor/32x32/apps", "res/32x32.png", "rustdesk.png")
    pisitools.insinto("/usr/share/icons/hicolor/128x128/apps", "res/128x128.png", "rustdesk.png")
    pisitools.insinto("/usr/share/icons/hicolor/256x256/apps", "res/128x128@2x.png", "rustdesk.png")

    # desktop entry
    shelltools.makedirs(os.path.join(get.installDIR(), "usr/share/applications"))
    with open(os.path.join(get.installDIR(), "usr/share/applications/rustdesk.desktop"), "w") as fh:
        fh.write("""[Desktop Entry]
Version=1.0
Name=RustDesk
GenericName=Remote Desktop
Comment=Remote Desktop
Exec=rustdesk %u
Icon=rustdesk
Terminal=false
Type=Application
MimeType=text/html;text/xml;application/xhtml+xml;application/vnd.mozilla.xul+xml;text/mml;x-scheme-handler/http;x-scheme-handler/https;
StartupNotify=true
Categories=Network;RemoteAccess;GTK;
Keywords=internet;
Actions=new-window;

[Desktop Action new-window]
Name=Open a New Window
Exec=rustdesk
""")

    # license
    pisitools.insinto("/usr/share/licenses/rustdesk", "LICENCE")
