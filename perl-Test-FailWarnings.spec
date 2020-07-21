#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Test
%define		pnam	FailWarnings
Summary:	Test::FailWarnings - Add test failures if warnings are caught
Name:		perl-Test-FailWarnings
Version:	0.008
Release:	1
License:	apache
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c03d51f550dbfd9945722ff7f4c32717
URL:		https://metacpan.org/release/Test-FailWarnings
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Capture-Tiny >= 0.12
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module hooks $SIG{__WARN__} and converts warnings to Test::More
fail() calls. It is designed to be used with done_testing, when you
don't need to know the test count in advance.

Just as with Test::NoWarnings, this does not catch warnings if other
things localize $SIG{__WARN__}, as this is designed to catch unhandled
warnings.

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
%{perl_vendorlib}/Test/FailWarnings.pm
%{_mandir}/man3/Test::FailWarnings.3*
