#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    # write layout's config
    os.system("rm -f usr/lib/graphviz/config{,6}")
    os.system("/usr/bin/dot -c")
