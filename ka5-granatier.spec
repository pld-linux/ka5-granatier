%define		kdeappsver	18.12.0
%define		qtver		5.9.0
%define		kaname		granatier
Summary:	Granatier
Name:		ka5-%{kaname}
Version:	18.12.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	a46aeb08db2c6134f730a5d722ca9929
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Qml-devel >= 5.11.1
BuildRequires:	Qt5Quick-devel >= 5.11.1
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	ka5-libkdegames-devel >= 18.12.0
BuildRequires:	kf5-extra-cmake-modules >= 5.53.0
BuildRequires:	kf5-kconfig-devel >= 5.30.0
BuildRequires:	kf5-kconfigwidgets-devel >= 5.30.0
BuildRequires:	kf5-kcoreaddons-devel >= 5.30.0
BuildRequires:	kf5-kcrash-devel >= 5.30.0
BuildRequires:	kf5-kdbusaddons-devel >= 5.30.0
BuildRequires:	kf5-kdoctools-devel >= 5.30.0
BuildRequires:	kf5-ki18n-devel >= 5.30.0
BuildRequires:	kf5-knewstuff-devel >= 5.30.0
BuildRequires:	kf5-kwidgetsaddons-devel >= 5.30.0
BuildRequires:	kf5-kxmlgui-devel >= 5.30.0
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Granatier is a clone of the classic Bomberman game, inspired by the
work of the Clanbomber clone.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/granatier.categories
%attr(755,root,root) %{_bindir}/granatier
%{_desktopdir}/org.kde.granatier.desktop
%{_datadir}/config.kcfg/granatier.kcfg
%{_datadir}/granatier
%{_iconsdir}/hicolor/128x128/apps/granatier.png
%{_iconsdir}/hicolor/16x16/apps/granatier.png
%{_iconsdir}/hicolor/22x22/apps/granatier.png
%{_iconsdir}/hicolor/32x32/apps/granatier.png
%{_iconsdir}/hicolor/48x48/apps/granatier.png
%{_iconsdir}/hicolor/64x64/apps/granatier.png
%dir %{_datadir}/kxmlgui5/granatier
%{_datadir}/kxmlgui5/granatier/granatierui.rc
%{_datadir}/metainfo/org.kde.granatier.appdata.xml
