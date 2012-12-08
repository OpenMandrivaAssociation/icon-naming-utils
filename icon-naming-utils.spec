%define name icon-naming-utils
%define version 0.8.90
%define release %mkrel 7

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




%changelog
* Sun May 08 2011 Funda Wang <fwang@mandriva.org> 0.8.90-6mdv2011.0
+ Revision: 672454
- rebuild

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.8.90-5
+ Revision: 665500
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.8.90-4mdv2011.0
+ Revision: 605964
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.8.90-3mdv2010.1
+ Revision: 522919
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.8.90-2mdv2010.0
+ Revision: 425201
- rebuild

* Wed Mar 04 2009 Götz Waschk <waschk@mandriva.org> 0.8.90-1mdv2009.1
+ Revision: 348226
- new version
- update patch 0 from Fedora
- rediff patch 1
- move icon-name-mapping to /usr/bin
- update license
- update URLs

* Fri Jun 20 2008 Götz Waschk <waschk@mandriva.org> 0.8.7-1mdv2009.0
+ Revision: 227370
- new version fetched from debian
- the URL is dead

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.8.6-3mdv2009.0
+ Revision: 221580
- rebuild

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 0.8.6-2mdv2008.1
+ Revision: 150282
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Aug 28 2007 Götz Waschk <waschk@mandriva.org> 0.8.6-1mdv2008.0
+ Revision: 72534
- new version
- rediff patch 4

  + Jérôme Soyer <saispo@mandriva.org>
    - Add *butu patches


* Tue Feb 27 2007 Götz Waschk <waschk@mandriva.org> 0.8.2-1mdv2007.0
+ Revision: 126658
- Import icon-naming-utils

* Tue Feb 27 2007 Götz Waschk <waschk@mandriva.org> 0.8.2-1mdv2007.1
- New version 0.8.2

* Wed Aug 23 2006 Götz Waschk <waschk@mandriva.org> 0.8.1-1mdv2007.0
- New release 0.8.1

* Wed Aug 09 2006 Götz Waschk <waschk@mandriva.org> 0.8.0-1mdv2007.0
- New release 0.8.0

* Thu Jul 27 2006 Götz Waschk <waschk@mandriva.org> 0.7.4-2mdv2007.0
- rebuild for new find-requires

* Wed Jul 26 2006 Götz Waschk <waschk@mandriva.org> 0.7.4-1mdv2007.0
- New release 0.7.4

* Tue Jul 11 2006 Götz Waschk <waschk@mandriva.org> 0.7.3-1mdv2007.0
- New release 0.7.3

* Mon Apr 24 2006 Götz Waschk <waschk@mandriva.org> 0.7.2-1mdk
- New release 0.7.2

* Tue Feb 14 2006 Götz Waschk <waschk@mandriva.org> 0.6.8-1mdk
- New release 0.6.8

* Sun Feb 05 2006 Götz Waschk <waschk@mandriva.org> 0.6.7-1mdk
- New release 0.6.7

* Tue Jan 17 2006 Götz Waschk <waschk@mandriva.org> 0.6.5-1mdk
- initial package

