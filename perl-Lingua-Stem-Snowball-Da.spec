%define module	Lingua-Stem-Snowball-Da
%define name	perl-%{module}
%define version 1.01
%define release %mkrel 6

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Porters stemming algorithm for Denmark
License:	GPL or Artistic
Group:		Development/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/C/CI/CINE/%{module}-%{version}.tar.bz2
Url:            http://search.cpan.org/dist/%{module}/
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
Requires:	locales-da
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
The stem function takes a scalar as a parameter and stems the word according to
Martin Porters Danish stemming algorithm, which can be found at the Snowball
website: http://snowball.tartarus.org/.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot} 
%makeinstall_std

mv %{buildroot}%{perl_vendorlib}/Lingua/Stem/Snowball/stemmer.pl \
    %{buildroot}%{perl_vendorlib}/Lingua/Stem/Snowball/stemmer-Da.pl

%clean 
rm -rf %{buildroot} 

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Lingua
%{_mandir}/man3*/*

