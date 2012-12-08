%define upstream_name	 Unicode-Map8
%define upstream_version 0.13

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7

Summary:	Mapping table between 8-bit chars and Unicode
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/G/GA/GAAS/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
# (tv) for test suite:
BuildRequires:	perl-Unicode-String

%description
The Unicode::Map8 class implement efficient mapping tables between 8-bit
character sets and 16 bit character sets like Unicode. The tables are efficient
both in terms of space allocated and translation speed. The 16-bit strings is
assumed to use network byte order.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# (tv) test suite failed in iurt but success with iurt --shell :-(
#%make test

%install
%makeinstall_std

%files 
%doc README Changes
%{perl_vendorarch}/auto/Unicode
%{perl_vendorarch}/Unicode
%{_mandir}/*/*
%{_bindir}/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.130.0-6mdv2012.0
+ Revision: 765797
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.130.0-5
+ Revision: 764320
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.130.0-4
+ Revision: 667407
- mass rebuild

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 0.130.0-3mdv2011.0
+ Revision: 564590
- rebuild for perl 5.12.1

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.130.0-2mdv2011.0
+ Revision: 555207
- rebuild

* Tue Jan 19 2010 Jérôme Quelin <jquelin@mandriva.org> 0.130.0-1mdv2010.1
+ Revision: 493492
- update to 0.13

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.120.0-1mdv2010.0
+ Revision: 401995
- rebuild using %%perl_convert_version

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.12-11mdv2009.0
+ Revision: 224584
- rebuild

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 0.12-10mdv2008.1
+ Revision: 151402
- rebuild for perl-5.10.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Aug 22 2007 Thierry Vignaud <tv@mandriva.org> 0.12-9mdv2008.0
+ Revision: 68994
- disable the test suite since it failed in iurt but success with iurt --shell
- buildrequires perl-Unicode-String for the test suite

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - rebuild
    - rebuild


* Wed Nov 30 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.12-6mdk
- spec cleanup
- %%mkrel
- better url

* Mon Nov 15 2004 Michael Scherer <misc@mandrake.org> 0.12-5mdk
- Rebuild for new perl

* Fri Jul 23 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.12-4mdk 
- fixed summary capitalization

* Fri Jul 23 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.12-3mdk 
- rpmbuildupdate aware

* Wed Feb 25 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.12-2mdk
- fixed dir ownership (distlint)

* Tue Dec 09 2003 Guillaume Rousse <guillomovitch@mandrake.org> 0.12-1mdk
- first mdk release

