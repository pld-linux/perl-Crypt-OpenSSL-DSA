%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	OpenSSL-DSA
Summary:	Crypt::OpenSSL::DSA - Digital Signature Algorithm using OpenSSL
Name:		perl-Crypt-OpenSSL-DSA
Version:	0.03
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	openssl-devel
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt::OpenSSL::DSA implements the DSA (Digital Signature Algorithm)
signature verification system.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitearch}/Crypt/OpenSSL/DSA
%{perl_sitearch}/Crypt/OpenSSL/DSA.pm
%dir %{perl_sitearch}/auto/Crypt/OpenSSL/DSA
%{perl_sitearch}/auto/Crypt/OpenSSL/DSA/*.bs
%attr(755,root,root) %{perl_sitearch}/auto/Crypt/OpenSSL/DSA/*.so
%{_mandir}/man3/*
