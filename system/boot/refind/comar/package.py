#!/usr/bin/python

import os


def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("refind-install")
    os.system("rm -rf /boot/efi/EFI/boot")
    
    
def preRemove():
    pass
