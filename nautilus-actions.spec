# NOTE: for versions >= 3.4 see filemanager-actions.spec
#
# Conditinal build:
%bcond_without	apidocs		# disable API documentation

Summary:	Nautilus extension which adds customized command in Nautilus menu
Summary(pl.UTF-8):	Rozszerzenie dodające własne polecenia w menu Nautilusa
Name:		nautilus-actions
Version:	3.2.4
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/nautilus-actions/3.2/%{name}-%{version}.tar.xz
# Source0-md5:	998eee031a4dd25115c201b776f82ed2
Patch0:		%{name}-desktop.patch
URL:		http://www.grumz.net/node/8/
BuildRequires:	GConf2-devel >= 2.8.0
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	gettext-tools
# minimum is glib 2.24; 2.30 to replace dbus-glib
BuildRequires:	glib2-devel >= 1:2.30
BuildRequires:	gnome-common
BuildRequires:	gnome-doc-utils
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	gtk-doc >= 1.16
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libgtop-devel >= 1:2.23.1
BuildRequires:	libtool
BuildRequires:	libunique3-devel >= 3.0
BuildRequires:	libuuid-devel
BuildRequires:	libxml2-devel >= 1:2.6.26
BuildRequires:	nautilus-devel >= 3.0.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libSM-devel >= 1.0
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	GConf2 >= 2.8.0
Requires:	glib2 >= 1:2.30
Requires:	libgtop >= 1:2.23.1
Requires:	libxml2 >= 1:2.6.26
Requires:	nautilus >= 3.0.0
Requires:	xorg-lib-libSM >= 1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nautilus extension which allow to configure program to be launch on
files selected into Nautilus interface.

%description -l pl.UTF-8
Rozszerzenie pozwalające na skonfigurowanie programu uruchamianego na
pliku wybranym w Nautilusie.

%package devel
Summary:	Header files for nautilus-actions
Summary(pl.UTF-8):	Pliki nagłówkowe nautilus-actions
Group:		X11/Development/Libraries
Requires:	GConf2-devel >= 2.8.0
Requires:	glib2-devel >= 1:2.30

%description devel
Header files for nautilus-actions.

%description devel -l pl.UTF-8
Pliki nagłówkowe nautilus-actions.

%package apidocs
Summary:	Nautilus Actions API documentation
Summary(pl.UTF-8):	Dokumentacja API Nautilus Actions
Group:		Documentation
Requires:	gtk-doc-common
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
Nautilus Actions API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API Nautilus Actions.

%prep
%setup -q
%patch0 -p1

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-schemas-install \
	--enable-gtk-doc%{!?with_apidocs:=no} \
	--with-gtk=3 \
	--with-html-dir=%{_gtkdocdir} \

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf docs-installed
cp -a $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version} docs-installed
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%{__rm} $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-3.0/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/nautilus-actions/*.la

%{!?with_apidocs:%{__rm} -rf $RPM_BUILD_ROOT%{_gtkdocdir}}

%find_lang %{name} --with-gnome --with-omf --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc docs-installed/*
%attr(755,root,root) %{_bindir}/nautilus-actions-config-tool
%attr(755,root,root) %{_bindir}/nautilus-actions-new
%attr(755,root,root) %{_bindir}/nautilus-actions-print
%attr(755,root,root) %{_bindir}/nautilus-actions-run
%dir %{_libdir}/nautilus-actions
%attr(755,root,root) %{_libdir}/nautilus-actions/libna-core.so
%attr(755,root,root) %{_libdir}/nautilus-actions/libna-io-desktop.so
%attr(755,root,root) %{_libdir}/nautilus-actions/libna-io-gconf.so
%attr(755,root,root) %{_libdir}/nautilus-actions/libna-io-xml.so
%attr(755,root,root) %{_libdir}/nautilus-actions/na-delete-xmltree
%attr(755,root,root) %{_libdir}/nautilus-actions/na-gconf2key.sh
%attr(755,root,root) %{_libdir}/nautilus-actions/na-print-schemas
%attr(755,root,root) %{_libdir}/nautilus-actions/na-set-conf
%{_datadir}/%{name}
%{_desktopdir}/nact.desktop
%{_iconsdir}/hicolor/*x*/apps/nautilus-actions.png
%{_iconsdir}/hicolor/scalable/apps/nautilus-actions.svg
%attr(755,root,root) %{_libdir}/nautilus/extensions-3.0/libnautilus-actions-menu.so
%attr(755,root,root) %{_libdir}/nautilus/extensions-3.0/libnautilus-actions-tracker.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/nautilus-actions

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/nautilus-actions-3
%endif
