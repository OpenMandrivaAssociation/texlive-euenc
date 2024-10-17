Name:		texlive-euenc
Version:	19795
Release:	2
Summary:	Unicode font encoding definitions for XeTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/euenc
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/euenc.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/euenc.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/euenc.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
