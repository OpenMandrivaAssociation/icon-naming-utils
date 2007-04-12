%define name icon-naming-utils
%define version 0.8.2
%define release %mkrel 1

Summary: Icon handling tools of the Tango Project
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://tango-project.org/releases/%{name}-%{version}.tar.bz2
License: GPL
Group: Graphical desktop/Other
Url: http://tango-project.org/Tango_Icon_Library#Download
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:noarch
BuildRequires: perl-XML-Simple

%description
This utility maps the icon names used by the GNOME and KDE desktops to
the icon names proposed in the Icon Naming Specification linked above.

%prep
%setup -q

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
%_prefix/lib/icon-name-mapping
%_datadir/dtds/
%_datadir/%name/
%_datadir/pkgconfig/%name.pc


