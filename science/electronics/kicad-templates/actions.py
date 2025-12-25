from pisi.actionsapi import cmaketools, pisitools, shelltools, get

def install():
    pisitools.insinto("/usr/share/kicad/templates", "*")
