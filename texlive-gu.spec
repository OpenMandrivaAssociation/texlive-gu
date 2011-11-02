Name:		texlive-gu
Version:	20080821
Release:	1
Summary:	Typeset crystallographic group-subgroup-schemes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/gu
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gu.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gu.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package simplifies typesetting of simple crystallographic
group-subgroup-schemes in the Barnighausen formalism. It
defines a new environment stammbaum, wherein all elements of
the scheme are defined. Afterwards all necessary dimensions are
calculated and the scheme is drawn. Currently two steps of
symmetry reduction are supported.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
