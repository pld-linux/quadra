# TODO
# - fix format-security"

# Conditional build:
%bcond_with	svga	# without svgalib version

Summary:	Multiplayer Action Puzzle Game
Summary(pl.UTF-8):	Gra logiczna dla wielu graczy
Name:		quadra
Version:	1.2.0
Release:	0.2
License:	LGPL v2.1
Group:		X11/Applications/Games
Source0:	http://quadra.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	df179970c4eb75af9ccdc5527d901fa6
Patch0:		%{name}-desktop.patch
Source2:	http://www.gamesdomain.com/faqdir/%{name}.txt
URL:		http://code.google.com/p/quadra/
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

%description -l pl.UTF-8
Quadra to gra logiczna dla wielu graczy dla systemu X Window i
svgaliba. Jej cechy obejmują:
 - rekurencyjne łączenie bloków
 - cieniowanie bloków
 - grę drużynową
 - sieć TCP/IP (darmowa gra przez Internet!)
 - płynne spadanie bloków
 - efekty dźwiękowe
 - widoki na innych graczy
 - okno pogadanek
 - muzykę opartą na CD
 - wiele więcej.

%package svga
Summary:	Svgalib driver for Quadra
Summary(pl.UTF-8):	Sterownik svgalib dla gry Quadra
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}

%description svga
Svgalib driver for Quadra

%description svga -l pl.UTF-8
Sterownik svgalib dla gry Quadra.

%prep
%setup -q

%build
CPPFLAGS="%{rpmcflags} -Wno-error=format-security"
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

cp -p images/quadra.xpm $RPM_BUILD_ROOT%{_pixmapsdir}
cp -p Quadra.desktop $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README ChangeLog quadra.txt
%attr(755,root,root) %{_bindir}/quadra
%{_datadir}/games/quadra.res
%{_pixmapsdir}/quadra.xpm
%{_desktopdir}/quadra.desktop

%if %{with svga}
%files svga
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/games/quadra-svga.so
%endif
