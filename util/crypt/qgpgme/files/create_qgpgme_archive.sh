#!/bin/bash

set -e

PROJECT_NAME="qgpgme"
ARCHIVE_NAME="qgpgme-2.0.0"
# Burayı değiştirdik:
GIT_REPO_URL="https://dev.gnupg.org/source/gpgmeqt.git"
COMMIT_ID="2e002d8024b9625ca4bd2cb0f1777835e2e5fcd2"

echo "GPGMEPP projesi için arşiv oluşturuluyor..."

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
find . -type d -name ".git" | xargs rm -rf

cd ..

echo "Arşiv oluşturuluyor: $ARCHIVE_NAME.tar.xz"
tar -cJvf "$ARCHIVE_NAME.tar.xz" "$PROJECT_NAME"

echo "Geçici $PROJECT_NAME klasörü siliniyor..."
rm -rf "$PROJECT_NAME"

echo "Arşiv başarıyla oluşturuldu: $ARCHIVE_NAME.tar.xz"
