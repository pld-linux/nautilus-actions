Summary:	Nautilus extension which adds customized command in Nautilus menu
Summary(pl):	Rozszerzenie dodaj±ce w³asne polecenia w menu Nautilusa
Name:		nautilus-actions
Version:	1.4
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	ftp://ftp2.grumz.net/grumz/%{name}-%{version}.tar.gz
# Source0-md5:	c3434900718401e13432533eab10e681
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-ldadd.patch
URL:		http://www.grumz.net/node/8/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.12.2
BuildRequires:	intltool >= 0.35
BuildRequires:	libbonobo-devel >= 2.15.2
BuildRequires:	libglade2-devel >= 1:2.6.0
BuildRequires:	libgnomeui-devel >= 2.15.91
BuildRequires:	libtool
BuildRequires:	libuuid-devel
BuildRequires:	libxml2-devel >= 1:2.6.26
BuildRequires:	nautilus-devel >= 2.15.92
BuildRequires:	rpmbuild(macros) >= 1.311
Requires:	hicolor-icon-theme
Requires:	nautilus >= 2.15.92
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nautilus extension which allow to configure program to be launch on
files selected into Nautilus interface.

%description -l pl
Rozszerzenie pozwalaj±ce na skonfigurowanie programu uruchamianego na
pliku wybranym w Nautilusie.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-schemas-install \
	--enable-commandline-tool

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-1.0/*.la

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
%{_desktopdir}/*
%{_iconsdir}/hicolor/*/apps/*
%attr(755,root,root) %{_libdir}/nautilus/extensions-1.0/*.so
