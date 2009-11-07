Summary:	Nautilus extension which adds customized command in Nautilus menu
Summary(pl.UTF-8):	Rozszerzenie dodające własne polecenia w menu Nautilusa
Name:		nautilus-actions
Version:	1.12.3
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/nautilus-actions/1.12/%{name}-%{version}.tar.bz2
# Source0-md5:	0f83eea8306593cf807ed26f4c1479aa
Patch0:		%{name}-desktop.patch
URL:		http://www.grumz.net/node/8/
BuildRequires:	GConf2-devel >= 2.8.0
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.16.0
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRequires:	gnome-common
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libtool
BuildRequires:	libunique-devel
BuildRequires:	libuuid-devel
BuildRequires:	libxml2-devel >= 1:2.6.26
BuildRequires:	nautilus-devel >= 2.22.0
BuildRequires:	rpmbuild(macros) >= 1.311
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires:	nautilus >= 2.22.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nautilus extension which allow to configure program to be launch on
files selected into Nautilus interface.

%description -l pl.UTF-8
Rozszerzenie pozwalające na skonfigurowanie programu uruchamianego na
pliku wybranym w Nautilusie.

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

rm -f $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-2.0/*.la

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
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/apps/*
%attr(755,root,root) %{_libdir}/nautilus/extensions-2.0/*.so
