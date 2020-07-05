#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    if os.path.exists("/etc/default/grub"):
        fileContent = open("/etc/default/grub").readlines()
        new = []
        for line in fileContent:
            line = line.strip()
            if line.startswith("#GRUB_CMDLINE_LINUX="): line = line[1:]
            if line.startswith("GRUB_CMDLINE_LINUX="):
                if not "rd.driver.blacklist=nouveau" in line:
                    if not line[-2] == '"': line = "%s \"" % line[:-1]
                    line = "%srd.driver.blacklist=nouveau\"" % line[:-1]
            new.append(line)
        with open("/etc/default/grub", "w") as f: f.write("\n".join(new))
        os.system("grub2-mkconfig -o /boot/grub2/grub.cfg")

def postRemove():
    if os.path.exists("/etc/default/grub"):
        fileContent = open("/etc/default/grub").readlines()
        new = []
        for line in fileContent:
            line = line.strip()
            if line.startswith("GRUB_CMDLINE_LINUX="):
                if not "rd.driver.blacklist=nouveau" in line: return
                line = "%s\"" % line[:-1-len("rd.driver.blacklist=nouveau")]
                if line[-2] == " ": line = "%s\"" % line[:-2]
            new.append(line)
        with open("/etc/default/grub", "w") as f: f.write("\n".join(new))
        os.system("grub2-mkconfig -o /boot/grub2/grub.cfg")
