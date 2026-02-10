#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pisi.actionsapi import shelltools, get, pisitools

def setup():
    shelltools.system("git clone --recursive https://github.com/JezerM/nody-greeter.git temp_dir")
    shelltools.system("cp -rf temp_dir/* .")
    shelltools.system("cp -rf temp_dir/.* . 2>/dev/null || true")
    shelltools.system("rm -rf temp_dir")
    
    if shelltools.can_access_file("../../package.patch"):
        shelltools.system("patch -p1 < ../../package.patch")
    
    shelltools.system("npm install node-gtk@latest nan@latest --legacy-peer-deps")
    shelltools.system("npm install --legacy-peer-deps")

def build():
    shelltools.system("sed -i 's/assert { type: \"json\" }/with { type: \"json\" }/g' build.js")
    shelltools.system("sed -i 's/assert { type: \"json\" }/with { type: \"json\" }/g' compile.js")
    shelltools.system("sed -i 's/npm ci --omit=dev --ignore-scripts/npm install --omit=dev --ignore-scripts --legacy-peer-deps/g' build.js")
    shelltools.system("sed -i 's/.*removeSync.*/\/\/ removeSync engellendi/g' build.js")
    shelltools.system("sed -i 's/.*rmSync.*/\/\/ rmSync engellendi/g' build.js")
    shelltools.system("rm -rf build/unpacked")
    shelltools.system("npm run rebuild")
    
    if not shelltools.can_access_directory("themes/themes"):
        shelltools.system("mkdir -p themes/themes && cp -r themes/* themes/themes/ 2>/dev/null || true")

    shelltools.system("npm run build")

def install():
    shelltools.system("node make --DEST_DIR=" + get.installDIR() + " install")
    shelltools.system("rm -rf " + get.installDIR()+"/usr/bin/nody-greeter")
    pisitools.dosym("/opt/nody-greeter/nody-greeter", "/usr/bin/nody-greeter")
    if shelltools.can_access_file("nody-greeter.desktop"):
        shelltools.system("cp nody-greeter.desktop " + get.installDIR() + "/usr/share/xgreeters/")

    pisitools.dodir("/usr/share/xgreeters")

    pisitools.dodoc("README.md", "LICENSE")