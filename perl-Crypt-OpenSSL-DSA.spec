%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	OpenSSL-DSA
Summary:	Crypt::OpenSSL::DSA Perl module
Summary(cs):	Modul Crypt::OpenSSL::DSA pro Perl
Summary(da):	Perlmodul Crypt::OpenSSL::DSA
Summary(de):	Crypt::OpenSSL::DSA Perl Modul
Summary(es):	Módulo de Perl Crypt::OpenSSL::DSA
Summary(fr):	Module Perl Crypt::OpenSSL::DSA
Summary(it):	Modulo di Perl Crypt::OpenSSL::DSA
Summary(ja):	Crypt::OpenSSL::DSA Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Crypt::OpenSSL::DSA ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul Crypt::OpenSSL::DSA
Summary(pl):	Modu³ Perla Crypt::OpenSSL::DSA
Summary(pt):	Módulo de Perl Crypt::OpenSSL::DSA
Summary(pt_BR):	Módulo Perl Crypt::OpenSSL::DSA
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Crypt::OpenSSL::DSA
Summary(sv):	Crypt::OpenSSL::DSA Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Crypt::OpenSSL::DSA
Summary(zh_CN):	Crypt::OpenSSL::DSA Perl Ä£¿é
Name:		perl-Crypt-OpenSSL-DSA
Version:	0.03
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	openssl-devel
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt::OpenSSL::DSA perl module.

%description -l cs
Modul Crypt::OpenSSL::DSA pro Perl.

%description -l da
Perlmodul Crypt::OpenSSL::DSA.

%description -l de
Crypt::OpenSSL::DSA Perl Modul.

%description -l es
Módulo de Perl Crypt::OpenSSL::DSA.

%description -l fr
Module Perl Crypt::OpenSSL::DSA.

%description -l it
Modulo di Perl Crypt::OpenSSL::DSA.

%description -l ja
Crypt::OpenSSL::DSA Perl ¥â¥¸¥å¡¼¥ë

%description -l ko
Crypt::OpenSSL::DSA ÆÞ ¸ðÁÙ.

%description -l no
Perlmodul Crypt::OpenSSL::DSA.

%description -l pl
Modu³ perla Crypt::OpenSSL::DSA.

%description -l pt
Módulo de Perl Crypt::OpenSSL::DSA.

%description -l pt_BR
Módulo Perl Crypt::OpenSSL::DSA.

%description -l ru
íÏÄÕÌØ ÄÌÑ Perl Crypt::OpenSSL::DSA.

%description -l sv
Crypt::OpenSSL::DSA Perlmodul.

%description -l uk
íÏÄÕÌØ ÄÌÑ Perl Crypt::OpenSSL::DSA.

%description -l zh_CN
Crypt::OpenSSL::DSA Perl Ä£¿é

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

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
