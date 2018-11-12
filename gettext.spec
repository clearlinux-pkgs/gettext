#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xD605848ED7E69871 (ueno@gnu.org)
#
Name     : gettext
Version  : 0.19.8.1
Release  : 28
URL      : http://mirrors.kernel.org/gnu/gettext/gettext-0.19.8.1.tar.xz
Source0  : http://mirrors.kernel.org/gnu/gettext/gettext-0.19.8.1.tar.xz
Source99 : http://mirrors.kernel.org/gnu/gettext/gettext-0.19.8.1.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0 GPL-3.0+ LGPL-2.0+ LGPL-2.1 MIT
Requires: gettext-bin = %{version}-%{release}
Requires: gettext-data = %{version}-%{release}
Requires: gettext-lib = %{version}-%{release}
Requires: gettext-license = %{version}-%{release}
Requires: gettext-locales = %{version}-%{release}
Requires: gettext-man = %{version}-%{release}
BuildRequires : acl-dev
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : bison
BuildRequires : emacs
BuildRequires : gettext-bin
BuildRequires : glib-dev
BuildRequires : glibc-locale
BuildRequires : libcroco-dev
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : libxml2-dev
BuildRequires : m4
BuildRequires : ncurses-dev
BuildRequires : pkg-config-dev
Patch1: CVE-2018-18751.patch

%description
This is the GNU gettext package.  It is interesting for authors or
maintainers of other packages or programs which they want to see
internationalized.  As one step the handling of messages in different
languages should be implemented.  For this task GNU gettext provides
the needed tools and library functions.

%package bin
Summary: bin components for the gettext package.
Group: Binaries
Requires: gettext-data = %{version}-%{release}
Requires: gettext-license = %{version}-%{release}
Requires: gettext-man = %{version}-%{release}

%description bin
bin components for the gettext package.


%package data
Summary: data components for the gettext package.
Group: Data

%description data
data components for the gettext package.


%package dev
Summary: dev components for the gettext package.
Group: Development
Requires: gettext-lib = %{version}-%{release}
Requires: gettext-bin = %{version}-%{release}
Requires: gettext-data = %{version}-%{release}
Provides: gettext-devel = %{version}-%{release}

%description dev
dev components for the gettext package.


%package doc
Summary: doc components for the gettext package.
Group: Documentation
Requires: gettext-man = %{version}-%{release}

%description doc
doc components for the gettext package.


%package lib
Summary: lib components for the gettext package.
Group: Libraries
Requires: gettext-data = %{version}-%{release}
Requires: gettext-license = %{version}-%{release}

%description lib
lib components for the gettext package.


%package license
Summary: license components for the gettext package.
Group: Default

%description license
license components for the gettext package.


%package locales
Summary: locales components for the gettext package.
Group: Default

%description locales
locales components for the gettext package.


%package man
Summary: man components for the gettext package.
Group: Default

%description man
man components for the gettext package.


%prep
%setup -q -n gettext-0.19.8.1
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1542039709
export CFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
%reconfigure --disable-static
make

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 check

%install
export SOURCE_DATE_EPOCH=1542039709
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gettext
cp COPYING %{buildroot}/usr/share/package-licenses/gettext/COPYING
cp djgpp/COPYING.DJ %{buildroot}/usr/share/package-licenses/gettext/djgpp_COPYING.DJ
cp gettext-runtime/COPYING %{buildroot}/usr/share/package-licenses/gettext/gettext-runtime_COPYING
cp gettext-runtime/intl/COPYING.LIB %{buildroot}/usr/share/package-licenses/gettext/gettext-runtime_intl_COPYING.LIB
cp gettext-runtime/libasprintf/COPYING %{buildroot}/usr/share/package-licenses/gettext/gettext-runtime_libasprintf_COPYING
cp gettext-runtime/libasprintf/COPYING.LIB %{buildroot}/usr/share/package-licenses/gettext/gettext-runtime_libasprintf_COPYING.LIB
cp gettext-tools/COPYING %{buildroot}/usr/share/package-licenses/gettext/gettext-tools_COPYING
cp gettext-tools/gnulib-lib/libxml/COPYING %{buildroot}/usr/share/package-licenses/gettext/gettext-tools_gnulib-lib_libxml_COPYING
cp gnulib-local/lib/libxml/COPYING %{buildroot}/usr/share/package-licenses/gettext/gnulib-local_lib_libxml_COPYING
%make_install
%find_lang gettext-runtime
%find_lang gettext-tools
## install_append content
rm -rf %{buildroot}/usr/share/doc/gettext/examples/hello-c++*
## install_append end

%files
%defattr(-,root,root,-)
/usr/lib64/gettext/cldr-plurals
/usr/lib64/gettext/hostname
/usr/lib64/gettext/project-id
/usr/lib64/gettext/urlget
/usr/lib64/gettext/user-email

