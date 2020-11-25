Name:           efitools
Version:        1.9.2
Release:        2
Summary:        Tools for secure booting efi images
Group:          System
License:        GPLv2+
URL:            https://git.kernel.org/pub/scm/linux/kernel/git/jejb/efitools.git
Source0:        https://git.kernel.org/pub/scm/linux/kernel/git/jejb/efitools.git/snapshot/efitools-%{version}.tar.gz
Patch0:         fix-spelling-error.patch

BuildRequires:	help2man
BuildRequires:	gnu-efi
BuildRequires:	perl-File-Slurp
BuildRequires:	binutils-devel
BuildRequires:	pkgconfig(openssl)
BuildRequires:	sbsigntools

%description	
Tools for creating and manipulating signed efi binaries 
for systems with secure boot bioses

%prep
%autosetup -p1

%build
%make_build CC=gcc LD=/usr/bin/ld.bfd
 
%install
%make_install

%files
%doc COPYING README 
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/efitools/COPYING
%{_datadir}/efitools/README
%{_datadir}/efitools/efi/HashTool.efi
%{_datadir}/efitools/efi/HelloWorld.efi
%{_datadir}/efitools/efi/KeyTool.efi
%{_datadir}/efitools/efi/Loader.efi
%{_datadir}/efitools/efi/LockDown.efi
%{_datadir}/efitools/efi/ReadVars.efi
%{_datadir}/efitools/efi/SetNull.efi
%{_datadir}/efitools/efi/ShimReplace.efi
%{_datadir}/efitools/efi/UpdateVars.efi
