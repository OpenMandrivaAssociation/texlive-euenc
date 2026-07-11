%global tl_name euenc
%global tl_revision 19795

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1h
Release:	%{tl_revision}.1
Summary:	Unicode font encoding definitions for XeTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/euenc
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/euenc.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/euenc.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/euenc.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Font encoding definitions for unicode fonts loaded by LaTeX in XeTeX or
LuaTeX. The package provides two encodings: EU1, designed for use with
XeTeX, which the fontspec uses for unicode fonts which require no macro-
level processing for accents, and EU2, which provides the same
facilities for use with LuaTeX. Neither encoding places any restriction
on the glyphs provided by a font; use of EU2 causes the package
euxunicode to be loaded (the package is part of this distribution). The
package includes font definition files for use with the Latin Modern
OpenType fonts.

