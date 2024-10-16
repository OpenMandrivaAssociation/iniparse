%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           python-iniparse
Version:        0.4
Release:        %mkrel 1
Summary:        Python Module for Accessing and Modifying Configuration Data in INI files
Group:          Development/Python
License:        MIT
URL:            https://code.google.com/p/iniparse/
Source0:        http://iniparse.googlecode.com/files/iniparse-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: python-setuptools

BuildArch: noarch

%description
iniparse is an INI parser for Python which is API compatible
with the standard library's ConfigParser, preserves structure of INI
files (order of sections & options, indentation, comments, and blank
lines are preserved when data is updated), and is more convenient to
use.

%prep
%setup -q -n iniparse-%{version}


%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
# fixes
chmod 644 $RPM_BUILD_ROOT//usr/share/doc/iniparse-%{version}/index.html
mv $RPM_BUILD_ROOT/usr/share/doc/iniparse-%{version} $RPM_BUILD_ROOT/usr/share/doc/python-iniparse-%{version}

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc  %{_docdir}/python-iniparse-%{version}/*
%{python_sitelib}/iniparse
%{python_sitelib}/iniparse-%{version}-py*.egg-info



%changelog
