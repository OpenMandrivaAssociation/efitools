%global debug_package %{nil}

Summary:	Tools for secure booting efi images
Name:		efitools
Version:	1.9.2
Release:	5
Group:		System
License:	GPLv2+
URL:		https://git.kernel.org/pub/scm/linux/kernel/git/jejb/efitools.git
Source0:	https://git.kernel.org/pub/scm/linux/kernel/git/jejb/efitools.git/snapshot/efitools-%{version}.tar.gz
Patch0:		fix-spelling-error.patch
Patch1:		efitools-fix-linking.patch
ExclusiveArch:	%{efi}
BuildRequires:	efi-srpm-macros
BuildRequires:	help2man
BuildRequires:	gnu-efi
BuildRequires:	perl-File-Slurp
BuildRequires:	binutils-devel
BuildRequires:	pkgconfig(openssl)
BuildRequires:	openssl
BuildRequires:	sbsigntools
Requires:	coreutils
Requires:	mtools
Requires:	parted
Requires:	util-linux
Recommends:	sbsigntools

%description
Tools for creating and manipulating signed efi binaries
for systems with secure boot bioses

%prep
%autosetup -p1

# (tpg) fix build with LLVM/clang
sed -i -e 's/-fno-toplevel-reorder//g' Make.rules

%build
%set_build_flags
%make_build -j1

%install
%make_install DOCDIR=%{buildroot}%{_docdir}/%{name}/ CFLAGS="%{optflags}"

# Remove COPYING and README installed by "make install"
# Those two files are packaged later.
rm -f %{buildroot}/%{_datadir}/%{name}/COPYING
rm -f %{buildroot}/%{_datadir}/%{name}/README

%files
%doc COPYING README
%{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%doc %{_mandir}/man1/*
