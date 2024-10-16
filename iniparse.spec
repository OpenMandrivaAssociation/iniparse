Name:		iniparse
Version:	0.4
Release:	%mkrel 1
Summary:	Better INI parser for Python
License:	MIT
Group:		Development/Python
URL:		https://vicking.narod.ru/flowchart/
Source:		%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-build

%description
Better INI parser for Python

%prep
%setup -q

%build
qmake
%make

%install
rm -rf %{buildroot}
%__install -Dm0644 %{name} %{buildroot}/%{bindir}/%{name}
#install *.so

%files

%clean
rm -rf %{buildroot}