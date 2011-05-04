%define name icon-naming-utils
%define version 0.8.90
%define release %mkrel 5

Summary: Icon handling tools of the Tango Project
Name: %{name}
Version: %{version}
Release: %{release}
URL: http://tango.freedesktop.org/Standard_Icon_Naming_Specification
Source0: http://tango.freedesktop.org/releases/%{name}-%{version}.tar.bz2
Patch0: icon-naming-utils-0.8.7-paths.patch
Patch1: icon-naming-utils-0.8.90-xfce.patch
Patch2: 03_gtk_apply_close_ok.patch
Patch3: 04_add_gtk_stock_directory.patch
Patch4: icon-naming-utils-0.8.6-missinglink.patch

License: GPL+
Group: Graphical desktop/Other
#Url: http://tango-project.org/Tango_Icon_Library#Download
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:noarch
BuildRequires: perl-XML-Simple

%description
This utility maps the icon names used by the GNOME and KDE desktops to
the icon names proposed in the Icon Naming Specification linked above.

%prep
%setup -q

%patch0 -p1 -b .fix_dtd
%patch1 -p1 -b .xfce
%patch2 -p1 -b .gtkapply
%patch3 -p1 -b .gtkstock
%patch4 -p1 -b .missinglink
autoreconf

%build
./configure --prefix=%_prefix --libdir=%_prefix/lib --libexecdir=%_prefix/lib
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog
%_bindir/icon-name-mapping
%_datadir/%name/
%_datadir/pkgconfig/%name.pc


