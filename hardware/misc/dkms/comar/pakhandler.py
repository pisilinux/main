#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import piksemel
import subprocess

class BuildModuleError(Exception):
    pass

def generate_initrd(kver):
    subprocess.call(["/usr/bin/mkinitcpio","-k","%s"% kver ,"-g","/boot/initramfs-%s-fallback.img"% kver,"-S","autodetect"])
    subprocess.call(["/usr/bin/mkinitcpio","-k","%s"% kver ,"-c","/etc/mkinitcpio.conf","-g","/boot/initramfs-%s.img"% kver])

def get_kver():
    with open("/etc/kernel/kernel") as f:
        return f.readline().strip()

def run_dkms(action, name, version, kver, arch):
    actions = {"build": ["build", "install"],
               "remove": ["uninstall", "remove"]}
    for action in actions[action]:
        os.system("PATH='/usr/sbin:/usr/bin:/sbin:/bin' dkms %s -m %s -v %s -k %s -a %s" % (action, name, version, kver, arch))

    if action == "install" and os.path.exists("/var/lib/dkms/%s/%s/build/make.log" % (name, version)):
        raise BuildModuleError("check /var/lib/dkms/%s/%s/build/make.log" % (name, version))

def check_dkms(metapath, filepath, action):
    if piksemel.parse(metapath).getTag("Package").getTagData("Name") == "kernel-module-headers":
        kver = get_kver()
        arch = piksemel.parse(metapath).getTag("Package").getTagData("Architecture").replace("_", "-")
        # rebuild if /usr/src/*/dkms.conf exists
        for d in os.walk("/usr/src").next()[1]:
            if os.path.isfile("/usr/src/%s/dkms.conf" % d):
                name = d.split("-")[0]
                version = d.split("-")[-1]
                run_dkms(action, name, version, kver, arch)
        generate_initrd(kver)
        return

    parse = piksemel.parse(filepath)
    for fp in parse.tags("File"):
        path = fp.getTagData("Path")
        # build if package has /usr/src/*/dkms.conf 
        if path.endswith("/dkms.conf") and path.startswith("usr/src/"):
            name = path.split("/")[-2].split("-")[0]
            version = path.split("/")[-2].split("-")[-1]
            kver = get_kver()
            arch = piksemel.parse(metapath).getTag("Package").getTagData("Architecture").replace("_", "-")
            run_dkms(action, name, version, kver, arch)
            generate_initrd(kver)
            return

def setupPackage(metapath, filepath):
    check_dkms(metapath, filepath, action="build")

def cleanupPackage(metapath, filepath):
    check_dkms(metapath, filepath, action="remove")

def postCleanupPackage(metapath, filepath):
    pass
