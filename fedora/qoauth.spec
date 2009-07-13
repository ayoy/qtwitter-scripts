Name:		qoauth
Version:	0.1.0
Release:	1%{?dist}
Summary:	A Qt OAuth support library

Group:		Applications/Internet
License:	LGPL
URL:		http://github.com/ayoy/qoauth
Source0:	http://files.ayoy.net/qoauth/release/%{version}/src/%{name}-%{version}-src.tar.bz2
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	qca2-devel
Requires:	qca-ossl

%description
QOAuth is a library providing support for OAuth authorization scheme for C++
applications.

%package	devel
Summary:	Development files for the Qt OAuth support library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description	devel
This package contains headers required to build applications using QOAuth
library.

%prep
%setup -q
sed -i -e '/^ *docs \\$/d' \
       -e "s!\(\$\${INSTALL_PREFIX}\)/lib!%{_libdir}!" qoauth.pro

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
%{_libdir}/lib%{name}*.so.*

%files devel
%defattr(-,root,root,-)
%doc doc/html
%{_libdir}/lib%{name}*.so
%{_libdir}/lib%{name}.prl
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/qt4/mkspecs/features/oauth.prf
%{_includedir}/*

%changelog
* Mon Jul 13 2009 Dominik Kapusta <d at, ayoy.net> 0.1.0
- Initial Fedora package
