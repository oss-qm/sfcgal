Name:		sfcgal
Version:	1.3.7
Release:	0%{?dist}
Summary:	A wrapper around CGAL that intents to implement 2D and 3D operations on OGC standards models
License:	GPLv2
URL:		https://oslandia.github.io/SFCGAL/
Source0:	%{name}-%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	gdal-devel
BuildRequires:	cgal-devel
Requires:	gdal
Requires:	cgal

%description
A wrapper around CGAL that intents to implement 2D and 3D operations on OGC standards models

%package devel
Summary:	Development Libraries for the SFCAL
Requires:	pkgconfig libtiff-devel
Requires:	%{name} = %{version}-%{release}
Requires:	gdal-devel

%description devel
A wrapper around CGAL that intents to implement 2D and 3D operations on OGC standards models


%prep
%setup -q -n %{name}-%{version}


%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
    ..

make VERBOSE=1 %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}

pushd build

make install DESTDIR=$RPM_BUILD_ROOT

popd

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc README.md AUTHORS LICENSE NEWS
%{_libdir}/*.so.*

%files devel
%dir %{_includedir}
%{_bindir}/sfcgal-config
%{_includedir}/SFCGAL/*.h
%{_includedir}/SFCGAL/algorithm/*.h
%{_includedir}/SFCGAL/capi/*.h
%{_includedir}/SFCGAL/detail/*.h
%{_includedir}/SFCGAL/detail/algorithm/*.h
%{_includedir}/SFCGAL/detail/generator/*.h
%{_includedir}/SFCGAL/detail/graph/*.h
%{_includedir}/SFCGAL/detail/graph/algorithm/*.h
%{_includedir}/SFCGAL/detail/io/*.h
%{_includedir}/SFCGAL/detail/tools/*.h
%{_includedir}/SFCGAL/detail/transform/*.h
%{_includedir}/SFCGAL/detail/triangulate/*.h
%{_includedir}/SFCGAL/io/*.h
%{_includedir}/SFCGAL/triangulate/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.la

%changelog
* Thu Feb 6 2020 Enrico Weigelt, metux IT consult <info@metux.net> - 1.3.7-3
- Packaged onto new upstream release.
