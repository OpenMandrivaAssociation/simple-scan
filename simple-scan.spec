Name:           simple-scan
Version:        2.32.0.1
Release:        %mkrel 1
Summary:        Simple scanning utility

Group:          Graphical desktop/GNOME
License:        GPLv3+
URL:            https://launchpad.net/simple-scan
Source0:        http://ftp.gnome.org/pub/gnome/sources/%{name}/%{version}/simple-scan-%version.tar.bz2

BuildRequires: intltool
BuildRequires: libGConf2-devel
BuildRequires: gtk2-devel
BuildRequires: jpeg-devel
BuildRequires: libgudev-devel
BuildRequires: sane-devel
BuildRequires: gnome-doc-utils

Requires: gnome-icon-theme
Requires: xdg-utils
Requires: yelp

%description
Simple Scan is an easy-to-use application, designed to let users connect their
scanner and quickly have the image/document in an appropriate format.

%prep
%setup -q

%build

%configure2_5x --disable-schemas-install
%make

%install
rm -fr %buildroot
%makeinstall_std

%find_lang %{name} --with-man --with-gnome

%clean
rm -rf %{buildroot}

%files -f %{name}.lang 
%defattr(-,root,root,-)
%doc AUTHORS README COPYING ChangeLog
%{_mandir}/man1/%{name}.1.*
%{_sysconfdir}/gconf/schemas/%{name}.schemas
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
