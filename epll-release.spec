%define _ll_buildid .2

Name:           epll-release
Version:        2017.03
Release:        1%{?_ll_buildid}%{?dist}
Summary:        Extra Packages for Lambda Linux repository configuration

Group:          System Environment/Base
License:        GPLv2

# sets 1-9 reserved for repository definitions
Source1:        epll.repo
Source2:        epll-preview.repo

# 10-19 reserved for scripts and other program fare

# 20-29 reserved for auth and gpg keys
Source20:       RPM-GPG-KEY-lambda-epll

# 30-39 documentation
Source31:       GPL

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
Requires:       system-release >= %{version}
Conflicts:      fedora-release

%description
This package contains the Extra Packages for Lambda Linux (EPLL)
repository GPG key as well as configuration for yum and up2date.

%prep
%setup -q -c -T
cp %{SOURCE20} .
cp %{SOURCE31} ./GPL

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc

mkdir -p -m 755 $RPM_BUILD_ROOT/etc/pki/rpm-gpg
for file in RPM-GPG-KEY* ; do
        install -m 644 $file $RPM_BUILD_ROOT/etc/pki/rpm-gpg
done

# Setup repo definitions
install -d -m 755 $RPM_BUILD_ROOT/etc/yum.repos.d/
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT/etc/yum.repos.d/
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT/etc/yum.repos.d/

# Symlink to the version-specific doc dir
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/
ln -s %name-%version $RPM_BUILD_ROOT%{_docdir}/%name

%files
%defattr(-,root,root)
%doc GPL
%config(noreplace) /etc/yum.repos.d/*
%dir /etc/pki/rpm-gpg
/etc/pki/rpm-gpg/*
# release notes
%{_docdir}/%name

%changelog
* Tue Apr 11 2017 Rajiv M Ranganath <rajiv.ranganath@atihita.com>
- epll-release.spec: Update `Version:` to `2017.03`

* Mon Oct 31 2016 Rajiv M Ranganath <rajiv.ranganath@atihita.com>
- RPM-GPG-KEY-lambda-epll: Switch package signing public key

* Wed Sep 28 2016 Rajiv M Ranganath <rajiv.ranganath@atihita.com>
- epll-release.spec: Rename `_buildid` to `_ll_buildid`
- epll-release.spec: Update `Version:` to `2016.09`

* Wed Mar 16 2016 Rajiv M Ranganath <rajiv.ranganath@atihita.com> - 2016.03-1
- Update `Version:` to `2016.03`

* Tue Sep 15 2015 Rajiv M Ranganath <rajiv.ranganath@atihita.com> 2015.09-1
- Update `Version:` to `2015.09`

* Sat Mar 28 2015 Rajiv M Ranganath <rajiv.ranganath@atihita.com> 2015.03-1
- Update `Version:` to `2015.03`

* Wed Jan 07 2015 Rajiv M Ranganath <rajiv.ranganath@atihita.com> 2014.09-1
- Add repo priority

* Sat Dec 06 2014 Rajiv M Ranganath <rajiv.ranganath@atihita.com> 2014.09-1
- Add `epll-release.spec`
- Add `RPM-GPG-KEY-lambda-epll`
- Add `epll.repo` and `epll-preview.repo`
- Add GPL License
