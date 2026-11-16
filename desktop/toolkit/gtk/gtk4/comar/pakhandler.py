#!/usr/bin/python
# -*- coding: utf-8 -*-

import piksemel
import os
import fnmatch

def update_icon_cache(filepath):
    parse = piksemel.parse(filepath)

    for icon in parse.tags("File"):
        path = icon.getTagData("Path")

        if path.startswith("usr/share/icons/"):
            full_path = os.path.join("/", path)

            if os.path.isdir(full_path) and os.path.exists(os.path.join(full_path, "index.theme")):
                os.system("/usr/bin/gtk4-update-icon-cache -q -t -f %s" % full_path)
            elif not os.path.exists(full_path):
                cache_file = os.path.join(full_path, "icon-theme.cache")
                if os.path.exists(cache_file):
                    os.remove(cache_file)


def setupPackage(metapath, filepath):
    update_icon_cache(filepath)

def cleanupPackage(metapath, filepath):
    # Kaldirma oncesi ozel bir islem gerekmiyor
    pass

def postCleanupPackage(metapath, filepath):
    update_icon_cache(filepath)
