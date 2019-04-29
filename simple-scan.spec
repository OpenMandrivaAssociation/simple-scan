%define _disable_rebuild_configure 1
%define url_ver %(echo %{version}|cut -d. -f1,2)

Name:		simple-scan
Version:	3.32.2
Release:	1
Summary:	Simple scanning utility
Group:		Graphical desktop/GNOME
License:	GPLv3+
URL:		https://launchpad.net/simple-scan
Source0:	hhttp://ftp.acc.umu.se/pub/GNOME/sources/simple-scan/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires: intltool
BuildRequires: jpeg-devel
BuildRequires: sane-devel
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(colord)
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(gmodule-export-2.0)
BuildRequires: pkgconfig(gnome-doc-utils)
BuildRequires: pkgconfig(gthread-2.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(gudev-1.0)
BuildRequires: pkgconfig(packagekit-glib2)
BuildRequires: pkgconfig(zlib)
BuildRequires: itstool
BuildRequires:	vala
BuildRequires:		pkgconfig(libjpeg)
BuildRequires:		pkgconfig(sane-backends)
BuildRequires:		meson
BuildRequires:		libxml2-utils

Requires: adwaita-icon-theme
Requires: xdg-utils
Requires: yelp

%description
Simple Scan is an easy-to-use application, designed to let users connect their
scanner and quickly have the image/document in an appropriate format.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name} --with-man --with-gnome

%files -f %{name}.lang 
%doc COPYING NEWS README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.SimpleScan.gschema.xml
#{_datadir}/%{name}
%{_mandir}/man1/%{name}.1.*
%{_datadir}/metainfo/%{name}.appdata.xml
%{_iconsdir}/hicolor/*/apps/org.gnome.SimpleScan*.svg

