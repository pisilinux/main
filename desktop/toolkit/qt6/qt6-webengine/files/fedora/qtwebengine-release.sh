#!/bin/sh
set -x
VERSION=5.15.5
CHROMIUMHASH=`wget https://code.qt.io/cgit/qt/qtwebengine.git/tree/src/3rdparty?h=$VERSION -q --content-on-error -O - | grep "Bad object name: " | sed 's/^.*Bad object name: \([0-9a-f]\{40\}\).*$/\1/g'`
rm -rf qtwebengine-$VERSION qtwebengine-$VERSION.tar.gz qtwebengine-chromium-$CHROMIUMHASH qtwebengine-chromium-$CHROMIUMHASH.tar.gz qtwebengine-everywhere-opensource-src-$VERSION
wget https://github.com/qt/qtwebengine/archive/$VERSION.tar.gz -O qtwebengine-$VERSION.tar.gz || exit $?
tar xzf qtwebengine-$VERSION.tar.gz || exit $?
wget https://github.com/qt/qtwebengine-chromium/archive/$CHROMIUMHASH.tar.gz -O qtwebengine-chromium-$CHROMIUMHASH.tar.gz || exit $?
tar xzf qtwebengine-chromium-$CHROMIUMHASH.tar.gz || exit $?
mv qtwebengine-$VERSION qtwebengine-everywhere-opensource-src-$VERSION || exit $?
cd qtwebengine-everywhere-opensource-src-$VERSION ; syncqt.pl -version $VERSION || exit $?
rmdir ../qtwebengine-everywhere-opensource-src-$VERSION/src/3rdparty || exit $?
mv ../qtwebengine-chromium-$CHROMIUMHASH src/3rdparty || exit $?
# cd ..
# XZ_OPT=-9 tar cJf qtwebengine-everywhere-opensource-src-$VERSION.tar.xz qtwebengine-everywhere-opensource-src-$VERSION || exit $?
# rm -rf qtwebengine-$VERSION qtwebengine-$VERSION.tar.gz qtwebengine-chromium-$CHROMIUMHASH qtwebengine-chromium-$CHROMIUMHASH.tar.gz qtwebengine-everywhere-opensource-src-$VERSION
