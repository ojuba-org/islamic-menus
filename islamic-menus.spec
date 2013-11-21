%global owner ojuba-org
%global commit FIXME:THIS_VALUE_IS_VARIABLE_MUST_FIXED_BEFORE_PACKAGING

Name:			islamic-menus
Version:		1.0.6
Release:		1%{?dist}
Summary:		Islamic menus for desktops conforming with XDG standards
Group:			User Interface/Desktops
License:		GPLv3+
URL:			https://github.com/ojuba-org/islamic-menus
Source0:		https://github.com/%{owner}/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz
BuildArch:		noarch
Requires:		redhat-menus hicolor-icon-theme
BuildRequires:	intltool

%description
Categorize islamic apps in a menu for the GNOME, KDE and other
XDG-conforming desktops.

%prep
%setup -q -n %{name}-%{commit}

%build
make %{?_smp_mflags}

%install
%makeinstall

%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files
%doc COPYING
%config(noreplace) %{_sysconfdir}/xdg/menus/applications-merged/islamic.menu
%{_datadir}/desktop-directories/*.directory
%{_datadir}/icons/hicolor/scalable/categories/*.svg

%changelog
* Thu Nov 21 2013 Mosaab Alzoubi <moceap@hotmail.com> - 1.0.6-1
- Remove line about applications-gnome-merged due to GNOME_BZ #688972

* Sun Nov 17 2013 Mosaab Alzoubi <moceap@hotmail.com> - 1.0.5-6
- Remove un-necessary lines about buildroot.
- Use Fedora icon cache rules.
- Update source line to github directly.

* Fri Oct 18 2013 Mosaab Alzoubi <moceap@hotmail.com> - 1.0.5-5
- To zero warnings by rpmlint.

* Sat Oct 12 2013 Mosaab Alzoubi <moceap@hotmail.com> - 1.0.5-4
- Fix spec name.

* Tue Oct 8 2013 Mosaab Alzoubi <moceap@hotmail.com> - 1.0.5-3
- Hosted at Ojuba project.

* Mon Oct 7 2013 Mosaab Alzoubi <moceap@hotmail.com> - 1.0.5-2
- Update sources and URL.

* Wed Jun 2 2010 Muayyad Saleh Alsadi <alsadi@ojuba.org> - 1.0.3-1
- Initial release.
