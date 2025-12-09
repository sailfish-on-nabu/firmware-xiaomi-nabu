Name:           firmware-xiaomi-nabu
Version:        0.1
Release:        0
Summary:        firmware for Xiaomi Nabu
License:        BSD-3-Clause
URL:            https://github.com/sailfish-on-nabu
Source:         %{name}-%{version}.tar.bz2
BuildArch:      noarch

%description
This package contains the firmware files for Xiaomi Nabu

%prep
%autosetup -p1
find . -name ".gitignore" -delete

%build

%install
mkdir -p %{buildroot}%{_datadir}/alsa
cp -R firmware/* %{buildroot}/usr/lib/

%files
/usr/lib/firmware

%changelog
