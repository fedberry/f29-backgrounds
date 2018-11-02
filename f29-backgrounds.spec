%global relnum 29
%global Bg_Name F%{relnum}
%global bgname %(t="%{Bg_Name}";echo ${t,,})
#fedora f29-background package release
%global fedrel %{relnum}.1.3
#fedora git commit for their Source0
%global fedgit 707ecc56c5b0070b07f316dd9d24b9bc51a7b77e82049f7f693f4c5a828cba2d7731f14b5f2ea574875c81c60b1a490f55d9b655df936b6052e0bfa23eb171ad

# Enable Extras
%global with_extras 1

Name:           %{bgname}-backgrounds
Version:        %{relnum}.2
Release:        1%{?dist}
Summary:        FedBerry %{relnum} default desktop background
License:        CC-BY-SA
URL:            https://github.com/fedberry/f29-backgrounds
Source0:        http://pkgs.fedoraproject.org/repo/pkgs/%{name}/%{name}-%{fedrel}.tar.xz/sha512/%{fedgit}/%{name}-%{fedrel}.tar.xz
Source1:        https://raw.githubusercontent.com/fedberry/%{name}/master/fedberry-backgrounds-%{version}.tar.xz
BuildArch:      noarch

# for %%_kde4_* macros
BuildRequires:  kde-filesystem

Requires:       %{name}-gnome = %{version}-%{release}
Requires:       %{name}-kde = %{version}-%{release}
Requires:       %{name}-xfce = %{version}-%{release}
Requires:       %{name}-mate = %{version}-%{release}


%description
This package contains desktop backgrounds for the FedBerry %{relnum} default
theme.  Pulls in themes for GNOME, KDE, Mate and Xfce desktops.

%package        base
Summary:        Base images for FedBerry %{relnum} default background
License:        CC-BY-SA

%description    base
This package contains base images for FedBerry %{relnum} default background.


%package        kde
Summary:        FedBerry %{relnum} default wallpaper for KDE

Requires:       %{name}-base = %{version}-%{release}
Requires:       kde-filesystem

%description    kde
This package contains KDE desktop wallpaper for the FedBerry %{relnum}
default theme.

%package        gnome
Summary:        FedBerry %{relnum} default wallpaper for Gnome and Cinnamon

Requires:       %{name}-base = %{version}-%{release}

%description    gnome
This package contains Gnome/Cinnamon desktop wallpaper for the
FedBerry %{relnum} default theme.

%package        mate
Summary:        FedBerry %{relnum} default wallpaper for Mate

Requires:       %{name}-base = %{version}-%{release}

%description    mate
This package contains Mate desktop wallpaper for the FedBerry %{relnum}
default theme.

%package        xfce
Summary:        FedBerry %{relnum} default background for XFCE4

Requires:       %{name}-base = %{version}-%{release}
Requires:       xfdesktop

%description    xfce
This package contains XFCE4 desktop background for the FedBerry %{relnum}
default theme.

%if %{with_extras}
%package        extras-base
Summary:        Base images for F%{relnum} Extras Backrounds
License:        CC-BY and CC-BY-SA

%description    extras-base
This package contains base images for F%{relnum} supplemental
wallpapers.

%package        extras-gnome
Summary:        Extra F%{relnum} Wallpapers for Gnome and Cinnamon

Requires:       %{name}-extras-base  = %{version}-%{release}

%description    extras-gnome
This package contains F%{relnum} supplemental wallpapers for Gnome
and Cinnamon

%package        extras-mate
Summary:        Extra F%{relnum} Wallpapers for Mate

Requires:       %{name}-extras-base  = %{version}-%{release}

%description    extras-mate
This package contains F%{relnum} supplemental wallpapers for Mate

%package        extras-kde
Summary:        Extra F%{relnum} Wallpapers for KDE

Requires:       %{name}-extras-base  = %{version}-%{release}

%description    extras-kde
This package contains F%{relnum} supplemental wallpapers for Gnome

%package        extras-xfce
Summary:        Extra F%{relnum} Wallpapers for XFCE

Requires:       %{name}-extras-base  = %{version}-%{release}

%description    extras-xfce
This package contains F%{relnum} supplemental wallpapers for XFCE
%endif

%prep
%autosetup -n %{name} -a 1


%build
make %{?_smp_mflags}


%install
%make_install

%files
%doc

%files base
%license CC-BY-SA-4.0 Attribution
%dir %{_datadir}/backgrounds/%{bgname}
%dir %{_datadir}/backgrounds/%{bgname}/default
%{_datadir}/backgrounds/%{bgname}/default/

%files kde
%{_kde4_datadir}/wallpapers/%{Bg_Name}/

%files gnome
%{_datadir}/gnome-background-properties/%{bgname}.xml

%files mate
%{_datadir}/mate-background-properties/%{bgname}.xml

%files xfce
%{_datadir}/xfce4/backdrops/%{bgname}.png

%if %{with_extras}
%files extras-base
%license CC-BY-SA-4.0 Attribution-Extras
%{_datadir}/backgrounds/%{bgname}/extras/*.png
%{_datadir}/backgrounds/%{bgname}/extras/%{bgname}-extras.xml

%files extras-gnome
%{_datadir}/gnome-background-properties/%{bgname}-extras.xml

%files extras-kde
%{_kde4_datadir}/wallpapers/%{Bg_Name}_*/

%files extras-mate
%{_datadir}/mate-background-properties/%{bgname}-extras.xml

%files extras-xfce
%{_datadir}/xfce4/backdrops/*.png
%endif


%changelog
* Fri Nov 02 2018 Vaughan <devel at agrez dot net> - 29.2-1
- Update for 29 release
- Sync with Fedora 29.1.3 backgrounds release

* Thu Jul 19 2018 Vaughan <devel at agrez dot net> - 28.2-1
- Update for 28 release
- Sync with Fedora 28 backgrounds

* Thu Nov 30 2017 Vaughan <devel at agrez dot net> - 27.2-1
- Fix makefile

* Thu Nov 23 2017 Vaughan <devel at agrez dot net> - 27.1-1
- Update for 27 release
- Sync with Fedora 27 backgrounds

* Wed Aug 23 2017 Vaughan <devel at agrez dot net> - 26.3-1
- Update for 26 release
- Sync with Fedora 26 backgrounds
- Bump package version > than Fedora release
- Drop alt background images

* Sun Apr 09 2017 Vaughan <devel at agrez dot net> - 25.3-1
- Update fedberry backgrounds

* Tue Jan 10 2017 Vaughan <devel at agrez dot net> - 25.2-1
- Update for 25 release
- Sync with Fedora 25 backgrounds
- Versioning extras-base requirement rhbz#1395468
- Bump package version > than Fedora release

* Sat Sep 10 2016 Vaughan <devel at agrez dot net> - 24.2-1
- Import package
- Add default fedberry backgrounds
- Bump package version

* Wed May 11 2016 Luya Tshimbalanga <luya@fedoraproject.org> - 24.1.2-1
- Upstream update fixing one wrong supplemental wallpaper

* Wed Apr 27 2016 Luya Tshimbalanga <luya@fedoraproject.org> - 24.1.1-1
- Upstream release of updated default wallpaper

* Sat Apr 23 2016 Luya Tshimbalanga <luya@fedoraproject.org> - 24.1.0-1
- Added supplemental wallpapers

* Thu Feb 18 2016 Luya Tshimbalanga <luya@fedoraproject.org> - 24.0.0-1
- Update default wallpaper
- Initial release
