export KF5=/usr
export QTDIR=/usr/lib/qt5
export XDG_DATA_DIRS=$KF5/share:$XDG_DATA_DIRS:/usr/share
export XDG_CONFIG_DIRS=$XDG_CONFIG_DIRS:/etc/xdg
export PATH=$KF5/bin:$QTDIR/bin:$PATH
export QT_PLUGIN_PATH=$QTDIR/plugins:$QT_PLUGIN_PATH
export QML2_IMPORT_PATH=/usr/lib/qt5/qml:/usr/lib/qt5/qmldir
export QML_IMPORT_PATH=$QML2_IMPORT_PATH
export KDE_SESSION_VERSION=5
export KDE_FULL_SESSION=true
#separete
export XDG_DATA_HOME=$HOME/.local/share
export XDG_CONFIG_HOME=$HOME/.config
export XDG_CACHE_HOME=$HOME/.cache
#export XDG_RUNTIME_DIR=/tmp/runtime-$USER
#build
export CMAKE_PREFIX_PATH=$KF5:$CMAKE_PREFIX_PATH
#debug
export QT_MESSAGE_PATTERN='%{appname}(%{pid})/%{category} %{function}: %{message}'
