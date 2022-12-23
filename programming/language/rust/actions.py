#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "rustc-%s-src" %get.srcVERSION()

### ÖNEMLİ NOT: ###
#LLVM yükseltmelerinden sonra, ilk aşama olarak rust, manuel indirdiğimiz binary rust paketi ile derlenecek. Bu birinci aşama olacak.
#İkinci aşamada ise derlediğimiz bu rust ile rust tekrar derlenecek.
#İkinci aşamada aşağıdaki satırlar yoruma çevrilecek.

### IMPORTANT NOTE ###
#After upgrading LLVM, rust will be built via manually downloaded binary rust distro. This will be phase 1.
#At phase 2, rust will be built again with this newly built rust.
#Before phase 2, the lines below will be commented out.

RustBinDir = "rust-%s-x86_64-unknown-linux-gnu" %get.srcVERSION()
RustcDir = "%s/rustbin" %get.workDIR()

#################################################################

def build():
    #İkinci aşamada bu satırlar da yoruma çevrilecek.
    #At phase 2, these lines also will be commented out.
    shelltools.cd(RustBinDir)
    shelltools.system("./install.sh --prefix=%s --without=rust-docs" %RustcDir)
    shelltools.cd("..")
    pisitools.dosed("config.toml", "/usr/bin/cargo", RustcDir+"/bin/cargo")
    pisitools.dosed("config.toml", "/usr/bin/rustc", RustcDir+"/bin/rustc")
    ####################################################
    
    shelltools.export("LC_ALL", "en_US.UTF-8")
    shelltools.export("RUST_BACKTRACE", "1")
    shelltools.system("python ./x.py build")
    

def install():
    shelltools.system("DESTDIR=%s python ./x.py install" % get.installDIR())
    
    #pisitools.insinto("/", "build/x86_64-unknown-linux-gnu/stage0/etc")
    #pisitools.insinto("/usr", "build/x86_64-unknown-linux-gnu/stage0/bin")
    #pisitools.insinto("/usr", "build/x86_64-unknown-linux-gnu/stage0/lib")
    #pisitools.insinto("/usr", "build/x86_64-unknown-linux-gnu/stage0/share")
    #pisitools.insinto("/usr", "build/x86_64-unknown-linux-gnu/stage0/manifest.in")
        
    #pisitools.dodoc("LICENSE","AUTHORS","README*")
