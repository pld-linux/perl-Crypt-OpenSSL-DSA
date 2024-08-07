#
# Conditional build:
%bcond_without	tests	# Do not perform "make test"
#
%define		pdir	Crypt
%define		pnam	OpenSSL-DSA
Summary:	Crypt::OpenSSL::DSA - Digital Signature Algorithm using OpenSSL
Summary(pl.UTF-8):	Crypt::OpenSSL::DSA - algorytm DSA używający OpenSSL
Name:		perl-Crypt-OpenSSL-DSA
Version:	0.20
Release:	6
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Crypt/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8f11ba8db9dfbfff37a5df677af02538
URL:		https://metacpan.org/dist/Crypt-OpenSSL-DSA
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	openssl-tools
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
BuildRequires:	which
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt::OpenSSL::DSA implements the DSA (Digital Signature Algorithm)
signature verification system.

%description -l pl.UTF-8
Moduł Crypt::OpenSSL::DSA jest implementacją systemu weryfikacji
podpisów DSA (Digital Signature Algorithm).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/Crypt/OpenSSL/DSA/Signature.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Crypt/OpenSSL/DSA.pm
%dir %{perl_vendorarch}/auto/Crypt/OpenSSL/DSA
%attr(755,root,root) %{perl_vendorarch}/auto/Crypt/OpenSSL/DSA/DSA.so
%{_mandir}/man3/Crypt::OpenSSL::DSA*.3pm*
