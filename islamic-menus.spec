Name:           islamic-menus
Version:        1.0.3
Release:        1%{?dist}
Summary:        Islamic menus for desktops confirming with xdg standards
Group:          User Interface/Desktops
License:        GPLv2+
URL:            https://www.redhat.com/archives/fedora-games-list/2007-March/msg00003.html
# No URL as we are upstream
Source0:        %{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
Requires:       redhat-menus hicolor-icon-theme

%description
Catagorize islamic apps in a menu for the GNOME, KDE and other xdg-confirming desktops

%prep
%setup -q

%build
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT


%post
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
   %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%postun
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
   %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi


%files
%defattr(-,root,root,-)
%doc COPYING
%config(noreplace) %{_sysconfdir}/xdg/menus/applications-merged/islamic.menu
%{_datadir}/desktop-directories/*.directory
%{_datadir}/icons/hicolor/scalable/categories/*.svg

%changelog
* Wed Jun 2 2010 Muayyad Saleh Alsadi <alsadi@ojuba.org> 1.0.3-1
- Initial release

