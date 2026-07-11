%global tl_name gu
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Typeset crystallographic group-subgroup-schemes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/gu
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gu.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gu.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package simplifies typesetting of simple crystallographic group-
subgroup-schemes in the Barnighausen formalism. It defines a new
environment stammbaum, wherein all elements of the scheme are defined.
Afterwards all necessary dimensions are calculated and the scheme is
drawn. Currently two steps of symmetry reduction are supported.

