# TODO:
# - Check placement of kde files (desktop icons etc ..)
# - Add some *.kfl files (seem to be obsolete to 90's:(

Summary:	KFLog - flight logger program aimed at glider pilots
Summary(pl.UTF-8):   KFLog - program logowania lotu dla pilotów szybowców
Name:		kflog
Version:	2.1.1
Release:	0.2
License:	GNU
Group:		X11/Applications
Source0:	http://www.kflog.org/fileadmin/user_upload/kflog_downloads/src/%{name}-%{version}.tar.bz2
# Source0-md5:	266b9f8d4551b9926d9848fb0f28139e
# http://www.kflog.org/mapdata/data/airspace/Poland.kfl
URL:		http://www.kflog.org/kflog/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	rpmbuild(macros) >= 1.129
#BuildRequires:	unsermake >= 040805
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KFLog is an OpenSource program aimed at glider pilots. It gives you a
powerfull tool to plan your flight tasks before you go flying and
analyse your flights afterwards. KFLog is the only flight analyser
program available for Linux to be recognized by the FAI IGC. KFLog
projects the flights on a digital vectormap, that contains not only
airfields and airspaces, but a complete elevation-map, roads, cities,
rivers, and lots of other interesting objects.

%description -l pl.UTF-8
KFLog jest programem z otwartymi źródłami przeznaczonym dla pilotów
szybowców. Daje potężne narzędzie do planowania lotu przed lotem
oraz analizy lotu już po nim. KFLog jest jedynym analizatorem lotu
dostępnym dla Linuksa rozpoznawanym przez FAI IGC. KFLog prezentuje
lot na cyfrowej mapie, która zawiera nie tylko lotniska i strefy
przestrzeni lotniczej, ale także kompletną mapę wysokościową,
drogi, miasta, rzeki oraz sporo innych interesujących obiektów.

%prep
%setup -q

%build
cp -f %{_datadir}/automake/config.sub admin
%{__make} -f admin/Makefile.common cvs

%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir} \
	kdelnkdir=%{_desktopdir} \

mv -f $RPM_BUILD_ROOT%{_datadir}/applnk/Applications/%{name}.desktop \
	$RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so.*.*.*
%{_libdir}/*.la
%{_datadir}/apps/%{name}
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/*/*.png
