%bcond_with bootstrap
%global packname  rpanel
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.0_6
Release:          3
Summary:          Simple Interactive Controls for R Using the tcltk Package
Group:            Sciences/Mathematics
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-6.tar.gz
Requires:         R-tcltk R-tkrplot R-rgl R-sp R-geoR R-RandomFields
%if %{without bootstrap}
Requires:         R-sm
%endif
BuildRequires:    R-devel Rmath-devel texlive-collection-latex
BuildRequires:    R-tcltk R-tkrplot R-rgl R-sp R-geoR R-RandomFields
%if %{with bootstrap}
BuildRequires:    R-sm
%endif

%description
rpanel provides a set of functions to build simple GUI controls for R
functions.  These are built on the tcltk package. Uses could include
changing a parameter on a graph by animating it with a slider or a
"doublebutton", up to more sophisticated control panels.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%if %{without bootstrap}
%check
%{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/history.txt
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/COPYING
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/images
