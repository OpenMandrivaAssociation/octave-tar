%global octpkg octave_tar

Summary:	The octave_tar package provides functions for pack and unpack about tar format
Name:		octave-tar
Version:	1.0.1
Release:	1
License:	GPLv3+
Group:		Sciences/Mathematics
#Url:		https://packages.octave.org/octave_tar/
Url:		https://github.com/CNOCTAVE/octave_tar
Source0:	https://github.com/CNOCTAVE/octave_tar/releases/download/%{version}/octave_tar.tar.gz

BuildRequires:  octave-devel >= 8.0.0

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

BuildArch:	noarch

%description
The octave_tar package provides functions for pack and unpack about 
tar format.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}

%build
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

