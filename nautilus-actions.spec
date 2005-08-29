Summary:	Nautilus extension which adds customized command in Nautilus menu
Summary(pl):	Rozszerzenie dodaj±ce w³asne polecenia w menu Nautilusa
Name:		nautilus-actions
Version:	0.4
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	cfc0d0e580c176870049bdfc3f894e6d
Patch0:		%{name}-desktop.patch
URL:		http://www.grumz.net/?q=taxonomy/term/2/9
BuildRequires:	glib2-devel >= 1:2.6.0
BuildRequires:	libxml2-devel
BuildRequires:	nautilus-devel >= 2.10.0
Requires:	nautilus >= 2.10.0
Requires:	python-libxml2
Requires:	python-pygtk-glade >= 2.0.0
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
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/config_newaction.xml
%dir %{_datadir}/%{name}/nact
%{_datadir}/%{name}/nact/nautilus-actions-config.glade
%attr(755,root,root)%{_datadir}/%{name}/nact/nautilus-actions-config.py
%{_datadir}/%{name}/nact/nautilus-launch-icon.png
%{_desktopdir}/*
%attr(755,root,root) %{_libdir}/nautilus/extensions-1.0/*.so
