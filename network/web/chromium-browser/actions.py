#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "chromium-%s" % get.srcVERSION()

shelltools.export("HOME", get.workDIR())

ARCH = "x64"

def setup():
    shelltools.export("LC_ALL", "C")
    shelltools.system("export -n CFLAGS CXXFLAGS")
    shelltools.system("sed -i 's|icu)|icu-i18n)|g' build/linux/system.gyp")
    shelltools.system("CFLAGS+=' -fno-delete-null-pointer-checks'")
    shelltools.touch(get.workDIR() + "/chromium-*/chrome/test/data/webui/i18n_process_css_test.html")
    
    
    options = "\
                        -Dwerror= \
                        -Dclang=0 \
                        -Dpython_ver=2.7 \
                        -Dlinux_link_gsettings=1 \
                        -Dlinux_link_libpci=1 \
                        -Dlinux_link_libspeechd=1 \
                        -Dlinux_link_pulseaudio=1 \
                        -Dlinux_strip_binary=1 \
                        -Dlinux_use_bundled_binutils=0 \
                        -Dlinux_use_bundled_gold=0 \
                        -Dlinux_use_gold_flags=0 \
                        -Dicu_use_data_file_flag=1 \
                        -Dlogging_like_official_build=1 \
                        -Dtracing_like_official_build=1 \
                        -Dffmpeg_branding=Chrome \
                        -Dproprietary_codecs=1 \
                        -Duse_gnome_keyring=0 \
                        -Duse_system_bzip2=1 \
                        -Duse_system_flac=1 \
                        -Duse_system_ffmpeg=0 \
                        -Duse_system_harfbuzz=1 \
                        -Duse_system_icu=0 \
                        -Duse_system_libevent=1 \
                        -Duse_system_libjpeg=1 \
                        -Duse_system_libpng=1 \
                        -Duse_system_libvpx=1 \
                        -Duse_system_libxml=0 \
                        -Duse_system_snappy=1 \
                        -Duse_system_xdg_utils=1 \
                        -Duse_system_yasm=1 \
                        -Duse_system_zlib=0 \
                        -Duse_mojo=0 \
                        -Duse_gconf=0 \
                        -Duse_sysroot=0 \
                        -Denable_widevine=1 \
                        -Ddisable_glibc=1 \
                        -Ddisable_nacl=1 \
                        -Ddisable_pnacl=1 \
                        -Ddisable_fatal_linker_warnings=1 \
                        -Drelease_extra_cflags=-fno-ipa-cp \
                        -Denable_hangout_services_extension=1 \
                        -Dusb_ids_path=/usr/share/misc/usb.ids \
                        -Dlibspeechd_h_prefix=speech-dispatcher/ \
                        -Dfieldtrial_testing_like_official_build=1 \
                        -Dlinux_sandbox_path=/usr/lib/chromium-browser/chromium-sandbox \
                        -Dlinux_sandbox_chrome_path=/usr/lib/chromium-browser/chromium-browser \
                        -Dgoogle_api_key=AIzaSyDwr302FpOSkGRpLlUpPThNTDPbXcIn_FM \
                        -Dgoogle_default_client_id=413772536636.apps.googleusercontent.com \
                        -Dgoogle_default_client_secret=0ZChLK6AxeA3Isu96MkwqDR4 "
    
    shelltools.system("build/linux/unbundle/replace_gyp_files.py  %s" % options)
    shelltools.system("build/gyp_chromium build/all.gyp --depth=. %s" % options)
    shelltools.export("GYP_GENERATORS","ninja")

def build():
    
    #Sandbox for error must remain separate
    
    shelltools.system("ninja -C out/Release chrome")
    shelltools.system("ninja -C out/Release chrome_sandbox")
    shelltools.system("ninja -C out/Release chromedriver")

def install():
    shelltools.cd("out/Release")

    #should be checked should for the missing folder "out/Release"
    pisitools.insinto("/usr/lib/chromium-browser", "*.pak")
    pisitools.insinto("/usr/lib/chromium-browser", "*.json")
    pisitools.insinto("/usr/lib/chromium-browser", "chrome")
    pisitools.insinto("/usr/lib/chromium-browser", "locales")
    pisitools.insinto("/usr/lib/chromium-browser", "resources")
    pisitools.insinto("/usr/lib/chromium-browser", "icudtl.dat")
    pisitools.insinto("/usr/lib/chromium-browser", "mksnapshot")
    pisitools.insinto("/usr/lib/chromium-browser", "chromedriver")
    pisitools.insinto("/usr/lib/chromium-browser", "natives_blob.bin")
    pisitools.insinto("/usr/lib/chromium-browser", "snapshot_blob.bin")
    pisitools.insinto("/usr/lib/chromium-browser", "libwidevinecdm.so")
    pisitools.insinto("/usr/lib/chromium-browser", "libwidevinecdmadapter.so")
    pisitools.insinto("/usr/lib/chromium-browser", "character_data_generator")
    pisitools.insinto("/usr/lib/chromium-browser", "chrome_sandbox", "chrome-sandbox")
    
    
    pisitools.dosym("/usr/lib/chromium-browser/chrome", "/usr/bin/chromium-browser")
    
    shelltools.system("chmod -v 4755 %s/usr/lib/chromium-browser/chrome-sandbox" %get.installDIR())
    

    
    pisitools.newman("chrome.1", "chromium-browser.1")
    
    shelltools.cd("../..")
    for size in ["22", "24", "48", "64", "128", "256"]:
        pisitools.insinto("/usr/share/icons/hicolor/%sx%s/apps" %(size, size), "chrome/app/theme/chromium/product_logo_%s.png" % size, "chromium-browser.png")
   		
    pisitools.dosym("/usr/share/icons/hicolor/256x256/apps/chromium-browser.png", "/usr/share/pixmaps/chromium-browser.png")
    
    pisitools.dodoc("LICENSE")

