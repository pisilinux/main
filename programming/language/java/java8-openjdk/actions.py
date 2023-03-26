#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

import subprocess

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

jobs = "-j"+ subprocess.check_output("nproc 2>/dev/null", shell=True).rstrip("\n")

shelltools.export("ALT_PARALLEL_COMPILE_JOBS", jobs)
shelltools.export("HOTSPOT_BUILD_JOBS", jobs)
shelltools.export("LC_ALL", "C")

def setup():
    shelltools.export("CFLAGS", "%s -fPIC -O3" % get.CFLAGS())
    shelltools.export("CXXFLAGS", "%s -fPIC -O3" % get.CXXFLAGS())
    shelltools.export("CC", "gcc")
    shelltools.export("CXX", "g++")
    #shelltools.system('export DISTRIBUTION_PATCHES="patches/fontconfig-paths.diff \
                               #patches/openjdk7_nonreparenting-wm.diff"')
                               #patches/giflib_5.1.diff 
                             
    autotools.rawConfigure("\
                            --disable-tests \
                            --disable-Werror \
                            --with-parallel-jobs=%s \
                            --enable-nss \
                            --disable-system-kerberos \
                            --disable-system-pcsc \
                            --disable-system-sctp \
                            --enable-bootstrap \
                            --with-jdk-home=/usr/lib/jvm/java-8-openjdk \
                            --with-ecj-jar=/usr/share/java/ecj.jar \
                            --with-pkgversion='PisiLinux build 8.u352_3.25.0' \
                           " % jobs.replace("-j", ""))
    

def build():
    autotools.make()

def check():
    autotools.make("check -k")

