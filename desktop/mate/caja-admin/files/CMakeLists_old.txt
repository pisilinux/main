cmake_minimum_required(VERSION 2.6)
project(CajaAdmin NONE)
find_package(Gettext REQUIRED)

# Configurable paths
set(PKEXEC_PATH "/usr/bin/pkexec" CACHE FILEPATH "pkexec program path.")
set(CAJA_PATH "/usr/bin/caja" CACHE FILEPATH "caja program path.")
set(PLUMA_PATH "/usr/bin/pluma" CACHE FILEPATH "pluma program path.")
set(TERMINAL_PATH "/usr/bin/mate-terminal" CACHE FILEPATH "mate-terminal program path.")

# Configure files
configure_file(extension/caja-admin.py.in
               extension/caja-admin.py)
configure_file(polkit/org.freedesktop.caja-admin.policy.in
               polkit/org.freedesktop.caja-admin.policy)

# Update and compile the translations
gettext_create_translations(po/caja-admin.pot ALL
	po/ar.po
	po/de.po
	po/es.po
	po/fr.po
	po/it.po
	po/lt.po
	po/pl.po
	po/pt.po
	po/ru.po
	po/sk.po
	po/zh_CN.po)

# Install target
install(FILES "${CMAKE_CURRENT_BINARY_DIR}/polkit/org.freedesktop.caja-admin.policy"
        DESTINATION /usr/share/polkit-1/actions)
install(FILES "${CMAKE_CURRENT_BINARY_DIR}/extension/caja-admin.py"
        DESTINATION /usr/share/caja-python/extensions)

# Uninstall target
configure_file("${CMAKE_CURRENT_SOURCE_DIR}/cmake/cmake_uninstall.cmake.in"
               "${CMAKE_CURRENT_BINARY_DIR}/cmake/cmake_uninstall.cmake" IMMEDIATE @ONLY)
add_custom_target(uninstall COMMAND ${CMAKE_COMMAND}
                  -P ${CMAKE_CURRENT_BINARY_DIR}/cmake/cmake_uninstall.cmake)
