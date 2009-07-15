Name:		qtwitter
Version:	0.8.1
Release:	1%{?dist}
Summary:	A Qt-based client for Twitter and Identi.ca

Group:		Applications/Internet
License:	LGPL
URL:		http://qtwitter.ayoy.net
Source0:	http://files.ayoy.net/qtwitter/release/%{version}/src/%{name}-%{version}-src.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	qt-devel qoauth-devel
Requires:	qt-x11 qoauth

%description
qTwitter is an application interacting with Twitter and Identi.ca social
networks.

%prep
%setup -q
sed -i "s!\$\${INSTALL_PREFIX}\/lib!%{_libdir}!" \
    twitterapi/twitterapi.pro urlshortener/urlshortener.pro
sed -i -e '/doc \\/d' -e '/-Wl,-rpath,\$\${TOP}/d' qtwitter-app/qtwitter-app.pro

%build
qmake-qt4 PREFIX="/usr"
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install INSTALL_ROOT=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc README CHANGELOG LICENSE
%{_bindir}/*
%{_libdir}/lib*
%{_includedir}/*
%{_datadir}/*


%changelog
* Thu Jul 16 2009 Dominik Kapusta <d at, ayoy.net> 0.8.1
- New upstream version
* Mon Jul 13 2009 Dominik Kapusta <d at, ayoy.net> 0.8.0
- New upstream version
* Sat Jun 06 2009 Dominik Kapusta <d at, ayoy.net> 0.7.0
- Initial Fedora package
