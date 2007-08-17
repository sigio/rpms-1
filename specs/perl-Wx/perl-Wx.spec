# $Id$
# Authority: dag
# Upstream: Mattia Barbon <mbarbon@cpan.org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Wx

Summary: Perl module to interface to the wxWidgets cross-platform GUI toolkit
Name: perl-Wx
Version: 0.75
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Wx/

Source: http://www.cpan.org/modules/by-module/Wx/Wx-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(Alien::wxWidgets) >= 0.25
BuildRequires: perl(Data::Dumper)
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.17
BuildRequires: perl(File::Spec::Functions) >= 0.82
BuildRequires: perl(Test::Harness) >= 2.26
BuildRequires: perl(Test::More) >= 0.45

%description
perl-Wx is a Perl module to interface to the wxWidgets cross-platform GUI toolkit.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find docs/ samples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST MANIFEST.SKIP META.yml README.txt docs/ samples/
%doc %{_mandir}/man1/wx_xspp.pl.1*
%doc %{_mandir}/man3/*.3pm*
%{_bindir}/wx_overload.pl
%{_bindir}/wx_xspp.pl
%{perl_vendorarch}/Wx.pm
%{perl_vendorarch}/Wx/
%{perl_vendorarch}/auto/Wx/

%changelog
* Sun Aug 12 2007 Dag Wieers <dag@wieers.com> - 0.75-1
- Updated to release 0.75.

* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 0.74-1
- Initial package. (using DAR)
