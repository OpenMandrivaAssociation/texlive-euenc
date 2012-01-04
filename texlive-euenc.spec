# revision 19795
# category Package
# catalog-ctan /macros/latex/contrib/euenc
# catalog-date 2010-09-19 01:22:04 +0200
# catalog-license lppl1.3
# catalog-version 0.1h
Name:		texlive-euenc
Version:	0.1h
Release:	2
Summary:	Unicode font encoding definitions for XeTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/euenc
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/euenc.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/euenc.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/euenc.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Font encoding definitions for unicode fonts loaded by LaTeX in
XeTeX or LuaTeX. The package provides two encodings: -- EU1,
designed for use with XeTeX, which the fontspec uses for
unicode fonts which require no macro-level processing for
accents, and -- EU2, which provides the same facilities for use
with LuaTeX. Neither encoding places any restriction on the
glyphs provided by a font; use of EU2 causes the package
euxunicode to be loaded (the package is part of this
distribution). The package includes font definition files for
use with the Latin Modern OpenType fonts.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/euenc/eu1enc.def
%{_texmfdistdir}/tex/latex/euenc/eu1lmdh.fd
%{_texmfdistdir}/tex/latex/euenc/eu1lmr.fd
%{_texmfdistdir}/tex/latex/euenc/eu1lmss.fd
%{_texmfdistdir}/tex/latex/euenc/eu1lmssq.fd
%{_texmfdistdir}/tex/latex/euenc/eu1lmtt.fd
%{_texmfdistdir}/tex/latex/euenc/eu1lmvtt.fd
%{_texmfdistdir}/tex/latex/euenc/eu2enc.def
%{_texmfdistdir}/tex/latex/euenc/eu2lmdh.fd
%{_texmfdistdir}/tex/latex/euenc/eu2lmr.fd
%{_texmfdistdir}/tex/latex/euenc/eu2lmss.fd
%{_texmfdistdir}/tex/latex/euenc/eu2lmssq.fd
%{_texmfdistdir}/tex/latex/euenc/eu2lmtt.fd
%{_texmfdistdir}/tex/latex/euenc/eu2lmvtt.fd
%doc %{_texmfdistdir}/doc/latex/euenc/README
%doc %{_texmfdistdir}/doc/latex/euenc/euenc.pdf
%doc %{_texmfdistdir}/doc/latex/euenc/test-euxlm.ltx
#- source
%doc %{_texmfdistdir}/source/latex/euenc/Makefile
%doc %{_texmfdistdir}/source/latex/euenc/euenc.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
