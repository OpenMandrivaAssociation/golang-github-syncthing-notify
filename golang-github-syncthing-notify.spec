# https://github.com/syncthing/notify
%global goipath github.com/syncthing/notify
%global commit  116c45bb5ad48777321e4984d1320d56889b6097
%global date    20181011

%gometa

Name:           %{goname}
Summary:        File system event notification library on steroids
Version:        0
Release:        0.6%{?dist}
License:        MIT

URL:            %{gourl}
Source0:        %{gosource}

%description
%{summary}.


%package        devel
Summary:        %{summary}
BuildArch:      noarch

BuildRequires:  golang(golang.org/x/sys/unix)

%description    devel
%{summary}.

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup -p1


%install
%goinstall


%check
# The test runner currently crashes, ignore results for now.
%gochecks || :


%files devel -f devel.file-list
%license LICENSE
%doc README.md AUTHORS


%changelog
* Wed Oct 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0-0.6.20181011git116c45b
- Use forgeautosetup instead of gosetup.

* Mon Oct 15 2018 Fabio Valentini <decathorpe@gmail.com> - 0-0.5.20181011git116c45b
- Bump to commit 116c45b.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0-0.4.20180829gitb76b458
- Bump to commit b76b458.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.20180708gitcdf89c4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0-0.2.20180708gitcdf89c4
- Bump to commit cdf89c4.

* Tue May 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0-0.1.20180426gitb9ceffc
- Initial package.

