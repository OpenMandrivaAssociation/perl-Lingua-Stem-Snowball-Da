%define upstream_name	 Lingua-Stem-Snowball-Da
%define upstream_version 1.01

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Porters stemming algorithm for Denmark
License:	GPL+ or Artistic
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://search.cpan.org/CPAN/authors/id/C/CI/CINE/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch
Requires:	locales-da

%description
The stem function takes a scalar as a parameter and stems the word according to
Martin Porters Danish stemming algorithm, which can be found at the Snowball
website: http://snowball.tartarus.org/.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std
mv %{buildroot}%{perl_vendorlib}/Lingua/Stem/Snowball/stemmer.pl \
    %{buildroot}%{perl_vendorlib}/Lingua/Stem/Snowball/stemmer-Da.pl

%files
%doc Changes README
%{perl_vendorlib}/Lingua
%{_mandir}/man3*/*


%changelog
* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.10.0-1mdv2010.0
+ Revision: 403391
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.01-9mdv2009.0
+ Revision: 257600
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.01-8mdv2009.0
+ Revision: 245629
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.01-6mdv2008.1
+ Revision: 136280
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.01-6mdv2008.0
+ Revision: 86522
- rebuild


* Thu Aug 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.01-5mdv2007.0
- Rebuild

* Wed Nov 30 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.01-4mdk
- spec cleanup
- fix directory ownership
- %%mkrel
- rpmbuildupdate aware
- better summary
- better description
- better url

* Fri Oct 15 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.01-3mdk
- fix deps

