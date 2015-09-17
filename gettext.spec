#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gettext
Version  : 0.19.6
Release  : 15
URL      : http://mirrors.kernel.org/gnu/gettext/gettext-0.19.6.tar.xz
Source0  : http://mirrors.kernel.org/gnu/gettext/gettext-0.19.6.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0 GPL-3.0 GPL-3.0+ LGPL-2.0+ LGPL-2.1 MIT
Requires: gettext-bin
Requires: gettext-lib
Requires: gettext-doc
Requires: gettext-data
Requires: gettext-locales
BuildRequires : acl-dev
BuildRequires : bison
BuildRequires : emacs
BuildRequires : glib-dev
BuildRequires : libtool-dev
BuildRequires : libxml2
BuildRequires : ncurses-dev

%description
This is the GNU gettext package.  It is interesting for authors or
maintainers of other packages or programs which they want to see
internationalized.  As one step the handling of messages in different
languages should be implemented.  For this task GNU gettext provides
the needed tools and library functions.

%package bin
Summary: bin components for the gettext package.
Group: Binaries
Requires: gettext-data

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
Requires: gettext-lib
Requires: gettext-bin
Requires: gettext-data
Provides: gettext-devel

%description dev
dev components for the gettext package.


%package doc
Summary: doc components for the gettext package.
Group: Documentation

%description doc
doc components for the gettext package.


%package lib
Summary: lib components for the gettext package.
Group: Libraries
Requires: gettext-data

%description lib
lib components for the gettext package.


%package locales
Summary: locales components for the gettext package.
Group: Default

%description locales
locales components for the gettext package.


%prep
%setup -q -n gettext-0.19.6

%build
%configure --disable-static
make V=1

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install
%find_lang gettext-runtime
%find_lang gettext-tools
## make_install_append content
rm -rf %{buildroot}/usr/share/doc/gettext/examples/hello-c++*
## make_install_append end

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
/usr/share/doc/libasprintf/autosprintf_all.html
/usr/share/emacs/site-lisp/po-compat.el
/usr/share/emacs/site-lisp/po-compat.elc
/usr/share/emacs/site-lisp/po-mode.el
/usr/share/emacs/site-lisp/po-mode.elc
/usr/share/emacs/site-lisp/start-po.el
/usr/share/emacs/site-lisp/start-po.elc
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
/usr/lib64/*.so
/usr/share/aclocal/*.m4

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/gettext/*
%doc /usr/share/info/*
%doc /usr/share/man/man1/*
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*

%files locales -f gettext-runtime.lang -f gettext-tools.lang 
%defattr(-,root,root,-)

