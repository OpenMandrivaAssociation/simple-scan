Name:		simple-scan
Version:	3.4.2
Release:	8
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


%changelog
* Tue Jul 17 2012 Alexander Khrukin <akhrukin@mandriva.org> 3.4.2-1
+ Revision: 810037
- version update 3.4.2

* Thu Mar 15 2012 Matthew Dawkins <mattydaw@mandriva.org> 3.2.1-1
+ Revision: 785064
- new version 3.2.1
- cleaned up spec

* Mon May 23 2011 Funda Wang <fwang@mandriva.org> 2.32.0.2-2
+ Revision: 677834
- rebuild to add gconftool as req

* Thu Apr 21 2011 Funda Wang <fwang@mandriva.org> 2.32.0.2-1
+ Revision: 656421
- new version 2.32.0.2

* Fri Apr 01 2011 Funda Wang <fwang@mandriva.org> 2.32.0.1-1
+ Revision: 649615
- BR jepg
- new version 2.32.0.1

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-2mdv2011.0
+ Revision: 614890
- the mass rebuild of 2010.1 packages

* Sun Apr 25 2010 Emmanuel Andry <eandry@mandriva.org> 1.0.3-1mdv2010.1
+ Revision: 538711
- New version 1.0.3

* Sun Apr 18 2010 Emmanuel Andry <eandry@mandriva.org> 1.0.2-1mdv2010.1
+ Revision: 536395
- New version 1.0.2

* Sun Apr 04 2010 Emmanuel Andry <eandry@mandriva.org> 0.9.9-1mdv2010.1
+ Revision: 531389
- import simple-scan

