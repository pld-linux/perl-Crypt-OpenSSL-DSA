#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	OpenSSL-DSA
Summary:	Crypt::OpenSSL::DSA - Digital Signature Algorithm using OpenSSL
Summary(pl):	Modu� Perla Crypt::OpenSSL::DSA - algorytm DSA u�ywaj�cy OpenSSL
Name:		perl-Crypt-OpenSSL-DSA
Version:	0.11
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	openssl-devel >= 0.9.6m
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt::OpenSSL::DSA implements the DSA (Digital Signature Algorithm)
signature verification system.

%description -l pl
Modu� Crypt::OpenSSL::DSA jest implementacj� systemu weryfikacji
podpis�w DSA (Digital Signature Algorithm).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

##### were disabled - some of tests fail randomly ?
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitearch}/Crypt/OpenSSL/DSA.pm
%dir %{perl_sitearch}/auto/Crypt/OpenSSL/DSA
%{perl_sitearch}/auto/Crypt/OpenSSL/DSA/*.bs
%attr(755,root,root) %{perl_sitearch}/auto/Crypt/OpenSSL/DSA/*.so
%{_mandir}/man3/*
