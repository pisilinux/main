#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import piksemel
import subprocess

def generate_initrd(kver):
    subprocess.call(["/usr/bin/mkinitcpio","-k","%s"% kver ,"-g","/boot/initramfs-%s-fallback.img"% kver,"-S","autodetect"])
    subprocess.call(["/usr/bin/mkinitcpio","-k","%s"% kver ,"-c","/etc/mkinitcpio.conf","-g","/boot/initramfs-%s.img"% kver])

def get_kver():
    with open("/etc/kernel/kernel") as f:
        return f.readline().strip()

def run_dkms(name, version, kver, arch):
    os.system("dkms build -m %s -v %s -k %s -a %s" % (name, version, kver, arch))
    os.system("dkms install -m %s -v %s -k %s -a %s" % (name, version, kver, arch))

def buildModules(metapath, filepath):
    if piksemel.parse(metapath).getTag("Package").getTagData("Name") == "kernel-module-headers":
        kver = get_kver()
        arch = piksemel.parse(metapath).getTag("Package").getTagData("Architecture").replace("_", "-")
        # rebuild if /usr/src/*/dkms.conf exists
        for d in os.walk("/usr/src").next()[1]:
            if os.path.isfile("/usr/src/%s/dkms.conf" % d):
                name, version = d.split("-")
                run_dkms(name, version, kver, arch)
        generate_initrd(kver)
        return

    parse = piksemel.parse(filepath)
    for fp in parse.tags("File"):
        path = fp.getTagData("Path")
        # build if package has /usr/src/*/dkms.conf 
        if path.endswith("/dkms.conf") and path.startswith("usr/src/"):
            name = path.split("/")[-2].split("-")[0]
            version = path.split("/")[-2].split("-")[1]
            kver = get_kver()
            arch = piksemel.parse(metapath).getTag("Package").getTagData("Architecture").replace("_", "-")
            run_dkms(name, version, kver, arch)
            generate_initrd(kver)
            return

def setupPackage(metapath, filepath):
    buildModules(metapath, filepath)

def cleanupPackage(metapath, filepath):
    pass

def postCleanupPackage(metapath, filepath):
    pass