%files bin
%defattr(-,root,root,-)
/usr/bin/autopoint
/usr/bin/envsubst
/usr/bin/gettext
/usr/bin/gettext.sh
/usr/bin/gettextize
/usr/bin/msgattrib
/usr/bin/msgcat
/usr/bin/msgcmp
/usr/bin/msgcomm
/usr/bin/msgconv
/usr/bin/msgen
/usr/bin/msgexec
/usr/bin/msgfilter
/usr/bin/msgfmt
/usr/bin/msggrep
/usr/bin/msginit
/usr/bin/msgmerge
/usr/bin/msgunfmt
/usr/bin/msguniq
/usr/bin/ngettext
/usr/bin/recode-sr-latin
/usr/bin/xgettext

%files data
%defattr(-,root,root,-)
/usr/share/emacs/site-lisp/po-compat.el
/usr/share/emacs/site-lisp/po-compat.elc
/usr/share/emacs/site-lisp/po-mode.el
/usr/share/emacs/site-lisp/po-mode.elc
/usr/share/emacs/site-lisp/start-po.el
/usr/share/emacs/site-lisp/start-po.elc
/usr/share/gettext-0.19.8/its/appdata.its
/usr/share/gettext-0.19.8/its/appdata.loc
/usr/share/gettext-0.19.8/its/glade.loc
/usr/share/gettext-0.19.8/its/glade1.its
/usr/share/gettext-0.19.8/its/glade2.its
/usr/share/gettext-0.19.8/its/gsettings.its
/usr/share/gettext-0.19.8/its/gsettings.loc
/usr/share/gettext-0.19.8/its/gtkbuilder.its
/usr/share/gettext/ABOUT-NLS
/usr/share/gettext/archive.dir.tar.xz
/usr/share/gettext/config.rpath
/usr/share/gettext/gettext.h
/usr/share/gettext/intl/COPYING.LIB
/usr/share/gettext/intl/Makefile.in
/usr/share/gettext/intl/VERSION
/usr/share/gettext/intl/bindtextdom.c
/usr/share/gettext/intl/config.charset
/usr/share/gettext/intl/dcgettext.c
/usr/share/gettext/intl/dcigettext.c
/usr/share/gettext/intl/dcngettext.c
/usr/share/gettext/intl/dgettext.c
/usr/share/gettext/intl/dngettext.c
/usr/share/gettext/intl/eval-plural.h
/usr/share/gettext/intl/explodename.c
/usr/share/gettext/intl/export.h
/usr/share/gettext/intl/finddomain.c
/usr/share/gettext/intl/gettext.c
/usr/share/gettext/intl/gettextP.h
/usr/share/gettext/intl/gmo.h
/usr/share/gettext/intl/hash-string.c
/usr/share/gettext/intl/hash-string.h
/usr/share/gettext/intl/intl-compat.c
/usr/share/gettext/intl/intl-exports.c
/usr/share/gettext/intl/l10nflist.c
/usr/share/gettext/intl/langprefs.c
/usr/share/gettext/intl/libgnuintl.in.h
/usr/share/gettext/intl/libintl.rc
/usr/share/gettext/intl/loadinfo.h
/usr/share/gettext/intl/loadmsgcat.c
/usr/share/gettext/intl/localcharset.c
/usr/share/gettext/intl/localcharset.h
/usr/share/gettext/intl/locale.alias
/usr/share/gettext/intl/localealias.c
/usr/share/gettext/intl/localename.c
/usr/share/gettext/intl/lock.c
/usr/share/gettext/intl/lock.h
/usr/share/gettext/intl/log.c
/usr/share/gettext/intl/ngettext.c
/usr/share/gettext/intl/os2compat.c
/usr/share/gettext/intl/os2compat.h
/usr/share/gettext/intl/osdep.c
/usr/share/gettext/intl/plural-exp.c
/usr/share/gettext/intl/plural-exp.h
/usr/share/gettext/intl/plural.c
/usr/share/gettext/intl/plural.y
/usr/share/gettext/intl/printf-args.c
/usr/share/gettext/intl/printf-args.h
/usr/share/gettext/intl/printf-parse.c
/usr/share/gettext/intl/printf-parse.h
/usr/share/gettext/intl/printf.c
/usr/share/gettext/intl/ref-add.sin
/usr/share/gettext/intl/ref-del.sin
/usr/share/gettext/intl/relocatable.c
/usr/share/gettext/intl/relocatable.h
/usr/share/gettext/intl/setlocale.c
/usr/share/gettext/intl/textdomain.c
/usr/share/gettext/intl/threadlib.c
/usr/share/gettext/intl/tsearch.c
/usr/share/gettext/intl/tsearch.h
/usr/share/gettext/intl/vasnprintf.c
/usr/share/gettext/intl/vasnprintf.h
/usr/share/gettext/intl/vasnwprintf.h
/usr/share/gettext/intl/verify.h
/usr/share/gettext/intl/version.c
/usr/share/gettext/intl/wprintf-parse.h
/usr/share/gettext/intl/xsize.c
/usr/share/gettext/intl/xsize.h
/usr/share/gettext/javaversion.class
/usr/share/gettext/msgunfmt.tcl
/usr/share/gettext/po/Makefile.in.in
/usr/share/gettext/po/Makevars.template
/usr/share/gettext/po/Rules-quot
/usr/share/gettext/po/boldquot.sed
/usr/share/gettext/po/en@boldquot.header
/usr/share/gettext/po/en@quot.header
/usr/share/gettext/po/insert-header.sin
/usr/share/gettext/po/quot.sed
/usr/share/gettext/po/remove-potcdate.sin
/usr/share/gettext/projects/GNOME/team-address
/usr/share/gettext/projects/GNOME/teams.html
/usr/share/gettext/projects/GNOME/teams.url
/usr/share/gettext/projects/GNOME/trigger
/usr/share/gettext/projects/KDE/team-address
/usr/share/gettext/projects/KDE/teams.html
/usr/share/gettext/projects/KDE/teams.url
/usr/share/gettext/projects/KDE/trigger
/usr/share/gettext/projects/TP/team-address
/usr/share/gettext/projects/TP/teams.html
/usr/share/gettext/projects/TP/teams.url
/usr/share/gettext/projects/TP/trigger
/usr/share/gettext/projects/index
/usr/share/gettext/projects/team-address
/usr/share/gettext/styles/po-default.css
/usr/share/gettext/styles/po-emacs-x.css
/usr/share/gettext/styles/po-emacs-xterm.css
/usr/share/gettext/styles/po-emacs-xterm16.css
/usr/share/gettext/styles/po-emacs-xterm256.css
/usr/share/gettext/styles/po-vim.css

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/libasprintf.so
/usr/lib64/libgettextlib-0.19.8.1.so
/usr/lib64/libgettextlib.so
/usr/lib64/libgettextpo.so
/usr/lib64/libgettextsrc-0.19.8.1.so
/usr/lib64/libgettextsrc.so
/usr/lib64/preloadable_libintl.so
/usr/share/aclocal/*.m4
/usr/share/man/man3/bind_textdomain_codeset.3
/usr/share/man/man3/bindtextdomain.3
/usr/share/man/man3/dcgettext.3
/usr/share/man/man3/dcngettext.3
/usr/share/man/man3/dgettext.3
/usr/share/man/man3/dngettext.3
/usr/share/man/man3/gettext.3
/usr/share/man/man3/ngettext.3
/usr/share/man/man3/textdomain.3

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/gettext/*
%doc /usr/share/info/*
/usr/share/doc/libasprintf/autosprintf_all.html

%files lib
%defattr(-,root,root,-)
/usr/lib64/libasprintf.so.0
/usr/lib64/libasprintf.so.0.0.0
/usr/lib64/libgettextpo.so.0
/usr/lib64/libgettextpo.so.0.5.4

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gettext/COPYING
/usr/share/package-licenses/gettext/djgpp_COPYING.DJ
/usr/share/package-licenses/gettext/gettext-runtime_COPYING
/usr/share/package-licenses/gettext/gettext-runtime_intl_COPYING.LIB
/usr/share/package-licenses/gettext/gettext-runtime_libasprintf_COPYING
/usr/share/package-licenses/gettext/gettext-runtime_libasprintf_COPYING.LIB
/usr/share/package-licenses/gettext/gettext-tools_COPYING
/usr/share/package-licenses/gettext/gettext-tools_gnulib-lib_libxml_COPYING
/usr/share/package-licenses/gettext/gnulib-local_lib_libxml_COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/autopoint.1
/usr/share/man/man1/envsubst.1
/usr/share/man/man1/gettext.1
/usr/share/man/man1/gettextize.1
/usr/share/man/man1/msgattrib.1
/usr/share/man/man1/msgcat.1
/usr/share/man/man1/msgcmp.1
/usr/share/man/man1/msgcomm.1
/usr/share/man/man1/msgconv.1
/usr/share/man/man1/msgen.1
/usr/share/man/man1/msgexec.1
/usr/share/man/man1/msgfilter.1
/usr/share/man/man1/msgfmt.1
/usr/share/man/man1/msggrep.1
/usr/share/man/man1/msginit.1
/usr/share/man/man1/msgmerge.1
/usr/share/man/man1/msgunfmt.1
/usr/share/man/man1/msguniq.1
/usr/share/man/man1/ngettext.1
/usr/share/man/man1/recode-sr-latin.1
/usr/share/man/man1/xgettext.1

%files locales -f gettext-runtime.lang -f gettext-tools.lang
%defattr(-,root,root,-)

