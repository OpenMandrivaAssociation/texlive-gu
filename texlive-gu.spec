# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/gu
# catalog-date 2008-08-21 09:38:31 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-gu
Version:	20080821
Release:	6
Summary:	Typeset crystallographic group-subgroup-schemes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/gu
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gu.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gu.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20080821-2
+ Revision: 752452
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20080821-1
+ Revision: 718590
- texlive-gu
- texlive-gu
- texlive-gu
- texlive-gu

