Name:           alsa-ucm-conf-nabu
Version:        1.2.9
Release:        0
Summary:        ALSA UCM Profiles for Xiaomi Nabu
License:        BSD-3-Clause
URL:            https://www.alsa-project.org
Source:         %{name}-%{version}.tar.bz2
BuildArch:      noarch
Requires:       alsa-lib >= 1.2.8

%description
This package contains the profiles files for ALSA UCM (Use Case Manager).

%prep
%autosetup -p1
find . -name ".gitignore" -delete

%build

%install
mkdir -p %{buildroot}%{_datadir}/alsa
cp -a alsa-ucm-conf/* %{buildroot}%{_datadir}/alsa/ucm2/

%files
%{_datadir}/alsa

%changelog
