#
# Conditional build:
%bcond_without	svga	# without svgalib version
#
Summary:	Multiplayer puzzle game
Summary(pl):	Gra logiczna dla wielu graczy
Name:		quadra
Version:	1.1.8
Release:	3
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/quadra/%{name}-%{version}.tar.gz
# Source0-md5:	4934ee30d0bd98c4c454829a03224f6f
Source1:	%{name}.desktop
Source2:	http://www.gamesdomain.com/faqdir/%{name}.txt
Patch0:		%{name}-DESTDIR.patch
URL:		http://quadra.sourceforge.net/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	libpng-devel
%{?with_svga:BuildRequires:	svgalib-devel}
BuildRequires:	zlib-devel
Requires:	/bin/awk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Quadra is a full-featured multiplayer action puzzle game for the X
Window System and Svgalib. Features include:

 - Recursive block chaining
 - Blocks shadows
 - Teams playing
 - TCP/IP networking (free Internet playing!)
 - Smooth block falling
 - Sound effects
 - Watches on other players
 - Chat window
 - CD-based music
 - And much more!

%description -l pl
Quadra to gra logiczna dla wielu graczy dla systemu X Window i
svgaliba. Jej cechy obejmuj±:
 - rekurencyjne ³±czenie bloków
 - cieniowanie bloków
 - grê dru¿ynow±
 - sieæ TCP/IP (darmowa gra przez Internet!)
 - p³ynne spadanie bloków
 - efekty d¼wiêkowe
 - widoki na innych graczy
 - okno pogadanek
 - muzykê opart± na CD
 - wiele wiêcej.

%package svga
Summary:	Svgalib driver for Quadra
Summary(pl):	Sterownik svgalib dla gry Quadra
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}

%description svga
Svgalib driver for Quadra

%description svga -l pl
Sterownik svgalib dla gry Quadra.

%prep
%setup -q
%patch0

%build
%{__autoconf}
%configure \
	%{!?with_svga:--without-svgalib}

%{__make}

/bin/awk 'BEGIN { RS="<pre>" ; getline ; RS="</pre>" ; getline ; print $0 }' %{SOURCE2} > quadra.txt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install images/quadra.xpm $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README quadra.txt
%attr(755,root,root) %{_bindir}/*
%{_datadir}/games/quadra.res
%{_pixmapsdir}/*
%{_desktopdir}/*.desktop

%if %{with svga}
%files svga
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/games/quadra-svga.so
%endif
