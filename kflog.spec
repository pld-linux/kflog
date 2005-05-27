# TODO: Needs fixing placement of kde files (desktop icons etc ..)
Summary:	KFLog is flight logger program aimed at glider pilots
Summary(pl):	KFLog jest programem logowania lotu dla pilotów szybowców
Name:		kflog
Version:	2.1.1
Release:	0.1
License:	GNU
Group:		TODO
######		Unknown group!
Source0:	http://www.kflog.org/fileadmin/user_upload/kflog_downloads/src/%{name}-%{version}.tar.bz2
# Source0-md5:
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

%description -l pl
KFLog jest opensource'owym programem przeznaczonym dla pilotów
szybowców. Daje pote¿ne narzêdzie do planowania lotu prze lotem
oraz analizy lotu ju¿ po. KFLog jest jedynym analizatorem lotu
dostêpnym dla Linuxa rozpoznawanym przez FAI IGC. KFLog prezentuje
lot na cyfrowej mapie, które zawiera nie tylko lotniska i strefy
przestrzeni lotniczej, ale tak¿e kompletn± mape wysoko¶ciow±,
drogi, miasta, rzeki oraz sporo innych interesuj±cych obiektów.

%prep
#setup -q -n %{name}
%setup -q

%build
cp -f %{_datadir}/automake/config.sub admin
#export PATH=/usr/share/unsermake:$PATH
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

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
#%{_pixmapsdir}/*
#%{_desktopdir}/*
%{_iconsdir}/*/*/apps/%{name}.png
#%{_datadir}/mimelnk/application/*
%{_datadir}/apps/%{name}
