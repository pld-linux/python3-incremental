# TODO: apidocs (BR: pydoctor), tests (BR: twisted.trial >= 16.4.0)
#
# Conditional build:
%bcond_with	doc	# API documentation (pydoctor based)
%bcond_with	tests	# unit tests (require Twisted)

Summary:	Library that versions Python projects
Summary(pl.UTF-8):	Biblioteka wersjonująca projekty w Pythonie
Name:		python3-incremental
Version:	24.11.0
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/incremental/
Source0:	https://files.pythonhosted.org/packages/source/i/incremental/incremental-%{version}.tar.gz
# Source0-md5:	5d7524d053b182d713981ea20079ed76
URL:		https://pypi.org/project/incremental/
BuildRequires:	python3-build
BuildRequires:	python3-hatchling >= 1.6.0
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.8
%if %{with tests}
BuildRequires:	python3-twisted >= 16.4.0
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
%if %{with doc}
BuildRequires:	pydoctor
%endif
Requires:	python3-modules >= 1:3.8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Incremental is a small library that versions your Python projects.

%description -l pl.UTF-8
Incremental to mała biblioteka do wersjonowania projektów w Pythonie.

%package apidocs
Summary:	API documentation for Python incremental module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona incremental
Group:		Documentation

%description apidocs
API documentation for Python incremental module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona incremental.

%prep
%setup -q -n incremental-%{version}

%build
%py3_build_pyproject

%if %{with tests}
PYTHONPATH=$(pwd)/src \
trial-3 incremental
%endif

%if %{with doc}
pydoctor -q --project-name incremental src/incremental
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files -n python3-incremental
%defattr(644,root,root,755)
%doc LICENSE NEWS.rst README.rst
%attr(755,root,root) %{_bindir}/incremental
%{py3_sitescriptdir}/incremental
%{py3_sitescriptdir}/incremental-%{version}.dist-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc # TODO
%endif
