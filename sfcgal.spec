%define source_name SFCGAL
%define _libname    libSFCGAL1
%define _soversion  1

Name:		sfcgal
Version:	1.3.7
Release:	mtx.2%{?dist}
Summary:	A wrapper around CGAL that intents to implement 2D and 3D operations on OGC standards models
License:	GPL-2.0+
Group:		Productivity/Graphics/CAD
Url:		http://www.sfcgal.org/
Source0:	%{name}-%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	gdal-devel
BuildRequires:	cgal-devel
Requires:	gdal
Requires:	cgal

%description
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

%package -n %{_libname}
Summary:        Libraries SFCGAL applications
Group:          Development/Libraries/C and C++
Provides:       libsfcgal%{_soversion}

%description -n %{_libname}
This library  support ISO 19107:2013, OGC Simple Features Access 1.2 for 3D operations.
It provides standard compliant geometry types and operations, that can
be accessed from its C or C++ APIs. PostGIS uses the C API, to expose some
SFCGAL's functions in spatial databases (cf. PostGIS manual).

Geometry coordinates have an exact rational number representation and can
be either 2D or 3D. Among supported geometry types are :

 Points
 LineStrings
 Polygons
 TriangulatedSurfaces
 PolyhedralSurfaces
 GeometryCollections
 Solids

 Supported operations include:

 WKT reading and writing with exact rational number representation for coordinates
 Intersection operations and predicates
 Convex hull computation
 Tessellation
 Extrusion
 Area and distance computation
 Minkovski sums
 Contour offsets
 Straight skeleton generations

%files -n %{_libname}
%doc README.md AUTHORS LICENSE NEWS
%{_libdir}/*.so.*

%package devel
Summary:	Development Libraries for the SFCAL
Requires:	pkgconfig libtiff-devel
Requires:	%{_libname} = %{version}-%{release}
Requires:	gdal-devel

%description devel
Content headers & files to envelopment files for %{_libname}

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
