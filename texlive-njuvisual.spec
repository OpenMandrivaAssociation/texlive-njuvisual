Name:		texlive-njuvisual
Version:	65261
Release:	1
Summary:	Display logos related to Nanjing University
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/njuvisual
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/njuvisual.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/njuvisual.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/njuvisual.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The njuvisual package collects standard colors and logos
related to Nanjing University, saves the vector logos as TikZ
pictures and provides a user-friendly interface to display them
in documents and beamers.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/njuvisual
%{_texmfdistdir}/tex/latex/njuvisual
%doc %{_texmfdistdir}/doc/latex/njuvisual

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
