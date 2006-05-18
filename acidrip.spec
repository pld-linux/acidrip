%include	/usr/lib/rpm/macros.perl
Summary:	Graphical frontend for MPlayer/Mencoder for DVD ripping
Summary(pl):	Graficzna nak³adka na MPlayer/Mencoder do zgrywania DVD
Name:		acidrip
Version:	0.14
Release:	1
License:	GPL/Artistic
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/acidrip/%{name}-%{version}.tar.gz
# Source0-md5:	c1c27bbf658e5c30f43e067a8ae283de
Source1:	%{name}.desktop
Patch0:		%{name}-makefile.patch
URL:		http://untrepid.com/acidrip/
BuildRequires:	perl-Gtk2 >= 0.98
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	lsdvd >= 0.10
Requires:	mplayer
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AcidRip is a Gtk2-perl application for ripping and encoding DVD's. It
is Graphical wraper to MPlayer and MEncoder which automates the
process in a number of ways:
- finds longest title
- calculate video bitrate for given filesize
- finds black bands and crops them
- gives sugesstions for improved performance

%description -l pl
AcidRip jest aplikacj± opart± o Gtk2-perl s³u¿±c± do zgrywania i
odkodowywania p³yt DVD. Jest to graficzna nak³adka na MPlayera i
MEncodera, która automatyzuje ten proces na kilka sposobów:
- znajduje najd³u¿szy tytu³
- oblicza transfer wideo dla danej wielko¶ci pliku
- znajduje i przycina czarne opaski
- podaje propozycje dla zwiêkszenia wydajno¶ci

%prep
%setup -q
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -c %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG TODO
%attr(755,root,root) %{_bindir}/*
%dir %{perl_vendorlib}/AcidRip
%{perl_vendorlib}/AcidRip/*.pm
%{_desktopdir}/*.desktop
%{_mandir}/man1/*
