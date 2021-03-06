Name:		qtwitter
Version:	0.10.0
Release:	1%{?dist}
Summary:	A Qt-based client for Twitter and Identi.ca

Group:		Applications/Internet
License:	LGPL
URL:		http://qtwitter.ayoy.net
Source0:	http://files.ayoy.net/qtwitter/release/%{version}/src/%{name}-%{version}-src.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	qt-devel qoauth-devel >= 1.0
Requires:	qt-x11 qoauth >= 1.0

%description
qTwitter is an microblogging services client.

%prep
%setup -q
sed -i -e '/-Wl,-rpath,\$\${DESTDIR}/d' qtwitter-app/qtwitter-app.pro

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
%{_libdir}/%{name}/plugins/*
%{_datadir}/*


%changelog
* Sun Nov 01 2009 Dominik Kapusta <d at, ayoy.net> 0.10.0
- New upstream version
* Thu Oct 01 2009 Dominik Kapusta <d at, ayoy.net> 0.9.2
- New upstream version
* Wed Sep 30 2009 Dominik Kapusta <d at, ayoy.net> 0.9.1
- New upstream version
* Thu Sep 10 2009 Dominik Kapusta <d at, ayoy.net> 0.9.0
- New upstream version
* Sat Aug 08 2009 Dominik Kapusta <d at, ayoy.net> 0.8.3
- New upstream version
* Thu Jul 30 2009 Dominik Kapusta <d at, ayoy.net> 0.8.2
- New upstream version
* Thu Jul 16 2009 Dominik Kapusta <d at, ayoy.net> 0.8.1
- New upstream version
* Mon Jul 13 2009 Dominik Kapusta <d at, ayoy.net> 0.8.0
- New upstream version
* Sat Jun 06 2009 Dominik Kapusta <d at, ayoy.net> 0.7.0
- Initial Fedora package
