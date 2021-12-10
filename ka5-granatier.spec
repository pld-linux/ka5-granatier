%define		kdeappsver	21.12.0
%define		kframever	5.56.0
%define		qtver		5.9.0
%define		kaname		granatier
Summary:	Granatier
Name:		ka5-%{kaname}
Version:	21.12.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	http://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	5ccedf603534dd8f1a655c7e19fa8019
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Qml-devel >= 5.11.1
BuildRequires:	Qt5Quick-devel >= 5.11.1
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	ka5-libkdegames-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf5-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf5-kcrash-devel >= %{kframever}
BuildRequires:	kf5-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-knewstuff-devel >= %{kframever}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Granatier is a clone of the classic Bomberman game, inspired by the
work of the Clanbomber clone.

%description -l pl.UTF-8
Granatier jest klonem klasycznej gry Bomberman, inspirowanym
przez działanie klona Clanbombera.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
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
%{_datadir}/metainfo/org.kde.granatier.appdata.xml
%{_datadir}/qlogging-categories5/granatier.categories
