#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt
#
# TODO: glibc has to be rebuilt with libtirpc, so that we can enable libtirpc support in samba

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

shelltools.export("JOBS", get.makeJOBS().replace("-j", ""))

def setup():
    shelltools.system("sed -r 's/nss_(setpw|endpw|setgr|endgr)ent/my_&/' \
                       -i nsswitch/nsstest.c")

    shelltools.system("python3 -m venv pyvenv && ./pyvenv/bin/pip3 install cryptography pyasn1 iso8601")
    shelltools.system('echo "^samba4.rpc.echo.*on.*ncacn_np.*with.*object.*nt4_dc" >> selftest/knownfail')

    shelltools.export("PYTHON", "%s/pyvenv/bin/python3" % get.curDIR())
    shelltools.export("CFLAGS", "-I/usr/include/tirpc")
    shelltools.export("LDFLAGS", "-ltirpc")
    shelltools.system("export PATH=$PWD/pyvenv/bin:$PATH")

    autotools.configure("--prefix=/usr                       \
                         --sysconfdir=/etc                   \
                         --localstatedir=/var                \
                         --with-piddir=/run/samba            \
                         --with-pammodulesdir=/lib/security  \
                         --without-ad-dc                     \
                         --enable-fhs                        \
                         --without-systemd                   \
                         --bundled-libraries=!tdb,!talloc,!pytalloc-util \
                         --enable-selftest")

def build():
    # For some reason, autotools.make() does not work.
    shelltools.system("make")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.system("install -d %s/lib" % get.installDIR())
    shelltools.move("%s/usr/lib/libnss_wins.so*" % get.installDIR(), "%s/lib" % get.installDIR())
    shelltools.move("%s/usr/lib/libnss_winbind.so*" % get.installDIR(), "%s/lib" % get.installDIR())
    pisitools.dosym("/lib/libnss_winbind.so.2", "/usr/lib/libnss_winbind.so")
    pisitools.dosym("/lib/libnss_wins.so.2", "/usr/lib/libnss_wins.so")

    shelltools.system("install -v -m644 examples/smb.conf.default %s/etc/samba/smb.conf.default" % get.installDIR())

    pisitools.dodir("/etc/openldap/schema")
    shelltools.system("install -v -m644 examples/LDAP/README \
                       %s/etc/openldap/schema/README.LDAP" % get.installDIR())
    shelltools.system("install -v -m644 examples/LDAP/samba* \
                       %s/etc/openldap/schema" % get.installDIR())
    shelltools.system("install -v -m755 examples/LDAP/{get*,ol*} \
                       %s/etc/openldap/schema" % get.installDIR())

    shelltools.system("install -d %s/usr/lib/cups/backend" % get.installDIR())
    pisitools.dosym("/usr/bin/smbspool", "/usr/lib/cups/backend/smb")

    pisitools.remove("/usr/lib/python3.11/site-packages/_tdb_text.py")
    pisitools.remove("/usr/lib/python3.11/site-packages/tdb.cpython-311-x86_64-linux-gnu.so")
    pisitools.remove("/usr/lib/python3.11/site-packages/tevent.py")
    pisitools.remove("/usr/lib/python3.11/site-packages/_tevent.cpython-311-x86_64-linux-gnu.so")