def install():
    jvmdir="/usr/lib/jvm/java-8-openjdk"

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "HACKING", "README", "NEWS")

    #cd main output directory
    shelltools.cd("openjdk.build")

    #---- install openjdk8-doc
    pisitools.insinto("/usr/share/doc/openjdk8-doc", "docs/*")

    #install openjdk8-src
    pisitools.insinto(jvmdir, "images/j2sdk-image/src.zip") 

    #---- instal jdk8-openjdk
    for d in ["include","lib","bin"]:
        pisitools.insinto(jvmdir, "images/j2sdk-image/%s" % d) 

    for f in shelltools.ls("%s/usr/lib/jvm/java-8-openjdk/bin" % get.installDIR()):
        if not f in ["java", "java-rmi.cgi", "keytool", "orbd",
                     "pack200", "policytool", "rmid", "rmiregistry",
                     "servertool", "tnameserv", "unpack200", "jjs", "clhsdb", "hsdb"]:
            pisitools.dosym("/usr/lib/jvm/java-8-openjdk/bin/%s" % f, "/usr/bin/%s" % f)

    #install man pages
    for man in shelltools.ls("images/j2sdk-image/man/man1"):
        pisitools.insinto("/usr/share/man/man1", "images/j2sdk-image/man/man1/%s" % man, "%s" % man)
        
    for man in shelltools.ls("images/j2sdk-image/man/ja_JP.UTF-8/man1"):
        pisitools.insinto("/usr/share/man/ja/man1", "images/j2sdk-image/man/ja_JP.UTF-8/man1/%s" % man, "%s" % man )
    
    pisitools.insinto("/usr/share/applications", "../jconsole.desktop", "jconsole-jdk8.desktop")
    shelltools.system("chmod go+r %s%s/lib/sa-jdi.jar" %(get.installDIR(), jvmdir))

    #---- instal jre8-openjdk
    pisitools.insinto("%s/jre/bin" % jvmdir , "images/j2sdk-image/jre/bin/*")
    #pisitools.insinto("%s/jre/lib/amd64" % jvmdir , "j2sdk-image/jre/lib/amd64/xawt")
    
    for binfile in shelltools.ls("images/j2sdk-image/jre/bin"):
        pisitools.dosym("%s/jre/bin/%s" % (jvmdir, binfile), "/usr/bin/%s" % binfile)

    pisitools.insinto("/usr/share/applications", "../policytool.desktop", "policytool-jdk8.desktop")

    for size in [16, 24, 32, 48]:
        fullsize = "%dx%d" % ((size, ) * 2)
        pisitools.insinto("/usr/share/icons/hicolor/%s/apps/" % fullsize, "../openjdk/jdk/src/solaris/classes/sun/awt/X11/java-icon%d.png" % size, "java8.png")

    #---- install jre8-openjdk-headless
    pisitools.insinto("%s/jre/" % jvmdir , "images/j2sdk-image/jre/lib")
    pisitools.insinto("%s/jre/bin" % jvmdir, "images/j2sdk-image/jre/bin/*")

    #pisitools.rename("%s/jre/lib/fontconfig.Ubuntu.properties.src" % jvmdir , "fontconfig.properties")
    #pisitools.rename("%s/jre/lib/fontconfig.Ubuntu.bfc" % jvmdir , "fontconfig.bfc")
    #pisitools.remove("%s/jre/lib/fontconfig.*.bfc" % jvmdir)
    #pisitools.remove("%s/jre/lib/fontconfig.*.properties.src" % jvmdir)

    pisitools.domove("%s/jre/lib/*.properties*" % jvmdir,"/etc/java-8-openjdk/")

    for propfile in shelltools.ls("%s/etc/java-8-openjdk/" % get.installDIR()):
        pisitools.dosym("/etc/java-8-openjdk/%s" % propfile, "%s/jre/lib/%s" % (jvmdir, propfile))

    pisitools.domove("%s/jre/lib/images/cursors/cursors.properties" % jvmdir,"/etc/java-8-openjdk/cursors/")
    pisitools.dosym("/etc/java-8-openjdk/cursors/cursors.properties", "%s/jre/lib/images/cursors/cursors.properties" % jvmdir)

    pisitools.rename("%s/jre/lib/management/jmxremote.password.template" % jvmdir , "jmxremote.password")
    pisitools.rename("%s/jre/lib/management/snmp.acl.template" % jvmdir , "snmp.acl")

    for f in ["management.properties", "jmxremote.access", "jmxremote.password", "snmp.acl"]:
        pisitools.domove("%s/jre/lib/management/%s" % (jvmdir, f),"/etc/java-8-openjdk/management/")
        pisitools.dosym("/etc/java-8-openjdk/management/%s" % f, "%s/jre/lib/management/%s" % (jvmdir, f))

    for f in ["java.policy","java.security","nss.cfg"]:
        pisitools.domove("%s/jre/lib/security/%s" % (jvmdir, f),"/etc/java-8-openjdk/security/")
        pisitools.dosym("/etc/java-8-openjdk/security/%s" % f, "%s/jre/lib/security/%s" % (jvmdir, f))

    #confs=os.listdir("%s/etc/java-8-openjdk/" % get.installDIR())
    #for i in confs:
        #shelltools.system("chmod 0644 %s/etc/java-8-openjdk/%s" % (get.installDIR, i))
        
    #pisitools.domove("%s/jre/lib/fontconfig.bfc" % jvmdir,"/etc/java-8-openjdk/")
    pisitools.domove("%s/jre/lib/amd64/jvm.cfg" % jvmdir,"/etc/java-8-openjdk/")
    pisitools.dosym("/etc/java-8-openjdk/jvm.cfg" , "%s/jre/lib/amd64/jvm.cfg" % jvmdir)

    for license in ["LICENSE", "THIRD_PARTY_README", "release", "ASSEMBLY_EXCEPTION"]:
        pisitools.insinto("/usr/share/doc/jre8-openjdk-headless", "images/j2re-image/%s" % license)
      
    pisitools.remove("%s/jre/lib/security/cacerts" % jvmdir)
    
    #seems we need to add this symlink into ca-certificates-java package ?
    pisitools.dosym("/etc/ssl/certs/java/cacerts", "%s/jre/lib/security/cacerts" % jvmdir)
    
    pisitools.dosed("%s/usr/share/applications/policytool-jdk8.desktop" % get.installDIR(), "_JREBINDIR_", "/usr/lib/jvm/java-8-openjdk/jre/bin")
    pisitools.dosed("%s/usr/share/applications/jconsole-jdk8.desktop" % get.installDIR(), "_SDKBINDIR_", "/usr/lib/jvm/java-8-openjdk/bin")
    
    #icons
    pisitools.dosed("%s/usr/share/applications/policytool-jdk8.desktop" % get.installDIR(), "Icon=java-1.8.0-openjdk", "Icon=java8-1.8.0-openjdk")
    pisitools.dosed("%s/usr/share/applications/jconsole-jdk8.desktop" % get.installDIR(), "Icon=java-1.8.0-openjdk", "Icon=java8-1.8.0-openjdk")
