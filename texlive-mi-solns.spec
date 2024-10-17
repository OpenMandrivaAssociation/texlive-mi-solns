Name:		texlive-mi-solns
Version:	49651
Release:	2
Summary:	Extract solutions from exercises and quizzes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mi-solns
License:	lppl1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mi-solns.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mi-solns.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mi-solns.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package is designed to mark a solution environment of an
exercise or quiz and insert it into the same or a different
document. Solutions are ones created by either the exerquiz or
eqexam package. All PDF creators are supported.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/mi-solns
%{_texmfdistdir}/tex/latex/mi-solns
%doc %{_texmfdistdir}/doc/latex/mi-solns

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
