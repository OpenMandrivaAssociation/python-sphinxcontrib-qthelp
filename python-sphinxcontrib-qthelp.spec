%define	module	sphinxcontrib-qthelp

Summary:	Qt help file support for the Sphinx documentation generator
Name:		python-%{module}
Version:	2.0.0
Release:	1
Source0:	https://github.com/sphinx-doc/%{module}/archive/%{version}.tar.gz
License:	ISC
Group:		Development/Python
Url:		https://sphinx-doc.org/
BuildArch:	noarch
BuildSystem:	python
# python2 support dropped before 6.0
Obsoletes:	python2-%{module} < %{EVRD}

%description
Qt help file support for the Sphinx documentation generator

%files
%{py_puresitedir}/sphinxcontrib*
