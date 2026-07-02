#!/usr/bin/python3

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
import os

def setup():
	shelltools.export("CARGO_HOME", os.path.join(get.workDIR(), ".cargo"))

def build():
    shelltools.system("cargo build --release --bin OpenCADStudio")

def install():
    if not os.path.exists(get.installDIR() + "/usr/bin"):
        os.makedirs(get.installDIR() + "/usr/bin")
    if not os.path.exists(get.installDIR() + "/usr/share/doc/opencadstudio"):
        os.makedirs(get.installDIR() + "/usr/share/doc/opencadstudio")
    shelltools.system("cp target/release/OpenCADStudio " + get.installDIR() + "/usr/bin/opencadstudio")
    shelltools.system("cp README.md " + get.installDIR() + "/usr/share/doc/opencadstudio/README.md")
    shelltools.system("cp LICENSE " + get.installDIR() + "/usr/share/doc/opencadstudio/LICENSE")
