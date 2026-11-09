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
    #shelltools.export("JAVA_CMD", "/usr/bin/java_8")
    shelltools.system("mkdir -p third_party/node/linux/node-linux-x64/bin")
    shelltools.system("mkdir -p third_party/rust-toolchain/bin")
    shelltools.system("mkdir -p third_party/jdk/current/bin")
    shelltools.system("mkdir -p tthird_party/rust-toolchain/bin")

    # shelltools.system('echo "1.95.0" > third_party/rust-toolchain/VERSION')

    shelltools.system("ln -s /usr/bin/node third_party/node/linux/node-linux-x64/bin/")
    shelltools.system("ln -s /usr/bin/java third_party/jdk/current/bin/")
    shelltools.system("ln -s usr/bin/rustc third_party/rust-toolchain/bin/")

    shelltools.system("rm -f third_party/gperf/cipd/bin/gperf")
    shelltools.system("ln -s /usr/bin/gperf third_party/gperf/cipd/bin/")
    
    shelltools.system("sed -i 's/OFFICIAL_BUILD/GOOGLE_CHROME_BUILD/' tools/generate_shim_headers/generate_shim_headers.py")

    #for LIB in ["ffmpeg", "freetype", "flac", "fontconfig", "harfbuzz-ng", "libdrm", "libjpeg_turbo", "libpng", "libwebp", "libxml", "libxslt", "opus", "snappy", "zlib"]:
        #shelltools.system('find "third_party/%s" -type f  \! -path "third_party/%s/chromium/*" \! -path "*third_party/%s/google/*" \! -path "third_party/harfbuzz-ng/utils/hb_scoped.h" \! -regex ".*\.\(gn\|gni\|isolate\)" -delete' %(LIB, LIB, LIB))
	
	
    #shelltools.system("build/linux/unbundle/replace_gn_files.py --system-libraries ffmpeg freetype flac fontconfig harfbuzz-ng libdrm libjpeg libpng libwebp libxml libxslt opus snappy zlib")
    
    shelltools.system("sed -i -e 's/\<xmlMalloc\>/malloc/' -e 's/\<xmlFree\>/free/' \
                       third_party/blink/renderer/core/xml/*.cc \
                       third_party/blink/renderer/core/xml/parser/xml_document_parser.cc \
                       third_party/libxml/chromium/libxml_utils.cc")

    opt = 'custom_toolchain="//build/toolchain/linux/unbundle:default" \
           host_toolchain="//build/toolchain/linux/unbundle:default" \
           use_sysroot=false \
           rtc_use_pipewire=true \
           use_custom_libcxx=true \
           clang_use_chrome_plugins=true \
           is_official_build=true \
           disable_fieldtrial_testing_config=true \
           blink_enable_generated_code_formatting=false \
           fatal_linker_warnings=false \
           treat_warnings_as_errors=false \
           enable_hangout_services_extension=true \
           enable_widevine=true \
           is_debug=false \
           ffmpeg_branding="Chrome" \
           google_api_key="AIzaSyDwr302FpOSkGRpLlUpPThNTDPbXcIn_FM" \
           proprietary_codecs=true \
           link_pulseaudio=true \
           enable_swiftshader=false \
           use_vaapi=true \
           closure_compile=false \
           symbol_level=0 \
           use_lld=true \
           is_cfi=false \
           use_thin_lto=false \
           chrome_pgo_phase=0 \
           use_clang_modules=false \
           use_system_libffi=true \
           use_dbus=true'
            # remove_webcore_debug_symbols=true \
            # use_clang_modules=false \
            # fieldtrial_testing_like_official_build=true \

           
    shelltools.system("/usr/bin/python3 tools/rust/update_rust.py")
    shelltools.system("/usr/bin/python3 tools/clang/scripts/update.py")    
    clangpath = "%s/chromium-%s/third_party/llvm-build/Release+Asserts/bin" %(get.workDIR(), get.srcVERSION())
    #clangpath = "/usr/bin"

    shelltools.export("CC", "%s/clang" %clangpath)
    shelltools.export("CXX", "%s/clang++" %clangpath)
    shelltools.export("AR", "%s/llvm-ar" %clangpath)
    shelltools.export("NM", "nm" )
    shelltools.export("RANLIB", "ranlib" )
    
    pisitools.cflags.add("-Wno-builtin-macro-redefined -Wno-unknown-warning-option -fdebug-types-section")
    pisitools.cxxflags.add("-Wno-builtin-macro-redefined -Wno-unknown-warning-option -fdebug-types-section")
    pisitools.ldflags.add(" -fuse-ld=lld")
    shelltools.export("CPPFLAGS", "-D__DATE__=  -D__TIME__=  -D__TIMESTAMP__=")
    
    #shelltools.system("/usr/bin/python3 build/download_nacl_toolchains.py --packages nacl_x86_newlib,pnacl_newlib,pnacl_translator sync --extract")
    shelltools.system("/usr/bin/python3 tools/update_pgo_profiles.py --target=linux update --gs-url-base=chromium-optimization-profiles/pgo_profiles")
    shelltools.system("/usr/bin/python3 tools/gn/bootstrap/bootstrap.py --gn-gen-args '%s'"% opt)
    shelltools.system("out/Release/gn gen out/Release --args='%s'"% opt)


    # import os
    # os.makedirs("out/Release/gen/third_party/devtools-frontend/src/front_end/ui/components/code_highlighter/", exist_ok=True)
    # # with open("out/Release/gen/third_party/devtools-frontend/src/front_end/ui/components/code_highlighter/css_files-tsconfig.json", "w") as f:
        # f.write('{"extends": "../../../../../../tsconfig.json"}')


