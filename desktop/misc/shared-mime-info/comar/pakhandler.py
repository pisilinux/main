#!/usr/bin/python

import piksemel
import os
import re
import subprocess

def is_root_on_hdd():
    """Returns True if the root partition (/) is located on an HDD."""
    try:
        # 1. Get the source device for the mount point /
        result = subprocess.run(
            ["findmnt", "-n", "-o", "SOURCE", "/"],
            capture_output=True, text=True, check=True
        )
        source = result.stdout.strip()
        if not source:
            return False

        # 2. Strip the partition number (for /dev/sda1 -> /dev/sda, for /dev/nvme0n1p1 -> /dev/nvme0n1)
        disk = re.sub(r'p?\d+$', '', source)   # remove trailing digits and optional 'p'
        disk_name = os.path.basename(disk)

        # 3. Check the contents of the rotational file
        rotational_path = f"/sys/block/{disk_name}/queue/rotational"
        if not os.path.exists(rotational_path):
            return False

        with open(rotational_path, 'r') as f:
            rotational = int(f.read().strip())

        return rotational == 1

    except Exception:
        # On any error, assume it's not an HDD (variable won't be set)
        return False

def run_update_mime_database(path, use_fsync_opt):
    """Runs /usr/bin/update-mime-database for the given path.
       If use_fsync_opt is True, sets PKGSYSTEM_ENABLE_FSYNC=0."""
    cmd = ["/usr/bin/update-mime-database", path]
    env = os.environ.copy()
    if use_fsync_opt:
        env["PKGSYSTEM_ENABLE_FSYNC"] = "0"
    subprocess.run(cmd, env=env, check=False)

def updateMimeTypes(filepath):
    parse = piksemel.parse(filepath)
    paths = set()
    for icon in parse.tags("File"):
        path = icon.getTagData("Path")
        if "/share/mime/packages/" in path and path.endswith(".xml"):
            paths.add("/%s" % path.partition("packages/")[0])

    hdd = is_root_on_hdd()
    for p in paths:
        run_update_mime_database(p, hdd)

def setupPackage(metapath, filepath):
    updateMimeTypes(filepath)

def cleanupPackage(metapath, filepath):
    pass

def postCleanupPackage(metapath, filepath):
    updateMimeTypes(filepath)
