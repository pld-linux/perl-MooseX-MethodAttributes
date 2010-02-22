#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	MooseX
%define	pnam	MethodAttributes
Summary:	code attribute introspection
Summary(pl.UTF-8):	analiza kodu atrybutów
Name:		perl-MooseX-MethodAttributes
Version:	0.20
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/CPAN/authors/id/B/BO/BOBTFISH/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	39711fc1fbd4c0091811c2e585378b0e
URL:		http://search.cpan.org/dist/MooseX-MethodAttributes/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(MooseX::Types) >= 0.20
BuildRequires:	perl-Moose >= 0.79
BuildRequires:	perl-Test-Exception
BuildRequires:	perl-namespace-autoclean
BuildRequires:	perl-namespace-clean
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module allows code attributes of methods to be introspected using
Moose meta method objects.

%description -l pl.UTF-8
Moduł ten pozwala aby kod atrybutów metod był analizowany przy użyciu
metametody obiektów Moose.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/MooseX/*.pm
%{perl_vendorlib}/MooseX/MethodAttributes
%{_mandir}/man3/*
