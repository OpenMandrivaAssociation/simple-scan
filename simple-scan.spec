Name:		simple-scan
Version:	3.4.2
Release:	1
Summary:	Simple scanning utility
Group:		Graphical desktop/GNOME
License:	GPLv3+
URL:		https://launchpad.net/simple-scan
Source0:	https://launchpad.net/simple-scan/3.4/%{version}/+download/%{name}-%{version}.tar.gz

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
BuildRequires: pkgconfig(mx-1.0)
BuildRequires: pkgconfig(zlib)
BuildRequires: itstool

Requires: gnome-icon-theme
Requires: xdg-utils
Requires: yelp

%description
Simple Scan is an easy-to-use application, designed to let users connect their
scanner and quickly have the image/document in an appropriate format.

%prep
%setup -q

%build
%configure2_5x \
	--disable-schemas-install

%make

%install
%makeinstall_std

%find_lang %{name} --with-man --with-gnome

%files -f %{name}.lang 
%doc AUTHORS README COPYING ChangeLog
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.SimpleScan.gschema.xml
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1.*
