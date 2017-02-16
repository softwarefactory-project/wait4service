Name:       wait4service
Version:    0.1
Release:    1%{?dist}
Summary:    A simple hook to wait for a service

License:    ASL 2.0
URL:        https://softwarefactory-project.io/r/ProductivitySIG/wait4service
Source0:    https://pypi.python.org/packages/source/r/%{name}/%{name}-%{version}.tar.gz

BuildArch:  noarch

Requires:   nmap-ncat
Requires:   bash

%description
A simple hook system to wait for a service

%prep
%autosetup -n wait4service-%{version}

%install
install -p -D -m 0755 scripts/wait4service.sh %{buildroot}/usr/bin/wait4service

%files
/usr/bin/wait4service

%changelog
* Thu Feb 16 2017 Tristan Cacqueray - 0.1-1
- Initial package of wait4service hook
