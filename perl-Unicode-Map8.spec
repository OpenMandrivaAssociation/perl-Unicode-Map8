%define modname	Unicode-Map8
%undefine _debugsource_packages

Summary:	Mapping table between 8-bit chars and Unicode
Name:		perl-%{modname}
Version:	0.13
Release:	23
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://search.cpan.org/CPAN/authors/id/G/GA/GAAS/%{modname}-%{version}.tar.gz
BuildRequires:	perl-devel
# (tv) for test suite:
BuildRequires:	perl-Unicode-String

%description
The Unicode::Map8 class implement efficient mapping tables between 8-bit
character sets and 16 bit character sets like Unicode. The tables are efficient
both in terms of space allocated and translation speed. The 16-bit strings is
assumed to use network byte order.

%prep
%autosetup -p1 -n %{modname}-%{version}
perl Makefile.PL INSTALLDIRS=vendor

%build
%make_build

# FIXME as of 0.13, tests are broken on aarch64
%ifnarch %{aarch64}
%check
%make_build test
%endif

%install
%make_install

%files 
%doc README Changes
%{_bindir}/*
%{perl_vendorarch}/auto/Unicode
%{perl_vendorarch}/Unicode
%{_mandir}/man1/*
%{_mandir}/man3/*
