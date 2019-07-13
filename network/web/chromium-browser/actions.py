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
    shelltools.system("mkdir -p third_party/node/linux/node-linux-x64/bin")
    shelltools.system("ln -s /usr/bin/node third_party/node/linux/node-linux-x64/bin/")

    for LIB in ["freetype", "flac", "harfbuzz-ng", "libxml" ,"libxslt", "re2", "yasm"]:
        shelltools.system('find -type f -path "*third_party/$LIB/*" \! -path "*third_party/$LIB/chromium/*" \! -path "*third_party/$LIB/google/*" \! -regex ".*\.\(gn\|gni\|isolate\|py\)" -delete')

    shelltools.system("build/linux/unbundle/replace_gn_files.py --system-libraries flac freetype harfbuzz-ng libxml libxslt re2 yasm")
    
    shelltools.system("sed -i -e 's/\<xmlMalloc\>/malloc/' -e 's/\<xmlFree\>/free/' \
                       third_party/blink/renderer/core/xml/*.cc \
                       third_party/blink/renderer/core/xml/parser/xml_document_parser.cc \
					   third_party/libxml/chromium/libxml_utils.cc")

    opt = 'use_sysroot=false \
           enable_nacl=true \
           enable_nacl_nonsfi=true \
           use_custom_libcxx=false \
           clang_use_chrome_plugins=false \
           is_official_build=true \
           fieldtrial_testing_like_official_build=true \
           clang_use_chrome_plugins=false \
           fatal_linker_warnings=false \
           treat_warnings_as_errors=false \
           use_gnome_keyring=false\
           use_gold=false \
           enable_hangout_services_extension=true \
           enable_widevine=true \
           linux_use_bundled_binutils=false \
           is_debug=false \
           ffmpeg_branding="Chrome" \
           google_default_client_secret="0ZChLK6AxeA3Isu96MkwqDR4" \
           google_api_key="AIzaSyDwr302FpOSkGRpLlUpPThNTDPbXcIn_FM" \
           google_default_client_id="413772536636.apps.googleusercontent.com" \
           remove_webcore_debug_symbols=true \
           proprietary_codecs=true \
           link_pulseaudio=true \
           enable_swiftshader=false \
           use_vaapi=true \
           closure_compile=false'
           
        
    #clangpath = "%s/chromium-%s/third_party/llvm-build/Release+Asserts/bin/" %(get.workDIR(), get.srcVERSION())

    shelltools.export("CC", "clang" )
    shelltools.export("CXX", "clang++" )
    shelltools.export("AR", "llvm-ar" )
    
    shelltools.export("CFLAGS", "-Wno-builtin-macro-redefined")
    shelltools.export("CXXFLAGS", "-Wno-builtin-macro-redefined")
    shelltools.export("CPPFLAGS", "-D__DATE__=  -D__TIME__=  -D__TIMESTAMP__=")
    
    shelltools.system("build/download_nacl_toolchains.py --packages nacl_x86_newlib,pnacl_newlib,pnacl_translator sync --extract")
    shelltools.system("tools/clang/scripts/update.py")
    shelltools.system("tools/gn/bootstrap/bootstrap.py --gn-gen-args '%s'"% opt)
    shelltools.system("out/Release/gn gen out/Release --args='%s'"% opt)


def build():
    #Sandbox for error must remain separate
    shelltools.system("ninja -C out/Release chrome")
    shelltools.system("ninja -C out/Release chrome_sandbox")
    shelltools.system("ninja -C out/Release chromedriver")
    #shelltools.system("ninja -C out/Release widevinecdmadapter")

def install():
    shelltools.cd("out/Release")

    #should be checked should for the missing folder "out/Release"
    for vla in ["*.pak", "*.json", "chrome", "locales", "resources", "icudtl.dat", "mksnapshot", "chromedriver", "natives_blob.bin", "snapshot_blob.bin", "character_data_generator", \
			    "libEGL.so", "libGLESv2.so", "libVk*.so", "swiftshader", "v8_context_snapshot.bin", "MEIPreload", "nacl_helper", "nacl_helper_bootstrap", "nacl_helper_nonsfi", "nacl_irt_x86_64.nexe"]:
        pisitools.insinto("/usr/lib/chromium-browser", "%s" % vla)

    pisitools.insinto("/usr/lib/chromium-browser", "chrome_sandbox", "chrome-sandbox")
    pisitools.dosym("/usr/lib/chromium-browser/chrome", "/usr/bin/chromium-browser")
 
    shelltools.system("chmod -v 4755 %s/usr/lib/chromium-browser/chrome-sandbox" %get.installDIR())

    pisitools.newman("chrome.1", "chromium-browser.1")

    shelltools.cd("../..")
    for size in ["22", "24", "48", "64", "128", "256"]:
        pisitools.insinto("/usr/share/icons/hicolor/%sx%s/apps" %(size, size), "chrome/app/theme/chromium/product_logo_%s.png" % size, "chromium-browser.png")

    pisitools.dosym("/usr/share/icons/hicolor/256x256/apps/chromium-browser.png", "/usr/share/pixmaps/chromium-browser.png")

    pisitools.dodoc("LICENSE")
