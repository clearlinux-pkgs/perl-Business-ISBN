#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Business-ISBN
Version  : 3.004
Release  : 7
URL      : https://cpan.metacpan.org/authors/id/B/BD/BDFOY/Business-ISBN-3.004.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/B/BD/BDFOY/Business-ISBN-3.004.tar.gz
Summary  : 'work with International Standard Book Numbers'
Group    : Development/Tools
License  : Artistic-2.0
Requires: perl-Business-ISBN-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Business::ISBN::Data)

%description
See the tests in the t/ directory for examples until I add some more.

%package dev
Summary: dev components for the perl-Business-ISBN package.
Group: Development
Provides: perl-Business-ISBN-devel = %{version}-%{release}

%description dev
dev components for the perl-Business-ISBN package.


%package license
Summary: license components for the perl-Business-ISBN package.
Group: Default

%description license
license components for the perl-Business-ISBN package.


%prep
%setup -q -n Business-ISBN-3.004

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Business-ISBN
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Business-ISBN/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/Business/ISBN.pm
/usr/lib/perl5/vendor_perl/5.28.2/Business/ISBN10.pm
/usr/lib/perl5/vendor_perl/5.28.2/Business/ISBN13.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Business::ISBN.3
/usr/share/man/man3/Business::ISBN10.3
/usr/share/man/man3/Business::ISBN13.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Business-ISBN/LICENSE
