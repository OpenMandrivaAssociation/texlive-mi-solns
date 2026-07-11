%global tl_name mi-solns
%global tl_revision 49651

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.6
Release:	%{tl_revision}.1
Summary:	Extract solutions from exercises and quizzes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mi-solns
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mi-solns.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mi-solns.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mi-solns.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package is designed to mark a solution environment of an exercise
or quiz and insert it into the same or a different document. Solutions
are ones created by either the exerquiz or eqexam package. All PDF
creators are supported.

