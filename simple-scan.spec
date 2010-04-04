Name:           simple-scan
Version:        0.9.9 
Release:        %mkrel 1
Summary:        Simple scanning utility

Group:          Graphical desktop/GNOME
License:        GPLv3+
URL:            https://launchpad.net/simple-scan
Source0:        http://launchpad.net/simple-scan/trunk/%version/+download/simple-scan-%version.tar.gz

BuildRequires: intltool
BuildRequires: libGConf2-devel
BuildRequires: gtk2-devel
BuildRequires: libgudev-devel
BuildRequires: sane-devel
BuildRequires: gnome-doc-utils 

Requires: gnome-icon-theme
Requires: xdg-utils
Requires: yelp
Requires(pre): GConf2
Requires(post): GConf2
Requires(preun): GConf2

%description
Simple Scan is an easy-to-use application, designed to let users connect their
scanner and quickly have the image/document in an appropriate format.

%prep
%setup -q 

%build

%configure2_5x --disable-schemas-install
%make

%install
%makeinstall

desktop-file-install					\
	--remove-category Application			\
	--dir %{buildroot}%{_datadir}/applications	\
	--mode 0644					\
	%{buildroot}%{_datadir}/applications/%{name}.desktop

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
%{_datadir}/%{name}/

