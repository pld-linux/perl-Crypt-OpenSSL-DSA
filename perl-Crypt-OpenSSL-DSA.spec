#
# Conditional build:
%bcond_without	tests	# Do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	OpenSSL-DSA
Summary:	Crypt::OpenSSL::DSA - Digital Signature Algorithm using OpenSSL
Summary(pl):	Crypt::OpenSSL::DSA - algorytm DSA u¿ywaj±cy OpenSSL
Name:		perl-Crypt-OpenSSL-DSA
Version:	0.11
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	87db60686b76ee4633f4ec6bf0b666b1
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt::OpenSSL::DSA implements the DSA (Digital Signature Algorithm)
signature verification system.

%description -l pl
Modu³ Crypt::OpenSSL::DSA jest implementacj± systemu weryfikacji
podpisów DSA (Digital Signature Algorithm).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

##### were disabled - some of tests fail randomly ?
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Crypt/OpenSSL/DSA.pm
%dir %{perl_vendorarch}/auto/Crypt/OpenSSL/DSA
%{perl_vendorarch}/auto/Crypt/OpenSSL/DSA/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Crypt/OpenSSL/DSA/*.so
%{_mandir}/man3/*
