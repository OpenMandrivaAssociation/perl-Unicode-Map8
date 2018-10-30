%define modname	Unicode-Map8
%define modver	0.13

Summary:	Mapping table between 8-bit chars and Unicode
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	20
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://search.cpan.org/CPAN/authors/id/G/GA/GAAS/%{modname}-%{modver}.tar.gz
BuildRequires:	perl-devel
# (tv) for test suite:
BuildRequires:	perl-Unicode-String

%description
The Unicode::Map8 class implement efficient mapping tables between 8-bit
character sets and 16 bit character sets like Unicode. The tables are efficient
both in terms of space allocated and translation speed. The 16-bit strings is
assumed to use network byte order.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# (tv) test suite failed in iurt but success with iurt --shell :-(
#make test

%install
%makeinstall_std

%files 
%doc README Changes
%{_bindir}/*
%{perl_vendorarch}/auto/Unicode
%{perl_vendorarch}/Unicode
%{_mandir}/man1/*
%{_mandir}/man3/*

