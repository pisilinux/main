#!/usr/bin/python

import piksemel
import os
import re
import tempfile

ROOT_MOUNT_SOURCE_COMMAND = "findmnt -n -o SOURCE /"
PARTITION_SUFFIX_PATTERN = r"p?\d+$"
ROTATIONAL_FLAG_PATH_TEMPLATE = "/sys/block/{disk_name}/queue/rotational"


def _get_root_mount_source():
    with tempfile.NamedTemporaryFile(mode="r") as output_file:
        result = os.system("%s > %s" % (ROOT_MOUNT_SOURCE_COMMAND, output_file.name))
        if result != 0:
            raise OSError("Failed to get root mount source")

        output_file.seek(0)
        return output_file.read().strip()


def _strip_partition_suffix(device_path):
    return re.sub(PARTITION_SUFFIX_PATTERN, "", device_path)


def _is_rotational_disk(disk_name):
    rotational_flag_path = ROTATIONAL_FLAG_PATH_TEMPLATE.format(disk_name=disk_name)

    if not os.path.exists(rotational_flag_path):
        return False

    with open(rotational_flag_path, "r") as rotational_file:
        return int(rotational_file.read().strip()) == 1


def _is_root_on_hdd():
    """Return True if the root partition (/) is located on an HDD."""
    try:
        root_mount_source = _get_root_mount_source()
        if not root_mount_source:
            return False

        root_disk_path = _strip_partition_suffix(root_mount_source)
        root_disk_name = os.path.basename(root_disk_path)

        return _is_rotational_disk(root_disk_name)

    except (OSError, ValueError):
        return False

def _run_update_mime_database(path, use_fsync_opt):
    """Runs /usr/bin/update-mime-database for the given path.
       If use_fsync_opt is True, sets PKGSYSTEM_ENABLE_FSYNC=0."""
    os.system("%s/usr/bin/update-mime-database %s" % ("/usr/PKGSYSTEM_ENABLE_FSYNC=0 " if use_fsync_opt else "", path))

def updateMimeTypes(filepath):
    parse = piksemel.parse(filepath)
    paths = set()
    for icon in parse.tags("File"):
        path = icon.getTagData("Path")
        if "/share/mime/packages/" in path and path.endswith(".xml"):
            paths.add("/%s" % path.partition("packages/")[0])

    hdd = _is_root_on_hdd()
    for p in paths:
        _run_update_mime_database(p, hdd)

def setupPackage(metapath, filepath):
    updateMimeTypes(filepath)

def cleanupPackage(metapath, filepath):
    pass

def postCleanupPackage(metapath, filepath):
    updateMimeTypes(filepath)
