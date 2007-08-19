%define module	Unicode-Map8
%define name	perl-%{module}
%define version 0.12
%define release %mkrel 8

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Mapping table between 8-bit chars and Unicode
License:	GPL or Artistic
Group:		Development/Perl
Source:		http://search.cpan.org/CPAN/authors/id/G/GA/GAAS/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
Buildrequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
The Unicode::Map8 class implement efficient mapping tables between 8-bit
character sets and 16 bit character sets like Unicode. The tables are efficient
both in terms of space allocated and translation speed. The 16-bit strings is
assumed to use network byte order.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

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
