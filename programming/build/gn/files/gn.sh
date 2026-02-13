#!/bin/bash

set -e

PROJECT_NAME="gn-2026.02.04"
ARCHIVE_NAME="gn-2026.02.04"
# Burayı değiştirdik:
GIT_REPO_URL="https://gn.googlesource.com/gn"
COMMIT_ID="304bbef6c7e9a86630c12986b99c8654eb7fe648"

echo "glibc projesi için arşiv oluşturuluyor..."

if [ -d "$PROJECT_NAME" ]; then
    echo "Mevcut $PROJECT_NAME klasörü siliniyor..."
    rm -rf "$PROJECT_NAME"
fi

echo "Git deposu klonlanıyor: $GIT_REPO_URL"
git clone "$GIT_REPO_URL" "$PROJECT_NAME"

cd "$PROJECT_NAME"

if [ -n "$COMMIT_ID" ]; then
    echo "Belirtilen commit ID'sine geçiliyor: $COMMIT_ID"
    git checkout "$COMMIT_ID"
else
    echo "En son master branch'i kullanılıyor."
    git pull origin master
fi

echo "Git geçmişi temizleniyor..."
# find . -type d -name ".git" | xargs rm -rf

cd ..

echo "Arşiv oluşturuluyor: $ARCHIVE_NAME.tar.xz"
tar -cJvf "$ARCHIVE_NAME.tar.xz" "$PROJECT_NAME"

echo "Geçici $PROJECT_NAME klasörü siliniyor..."
# rm -rf "$PROJECT_NAME"

echo "Arşiv başarıyla oluşturuldu: $ARCHIVE_NAME.tar.xz"
