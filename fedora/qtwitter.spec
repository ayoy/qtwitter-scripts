Name:		qtwitter
Version:	0.7.0
Release:	1%{?dist}
Summary:	A Qt-based client for Twitter and Identi.ca

Group:		Applications/Internet
License:	LGPL
URL:		http://qtwitter.ayoy.net
Source0:	http://files.ayoy.net/qtwitter/release/current/src/%{name}-%{version}-src.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	qt-devel
Requires:	qt qt-x11

%description
qTwitter is an application interacting with Twitter and Identi.ca social
networks. Originally inspired by Twitterrific (known very well to MacOS X
users) aims to be as compact as possible, still providing outstanding
usability.

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


%files
%defattr(-,root,root,-)
%doc README CHANGELOG LICENSE
%{_bindir}/*
%{_libdir}/*
%{_includedir}/*
%{_datadir}/%{name}/*
%{_datadir}/icons/*
%{_datadir}/applications/*


%changelog
* Sat Jun 06 2009 Dominik Kapusta <d at, ayoy.net> 0.7.0
- Initial Fedora package
