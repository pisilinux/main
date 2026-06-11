#!/usr/bin/python

import os

# Update global mime databases, mime database format may change (0.70)
def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    cmd = (
        "disk=$(findmnt -n -o SOURCE / | sed 's/[0-9]*$//'); "
        "env $( [ -f \"/sys/block/${disk##*/}/queue/rotational\" ] && "
        "[ \"$(cat \"/sys/block/${disk##*/}/queue/rotational\")\" = \"1\" ] && "
        "echo PKGSYSTEM_ENABLE_FSYNC=0 ) "
        "/usr/bin/update-mime-database /usr/share/mime"
    )
    os.system(cmd)