def build():
    #Sandbox for error must remain separate
    shelltools.system("ninja -C out/Release chrome")
    shelltools.system("ninja -C out/Release chrome_sandbox")
    shelltools.system("ninja -C out/Release chromedriver")
    #shelltools.system("ninja -C out/Release widevinecdmadapter")

def install():
    shelltools.cd("out/Release")

    #should be checked should for the missing folder "out/Release"
    for vla in ["*.pak", "*.json", "chrome", "locales", "resources", "icudtl.dat", "mksnapshot", "chromedriver", "snapshot_blob.bin", "character_data_generator", \
			    "libEGL.so", "libGLESv2.so", "libVk*.so", "v8_context_snapshot.bin", "MEIPreload", "chrome_crashpad_handler"]:
        pisitools.insinto("/usr/lib/chromium-browser", "%s" % vla)
	
    pisitools.insinto("/usr/lib/chromium-browser", "chrome_sandbox", "chrome-sandbox")
    pisitools.dosym("/usr/lib/chromium-browser/chrome", "/usr/bin/chromium-browser")
 
    shelltools.system("chmod -v 4755 %s/usr/lib/chromium-browser/chrome-sandbox" %get.installDIR())
    
    shelltools.system("sed -ni \
                      -e '/<update_contact>/d' \
                      -e '/<p>/N;/<p>\n.*\(We invite\|Chromium supports Vorbis\)/,/<\/p>/d' \
                      -e '/^<?xml/,$p' \
                      '../../chrome/installer/linux/common/appdata.xml.template'")
    pisitools.insinto("/usr/share/metainfo", "../../chrome/installer/linux/common/appdata.xml.template", "chromium-browser.appdata.xml")
    pisitools.insinto("/usr/share/man/man1", "../../chrome/app/resources/manpage.1.in", "chromium-browser.1")

    #pisitools.newman("chrome.1", "chromium-browser.1")

    shelltools.cd("../..")
    for size in ["24", "48", "64", "128", "256"]:
        pisitools.insinto("/usr/share/icons/hicolor/%sx%s/apps" %(size, size), "chrome/app/theme/chromium/product_logo_%s.png" % size, "chromium-browser.png")

    pisitools.dosym("/usr/share/icons/hicolor/256x256/apps/chromium-browser.png", "/usr/share/pixmaps/chromium-browser.png")

    pisitools.dodoc("LICENSE")
