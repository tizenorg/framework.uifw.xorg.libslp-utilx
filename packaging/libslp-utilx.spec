#sbs-git:slp/pkgs/l/libslp-utilx libslp-utilx 0.1.7 5957503c84e65113399e346c7d5618e73957d6ff
Name:       libslp-utilx
Summary:    utilX
Version:    0.5.4
Release:    1
Group:      System/Libraries
License:    Apache-2.0
Source0:    %{name}-%{version}.tar.gz
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

BuildRequires: cmake
BuildRequires: pkgconfig(libdri2)
BuildRequires: pkgconfig(dri2proto)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xv)
BuildRequires: pkgconfig(xdamage)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(libtbm)
BuildRequires: pkgconfig(ttrace)

%description
Utility functions for the XWindow


%package devel
Summary:    utilX
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   pkgconfig(xproto)
Requires:   pkgconfig(x11)

%description devel
Utility functions for the XWindow (developement files)

%prep
%setup -q


%build
cmake . -DCMAKE_INSTALL_PREFIX=%{_prefix}


make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

# for license notification
mkdir -p %{buildroot}/usr/share/license
cp %{_builddir}/%{buildsubdir}/LICENSE.APLv2 %{buildroot}/usr/share/license/%{name}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
/usr/lib/libutilX.so.*
/usr/share/license/%{name}

%files devel
%defattr(-,root,root,-)
/usr/include/*
/usr/lib/libutilX.so
/usr/lib/pkgconfig/utilX.pc




