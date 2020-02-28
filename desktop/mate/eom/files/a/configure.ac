AC_PREREQ(2.59)
AC_CONFIG_MACRO_DIR([m4])

m4_define(eom_major_version, 1)
m4_define(eom_minor_version, 22)
m4_define(eom_micro_version, 2)
m4_define(eom_version, eom_major_version.eom_minor_version.eom_micro_version)

AC_INIT([eom], eom_version, [http://www.mate-desktop.org], [eom])
AM_INIT_AUTOMAKE([1.9 foreign no-dist-gzip dist-xz check-news])

# Support silencing the build output if supported (automake-1.11+)
m4_ifdef([AM_SILENT_RULES],[AM_SILENT_RULES([yes])])

AC_DEFINE(EOM_MAJOR_VERSION, eom_major_version, [EOM major version])
AC_SUBST(EOM_MAJOR_VERSION,  eom_major_version)
AC_DEFINE(EOM_MINOR_VERSION, eom_minor_version, [EOM minor version])
AC_SUBST(EOM_MINOR_VERSION,  eom_minor_version)
AC_DEFINE(EOM_MICRO_VERSION, eom_micro_version, [EOM micro version])
AC_SUBST(EOM_MICRO_VERSION,  eom_micro_version)

EOM_API_VERSION=2.20
AC_SUBST(EOM_API_VERSION)

AC_CONFIG_HEADERS([config.h])

AM_MAINTAINER_MODE

MATE_COMMON_INIT
MATE_MAINTAINER_MODE_DEFINES
MATE_COMPILE_WARNINGS
MATE_DEBUG_CHECK

# Disable building static archives by default
AC_DISABLE_STATIC
AC_PROG_LIBTOOL

AC_PROG_CC
AM_PROG_CC_C_O
AC_PATH_PROG([GLIB_COMPILE_RESOURCES], [glib-compile-resources])
AC_PATH_PROG([GLIB_GENMARSHAL], [glib-genmarshal])
AC_PATH_PROG([GLIB_MKENUMS],[glib-mkenums])

GTK_DOC_CHECK(1.9)

AC_CHECK_FUNCS(strptime)

# ****************************************************************
# Support for nl_langinfo (_NL_MEASUREMENT_MEASUREMENT) (optional)
# ****************************************************************
AC_MSG_CHECKING([for _NL_MEASUREMENT_MEASUREMENT])
AC_TRY_LINK([#include <langinfo.h>], [
char c;
c = *((unsigned char *)  nl_langinfo(_NL_MEASUREMENT_MEASUREMENT));
], have_langinfo_measurement=yes, have_langinfo_measurement=no)
AC_MSG_RESULT($have_langinfo_measurement)
if test "$have_langinfo_measurement" = "yes"; then
  AC_DEFINE([HAVE__NL_MEASUREMENT_MEASUREMENT], [1],
            [Define if _NL_MEASUREMENT_MEASUREMENT is available])
fi

# ***********
# Translation
# ***********

AM_GLIB_GNU_GETTEXT
IT_PROG_INTLTOOL([0.50.1])

GETTEXT_PACKAGE=AC_PACKAGE_NAME
AC_SUBST(GETTEXT_PACKAGE)
AC_DEFINE_UNQUOTED(GETTEXT_PACKAGE, "$GETTEXT_PACKAGE", [Gettext package.])

AC_SUBST(CFLAGS)
AC_SUBST(LDFLAGS)

# ***************
# mate-doc-utils
# ***************

PKG_PROG_PKG_CONFIG

YELP_HELP_INIT

# **********
# MATE Libs
# **********

GLIB_REQUIRED=2.52.0
GIO_REQUIRED=2.50.0
GTK_REQUIRED=3.22.0
MATE_DESKTOP_REQUIRED=1.17.0
GDKPIXBUF_REQUIRED=2.30.0
SHARED_MIME_INFO_REQUIRED=0.20
EXEMPI_REQUIRED=1.99.5
LIBPEAS_REQUIRED=1.8.0

PKG_CHECK_MODULES(GMODULE, gmodule-2.0, [GMODULE_ADD="gmodule-2.0"],[GMODULE_ADD=""])
EOM_MODULES="gtk+-3.0 >= $GTK_REQUIRED \
             glib-2.0 >= $GLIB_REQUIRED \
             $GMODULE_ADD \
             gio-2.0 >= $GLIB_REQUIRED \
             gio-unix-2.0 >= $GLIB_REQUIRED \
             gthread-2.0 >= $GLIB_REQUIRED \
             mate-desktop-2.0 >= $MATE_DESKTOP_REQUIRED \
             gdk-pixbuf-2.0 >= $GDKPIXBUF_REQUIRED \
             gio-2.0 >= $GIO_REQUIRED \
             gtk+-unix-print-3.0 >= $GTK_REQUIRED \
             shared-mime-info >= $SHARED_MIME_INFO_REQUIRED \
             libpeas-1.0 >= $LIBPEAS_REQUIRED \
             libpeas-gtk-1.0 >= $LIBPEAS_REQUIRED"

# Introspection
GOBJECT_INTROSPECTION_CHECK([0.9.3])

if test "$found_introspection" = "yes"; then
	have_introspection=yes
	AC_DEFINE([HAVE_INTROSPECTION], [1], [Define to enable GObject Introspection])
else
	have_introspection=no
fi

AM_CONDITIONAL(HAVE_INTROSPECTION, test "x$have_introspection" = xyes)

# ***************
# ZLIB (required)
# ***************

have_zlib=yes
AC_CHECK_HEADERS([zlib.h],
	[AC_CHECK_LIB([z], [inflate],
		[AC_CHECK_LIB([z], [crc32], [], [have_zlib=no])],
		[have_zlib=no])],
	[have_zlib=no])

if test x$have_zlib = xno; then
	AC_MSG_ERROR([No sufficient zlib library found on your system.])
fi

# ***************
# EXIF (optional)
# ***************

LIBEXIF_REQUIRED=0.6.14

AC_ARG_WITH([libexif], AC_HELP_STRING([--without-libexif], [disable EXIF support]))
have_exif=no
if test x$with_libexif != xno; then
    PKG_CHECK_MODULES(EXIF, libexif >= $LIBEXIF_REQUIRED, have_exif=yes, have_exif=no)
fi
if test "x$have_exif" = "xyes"; then
  AC_DEFINE(HAVE_EXIF, 1, [EXIF Support.])
  EOM_MODULES="$EOM_MODULES libexif >= $LIBEXIF_REQUIRED"
fi

AM_CONDITIONAL([HAVE_EXIF], [test "x$have_exif" = "xyes"])

# *********************
# Little CMS (optional)
# *********************

AC_ARG_WITH([cms], AC_HELP_STRING([--without-cms], [disable colour management support]))
have_lcms=no
if test x$with_cms != xno; then
    PKG_CHECK_MODULES(LCMS, lcms2, have_lcms=yes, have_lcms=no)
fi
if test "x$have_lcms" = "xyes"; then
  AC_DEFINE(HAVE_LCMS, 1, [Little CMS Support.])
  EOM_MODULES="$EOM_MODULES lcms2"
fi

AM_CONDITIONAL([HAVE_LCMS], [test "x$have_lcms" = "xyes"])

# *********************
# Exempi (optional)
# *********************
AC_ARG_WITH(xmp, AC_HELP_STRING([--without-xmp], [disable special XMP support]))
have_exempi=no
if test x$with_xmp != xno; then
    PKG_CHECK_MODULES(EXEMPI, exempi-2.0 >= $EXEMPI_REQUIRED, have_exempi=yes, have_exempi=no)
fi
if test "x$have_exempi" = "xyes"; then
  AC_DEFINE(HAVE_EXEMPI,1, [XMP support.])
  EOM_MODULES="$EOM_MODULES exempi-2.0 >= $EXEMPI_REQUIRED"
fi

AM_CONDITIONAL([HAVE_EXEMPI], [test "x$have_exempi" = "xyes"])

# Build EXIF-related documentation if we really have support for it
if test "x$have_exif" = "xyes" || test "x$have_exempi" = "xyes"; then
  EOM_DOC_EXIF_START=""
  EOM_DOC_EXIF_STOP=""
else
  EOM_DOC_EXIF_START="<!--"
  EOM_DOC_EXIF_STOP="-->"
fi

AC_SUBST([EOM_DOC_EXIF_START])
AC_SUBST([EOM_DOC_EXIF_STOP])

# ********************
# Jpeg (semi-optional)
# ********************

AC_ARG_WITH(libjpeg, AC_HELP_STRING([--without-libjpeg], [disable special JPEG support]))
  have_jpeg=no
  have_libjpeg_80=no
  if test x$with_libjpeg != xno && test -z "$LIBJPEG"; then
    AC_CHECK_LIB(jpeg, jpeg_destroy_decompress,
      have_jpeg=yes,
      have_jpeg=no
      AC_MSG_WARN(*** JPEG loader will not be built (JPEG library not found) ***))
    if test "$have_jpeg" = yes; then
      AC_MSG_CHECKING([for jpeglib.h])
      AC_TRY_CPP(
[#include <stdio.h>
#undef PACKAGE
#undef VERSION
#undef HAVE_STDLIB_H
#include <jpeglib.h>],
        have_jpeg=yes,
        have_jpeg=no)
      AC_MSG_RESULT($have_jpeg)
      if test "$have_jpeg" = yes; then
        LIBJPEG='-ljpeg'
	AC_DEFINE(HAVE_JPEG, 1, [Jpeg Support.])
        AC_DEFINE(HAVE_LIBJPEG, 1, [libjpeg is Present.])
        AC_CHECK_LIB(jpeg, jpeg_simple_progression,
          AC_DEFINE(HAVE_PROGRESSIVE_JPEG, 1, [Jpeg Progressive Saving Support.]),
          AC_MSG_WARN(JPEG library does not support progressive saving.))
	AC_MSG_CHECKING([[libjpeg version is 8 or greater]])
	AC_PREPROC_IFELSE([ AC_LANG_SOURCE(
			  [[
#include <stdio.h>
#include <jpeglib.h>
#if JPEG_LIB_VERSION < 80
#error "wrong version"
#endif
int main(int c, char**v) { return 0; }
			  ]]) ],
			  [AC_MSG_RESULT(yes)
			   have_libjpeg_80=yes],
		          [AC_MSG_RESULT(no)
		           have_libjpeg_80=no])

      else
          AC_MSG_WARN(*** JPEG loader will not be built (JPEG header file not found) ***)
      fi
    fi
  fi

  if test x$with_libjpeg != xno && test -z "$LIBJPEG"; then
     AC_MSG_ERROR([
*** Checks for JPEG loader failed. You can build without it by passing
*** --without-libjpeg to configure but some programs using GTK+ may
*** not work properly])
  fi
AC_SUBST(LIBJPEG)
AM_CONDITIONAL(ENABLE_JPEG, test x$have_jpeg = xyes)
AM_CONDITIONAL(HAVE_LIBJPEG_80, test "x$have_libjpeg_80" = xyes)

# ************************************
# libXML2 (required for toolbareditor)
# ************************************

LIBXML2_REQUIRED=2.0
PKG_CHECK_MODULES(LIBXML2, [libxml-2.0 >= $LIBXML2_REQUIRED])

# ***************
# RSVG (optional for scaling svg image)
# ***************

LIBRSVG_REQUIRED=2.36.2

AC_ARG_WITH([librsvg], AC_HELP_STRING([--without-librsvg], [disable RSVG support]))
have_rsvg=no
if test x$with_librsvg != xno; then
    PKG_CHECK_MODULES(RSVG, librsvg-2.0 >= $LIBRSVG_REQUIRED, have_rsvg=yes, have_rsvg=no)
fi
if test "x$have_rsvg" = "xyes"; then
  AC_DEFINE(HAVE_RSVG, 1, [RSVG Support.])
  EOM_MODULES="$EOM_MODULES librsvg-2.0 >= $LIBRSVG_REQUIRED"
else
  AC_WARN([LIBRSVG support disabled, svg files will not scale])
fi

AM_CONDITIONAL([HAVE_RSVG], [test "x$have_rsvg" = "xyes"])

# ****************
# CFLAGS/LIBS init
# ****************

PKG_CHECK_MODULES(EOM, $EOM_MODULES)
AC_SUBST(EOM_CFLAGS)
AC_SUBST(EOM_LIBS)

# *******************************************************
# libX11 (required for TotemScrSaver and Color Profiling)
# *******************************************************

# Check GDK rendering target
gdk_target_has_x11=`$PKG_CONFIG --variable=targets gdk-3.0 | grep x11`

if test "x$have_lcms" = "xyes" || test "$gdk_target_has_x11" != ""; then
	PKG_CHECK_MODULES(X11, [x11], have_x11=yes, have_x11=no)

	if test "x$have_x11" != "xyes"; then
		# Fallback for X11 releases without .pc-files
		AC_PATH_XTRA
		if test x$no_x = xyes ; then
			AC_MSG_ERROR([X development libraries (libX11) not found])
		else
			X11_LIBS="$X_PRE_LIBS $X_LIBS -lX11 $X_EXTRA_LIBS"
			AC_SUBST(X11_LIBS)
			have_x11=yes
		fi
	fi
fi

# *****
# GSettings
# *****

GLIB_GSETTINGS

AC_SEARCH_LIBS([floor],[m])

AC_CONFIG_FILES([
Makefile
src/Makefile
man/Makefile
jpegutils/Makefile
cut-n-paste/Makefile
cut-n-paste/toolbar-editor/Makefile
help/Makefile
po/Makefile.in
data/Makefile
data/eom.pc
data/eom.desktop.in
data/org.mate.eom.gschema.xml
data/pixmaps/Makefile
data/icons/Makefile
data/icons/16x16/Makefile
data/icons/22x22/Makefile
data/icons/24x24/Makefile
data/icons/32x32/Makefile
data/icons/48x48/Makefile
data/icons/scalable/Makefile
doc/Makefile
doc/reference/Makefile
doc/reference/version.xml
doc/reference/eom-docs.sgml
plugins/Makefile
])

AC_OUTPUT

echo "
Configure summary:

	Source code location .......:  ${srcdir}
	Compiler ...................:  ${CC}
	Extra Compiler Warnings ....:  ${WARN_CFLAGS}

	EXIF support ...............:  ${have_exif}
	XMP support ................:  ${have_exempi}
	JPEG support ...............:  ${have_jpeg}
	RSVG support ...............:  ${have_rsvg}
	Colour management support ..:  ${have_lcms}
	GObject Introspection.......:  ${have_introspection}
"
