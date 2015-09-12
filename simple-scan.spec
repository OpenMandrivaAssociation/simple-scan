Name:		simple-scan
Version:	3.16.1.1
Release:	3
Summary:	Simple scanning utility
Group:		Graphical desktop/GNOME
License:	GPLv3+
URL:		https://launchpad.net/simple-scan
Source0:	https://launchpad.net/simple-scan/3.15/%{version}/+download/%{name}-%{version}.tar.xz

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
BuildRequires: pkgconfig(zlib)
BuildRequires: itstool
BuildRequires:	vala

Requires: adwaita-icon-theme
Requires: xdg-utils
Requires: yelp

%description
Simple Scan is an easy-to-use application, designed to let users connect their
scanner and quickly have the image/document in an appropriate format.

%prep
%setup -q

%build
%configure

%make

%install
%makeinstall_std

%find_lang %{name} --with-man --with-gnome

%files -f %{name}.lang 
%doc COPYING NEWS README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.SimpleScan.gschema.xml
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1.*
%{_datadir}/appdata/simple-scan.appdata.xml

