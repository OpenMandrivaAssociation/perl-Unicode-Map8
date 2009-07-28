%define upstream_name	 Unicode-Map8
%define upstream_version 0.12

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1

Summary:	Mapping table between 8-bit chars and Unicode
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/G/GA/GAAS/%{upstream_name}-%{upstream_version}.tar.bz2

Buildrequires:	perl-devel
# (tv) for test suite:
Buildrequires:	perl-Unicode-String
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
The Unicode::Map8 class implement efficient mapping tables between 8-bit
character sets and 16 bit character sets like Unicode. The tables are efficient
both in terms of space allocated and translation speed. The 16-bit strings is
assumed to use network byte order.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
# (tv) test suite failed in iurt but success with iurt --shell :-(
#%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc README Changes
%{perl_vendorarch}/auto/Unicode
%{perl_vendorarch}/Unicode
%{_mandir}/*/*
%{_bindir}/*
