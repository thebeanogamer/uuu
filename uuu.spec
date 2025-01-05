Name:          uuu
Version:       1.5.182
Release:       %autorelease
Summary:       Freescale/NXP I.MX Chip image deploy tools
License:       BSD-3-Clause
URL:           https://github.com/nxp-imx/mfgtools

# Use their tarball instead of GitHub's as it includes the .tarball-version file cmake uses
Source:        %{url}/releases/download/%{name}_%{version}/%{name}_source-%{name}_%{version}.tar.gz

BuildRequires: cmake
BuildRequires: systemd-rpm-macros

BuildRequires: gcc-c++
BuildRequires: pkgconfig(libusb-1.0)
BuildRequires: pkgconfig(bzip2)
BuildRequires: pkgconfig(libzstd)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(tinyxml2)


%description
%{summary}.


%prep
%autosetup -p1 -n %{name}-%{name}_%{version}


%build
%cmake
%cmake_build
%_vpath_builddir/uuu/uuu -udev > 70-%{name}.rules


%install
%cmake_install
mkdir -p %{buildroot}/%{_udevrulesdir}
cp -p 70-%{name}.rules %{buildroot}/%{_udevrulesdir}/70-%{name}.rules


%check
%ctest


%post
%udev_rules_update


%files
%{_bindir}/%{name}
%{_udevrulesdir}/70-%{name}.rules


%changelog
%autochangelog
