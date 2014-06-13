Summary:	Icon handling tools of the Tango Project
Name:		icon-naming-utils
Version:	0.8.90
Release:	12
Group:		Graphical desktop/Other
License:	GPLv2+
Url:		http://tango.freedesktop.org/Standard_Icon_Naming_Specification
Source0:	http://tango.freedesktop.org/releases/%{name}-%{version}.tar.bz2
Patch0:		icon-naming-utils-0.8.7-paths.patch
Patch1:		icon-naming-utils-0.8.90-xfce.patch
Patch2:		03_gtk_apply_close_ok.patch
Patch3:		04_add_gtk_stock_directory.patch
Patch4:		icon-naming-utils-0.8.6-missinglink.patch
BuildArch:	noarch

BuildRequires:	perl-XML-Simple

%description
This utility maps the icon names used by the GNOME and KDE desktops to
the icon names proposed in the Icon Naming Specification linked above.

%prep
%setup -q
%apply_patches
autoreconf

%build
./configure \
	--prefix=%{_prefix} \
	--libdir=%{_prefix}/lib \
	--libexecdir=%{_prefix}/lib
%make

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog
%{_bindir}/icon-name-mapping
%{_datadir}/%{name}/
%{_datadir}/pkgconfig/%{name}.pc

