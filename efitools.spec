Name:		efitools
Version:	1.9.2
Release:	4
Summary:	Tools for secure booting efi images
Group:		System
License:	GPLv2+
URL:		https://git.kernel.org/pub/scm/linux/kernel/git/jejb/efitools.git
Source0:	https://git.kernel.org/pub/scm/linux/kernel/git/jejb/efitools.git/snapshot/efitools-%{version}.tar.gz
Patch0:		fix-spelling-error.patch
Patch1:		efitools-disable-efisigned.patch
ExclusiveArch:	%{efi}
BuildRequires:	efi-srpm-macros
BuildRequires:	help2man
BuildRequires:	gnu-efi
BuildRequires:	perl-File-Slurp
BuildRequires:	binutils-devel
BuildRequires:	pkgconfig(openssl)
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
# (tpg) use our flags
sed -i -e 's/CFLAGS.*= -O2 -g/CFLAGS += /' Make.rules
sed -i -e 's/LDFLAGS/LIBS/g' Make.rules
sed -i -e 's/\$(CC)/& $(LDFLAGS)/g' Makefile

%build
%set_build_flags
%make_build -j1

%install
export BRP_PESIGN_FILES='%{_datadir}/%{name}/efi/*.efi'
%make_install DOCDIR=%{buildroot}%{_docdir}/%{name}/ CFLAGS="%{optflags}"

# Remove COPYING and README installed by "make install"
# Those two files are packaged later.
rm -f %{buildroot}/%{_datadir}/%{name}/COPYING
rm -f %{buildroot}/%{_datadir}/%{name}/README

# Remove EFI binaries
rm -rf %{buildroot}/%{_datadir}/%{name}/

# Also remove efitool-mkusb which needs self-signed EFI binaries
rm -f %{buildroot}/%{_bindir}/efitool-mkusb

%files
%doc COPYING README 
%{_bindir}/*
%doc %{_mandir}/man1/*
