Name:		texlive-gu
Version:	15878
Release:	2
Summary:	Typeset crystallographic group-subgroup-schemes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/gu
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gu.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gu.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package simplifies typesetting of simple crystallographic
group-subgroup-schemes in the Barnighausen formalism. It
defines a new environment stammbaum, wherein all elements of
the scheme are defined. Afterwards all necessary dimensions are
calculated and the scheme is drawn. Currently two steps of
symmetry reduction are supported.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/gu/gu.sty
%doc %{_texmfdistdir}/doc/latex/gu/README
%doc %{_texmfdistdir}/doc/latex/gu/gudemo.tex
%doc %{_texmfdistdir}/doc/latex/gu/gudoc.pdf
%doc %{_texmfdistdir}/doc/latex/gu/gudoc.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
