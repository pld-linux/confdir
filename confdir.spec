Summary:	Library implementing HOME-ETC mechanism for per-user configuration and data files.
Summary(pl):	Biblioteka implementuj�ca mechanizm HOME-ETC do indywidualnych plik�w konfiguracyjnych i plik�w z zasobami.
Name:		confdir
Version:	0.0.1
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://snsinfo.ifpan.edu.pl/~roman/confdir/confdir-%{version}.tar.gz
BuildRequires:	libtool
BuildRoot:      %{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Confdir is a library implementing HOME-ETC mechanism for per-user configuration
and data files, as described by Pawe� Wilk in
cvs://cvs.pld.org.pl/PLD-doc/home-etc/HOME-ETC.txt. Confdir was inspired by his userdir library, but has additional features.

%description -l pl
Confdir jest bibliotek� implementuj�c� mechanizm HOME-ETC do indywidualnych plik�w konfiguracyjnych i plik�w z zasobami, tak jak zosta� on opisany przez Paw�a Wilka w dokumencie cvs://cvs.pld.org.pl/PLD-doc/home-etc/HOME-ETC.txt. Confdir by�a inspirowana jego bibliotek� userdir, ale ma dodatkowe mo�liwo�ci.

%package devel
Summary:	Header files for confdir library
Summary(pl):	Pliki nag��wkowe biblioteki confdir
Group:		Development/Libraries
Requires:	confdir = %{version}

%description devel
Header files for confdir library.

%description devel -l pl
Pliki nag��wkowe biblioteki confdir.

%package static
Summary:	Static confdir library
Summary(pl):	Biblioteka statyczna confdir
Group:		Development/Libraries
Requires:	confdir = %{version}

%description static
Static confdir library.

%description static -l pl
Biblioteka statyczna confdir.

%package examples
Summary:	Demonstration programs using confdir library
Summary(pl):	Przyk�adowe programy u�ywaj�ce biblioteki confdir
Group:		Development/Libraries

%description examples
Demonstration programs using confdir library.

%description examples -l pl
Przyk�adowe programy u�ywaj�ce biblioteki confdir.

%prep
%setup -q

%build
aclocal
autoconf
automake -a
%configure
%{__make}

gzip doc/* README AUTHORS

%install

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install examples/*.c $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so.*.*
%doc *.gz

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%attr(755,root,root) %{_libdir}/*.la
%{_includedir}/*
%doc doc/*.gz

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
