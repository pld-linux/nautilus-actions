Summary:	Nautilus extension which adds customized command in Nautilus menu
Summary(pl):	Rozszerzenie dodaj±ce w³asne polecenia w menu Nautilusa
Name:		nautilus-actions
Version:	0.7
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	ftp://ftp2.grumz.net/grumz/%{name}-%{version}.tar.gz
# Source0-md5:	78caa4f0546d33d381c6f41090b64db1
Patch0:		%{name}-desktop.patch
URL:		http://www.grumz.net/?q=taxonomy/term/2/9
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.8.1
BuildRequires:	intltool
BuildRequires:	libbonobo-devel >= 2.10.0
BuildRequires:	libgnomeui-devel >= 2.12.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	nautilus-devel >= 2.12.0
Requires:	nautilus >= 2.12.0
Requires:	python-libxml2
Requires:	python-pygtk-glade >= 2.8.0
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

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-1.0/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*
%attr(755,root,root) %{_libdir}/nautilus/extensions-1.0/*.so
