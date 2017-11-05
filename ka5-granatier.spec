%define		kdeappsver	17.08.2
%define		qtver		5.3.2
%define		kaname		granatier
Summary:	Granatier
Name:		ka5-%{kaname}
Version:	17.08.2
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	0360f5728c9c3cb3ff1f0a27823d0869
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-extra-cmake-modules >= 1.4.0
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Granatier.

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
