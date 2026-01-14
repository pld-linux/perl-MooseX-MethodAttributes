#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	MooseX
%define	pnam	MethodAttributes
Summary:	code attribute introspection
Summary(pl.UTF-8):	analiza kodu atrybutów
Name:		perl-MooseX-MethodAttributes
Version:	0.26
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/MooseX/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	556fa58ae5b0cd2e150cc9075efc7460
URL:		http://search.cpan.org/dist/MooseX-MethodAttributes/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(MooseX::Types) >= 0.21
BuildRequires:	perl-Moose >= 0.99
BuildRequires:	perl-Test-Exception
BuildRequires:	perl-namespace-autoclean
BuildRequires:	perl-namespace-clean => 0.10
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
