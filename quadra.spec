Summary:	Multiplayer puzzle game
Summary(pl):	Gra logiczna dla wielu graczy
Name:		quadra
Version:	1.1.8
Release:	2
License:	GPL
Group:		X11/Applications/Games
Source0:	http://download.sourceforge.net/quadra/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	http://www.gamesdomain.com/faqdir/%{name}.txt
Patch0:		%{name}-DESTDIR.patch
Icon:		quadra.xpm
URL:		http://quadra.Sourceforge.net/
Requires:	/bin/awk
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	libpng-devel
%ifarch %{ix86} alpha
BuildRequires:	svgalib-devel
%endif
BuildRequires:	zlib-devel
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
Quadra to gra logiczna dla wielu graczy, wzorowana na Tetris.

%package svga
Summary:	Svgalib driver for Quadra
Summary(pl):	Driver svgalib dla gry quadra
Group:		Applications/Games
Requires:	quadra = %{version}

%description svga
Svgalib driver for Quadra

%description svga -l pl
Driver svgalib dla gry quadra

%prep
%setup -q
%patch0

%build
rm -f missing
%{__autoconf}
%configure \
%ifnarch %{ix86} alpha
	--without-svgalib
%endif
%{__make}

/bin/awk 'BEGIN { RS="<pre>" ; getline ; RS="</pre>" ; getline ; print $0 }' %{SOURCE2} > quadra.txt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_applnkdir}/Games}

%{__make} install DESTDIR="$RPM_BUILD_ROOT"
install images/quadra.xpm $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README quadra.txt
%attr(755,root,root) %{_bindir}/*
%{_datadir}/games/quadra.res
%{_pixmapsdir}/*
%{_applnkdir}/Games/*

%ifarch %{ix86} alpha
%files svga
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/games/quadra-svga.so
%endif