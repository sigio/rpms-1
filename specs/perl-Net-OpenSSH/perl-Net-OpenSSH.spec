# $Id$
# Authority: dag
# Upstream: Salvador Fandino <sfandino$yahoo,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-OpenSSH

Summary: Perl module named Net-OpenSSH
Name: perl-Net-OpenSSH
Version: 0.52
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-OpenSSH/

Source: http://search.cpan.org/CPAN/authors/id/S/SA/SALVA/Net-OpenSSH-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
Requires: openssh-clients >= 4.1
Requires: perl
Requires: perl(IO::Pty)
Requires: perl(Net::SFTP::Foreign)

%description
perl-Net-OpenSSH is a Perl module.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README sample/
%doc %{_mandir}/man3/Net::OpenSSH.3pm*
%doc %{_mandir}/man3/Net::OpenSSH::*.3pm*
%dir %{perl_vendorlib}/Net/
%{perl_vendorlib}/Net/OpenSSH/
%{perl_vendorlib}/Net/OpenSSH.pm

%changelog
* Wed Aug 17 2011 Steve Huff <shuff@vecna.org> - 0.52-1
- Update to version 0.52.

* Tue Jun 22 2010 Dag Wieers <dag@wieers.com> - 0.36-1
- Initial package. (using DAR)
