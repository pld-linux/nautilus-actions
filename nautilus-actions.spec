Summary:	Nautilus extension which adds customized command in Nautilus menu
Summary(pl.UTF-8):	Rozszerzenie dodające własne polecenia w menu Nautilusa
Name:		nautilus-actions
Version:	3.1.2
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/nautilus-actions/3.1/%{name}-%{version}.tar.bz2
# Source0-md5:	7223c974d210cc90dbddfe5364d1f71b
Patch0:		%{name}-desktop.patch
URL:		http://www.grumz.net/node/8/
BuildRequires:	GConf2-devel >= 2.8.0
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	dbus-glib-devel
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.16.0
BuildRequires:	gnome-common
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libgtop-devel >= 1:2.23.1
BuildRequires:	libtool
BuildRequires:	libunique-devel
BuildRequires:	libuuid-devel
BuildRequires:	libxml2-devel >= 1:2.6.26
BuildRequires:	nautilus-devel >= 3.0.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	xorg-lib-libSM-devel
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	nautilus >= 3.0.0
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
Requires:	glib2-devel >= 1:2.16.0

%description devel
Header files for nautilus-actions.

%description devel -l pl.UTF-8
Pliki nagłówkowe nautilus-actions.

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
	--disable-schemas-install

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-3.0/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/nautilus-actions/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/nautilus-actions-config-tool
%attr(755,root,root) %{_bindir}/nautilus-actions-new
%attr(755,root,root) %{_bindir}/nautilus-actions-print
%attr(755,root,root) %{_bindir}/nautilus-actions-run
%dir %{_libdir}/nautilus-actions
%attr(755,root,root) %{_libdir}/nautilus-actions/na-delete-xmltree
%attr(755,root,root) %{_libdir}/nautilus-actions/na-gconf2key.sh
%attr(755,root,root) %{_libdir}/nautilus-actions/na-print-schemas
%attr(755,root,root) %{_libdir}/nautilus-actions/libna-core.so
%attr(755,root,root) %{_libdir}/nautilus-actions/libna-io-desktop.so
%attr(755,root,root) %{_libdir}/nautilus-actions/libna-io-gconf.so
%attr(755,root,root) %{_libdir}/nautilus-actions/libna-io-xml.so
%{_datadir}/%{name}
%{_desktopdir}/nact.desktop
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/*/apps/*.svg
%attr(755,root,root) %{_libdir}/nautilus/extensions-3.0/libnautilus-actions-menu.so
%attr(755,root,root) %{_libdir}/nautilus/extensions-3.0/libnautilus-actions-tracker.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/nautilus-actions
