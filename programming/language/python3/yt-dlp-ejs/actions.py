from pisi.actionsapi import python3modules

def build():
    python3modules.compile(pyVer="3")

def install():
    python3modules.install(pyVer="3")
