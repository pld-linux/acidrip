# TODO:
# - remove buildtime test for lsdvd/mplayer (major build issue)
# - better descritions
#
%include        /usr/lib/rpm/macros.perl
Summary:	Graphical frontend for MPlayer/Mencoder for DVD ripping
Summary(pl):	Graficzna nak³adka na MPlayer/Mencoder do zgrywania DVD
Name:		acidrip
Version:	0.11
Release:	0.1
License:	GPL/Artistic
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/acidrip/%{name}-%{version}.tar.gz
# Source0-md5:	1a06fb89a4ac2486b9a2f192afb49386
Source1:	%{name}.desktop
# icon taken from gnome-gorilla theme and a little bit modificated
Source2:	%{name}.png
URL:		http://acidrip.thirtythreeandathird.net/
BuildRequires:	perl-Gtk2 >= 0.98
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	lsdvd >= 0.9
Requires:	mplayer
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AcidRip is a Gtk2-perl application for ripping and encoding DVD's.

%description -l pl
AcidRip jest aplikacj± opart± o Gtk2-perl s³u¿±c± do zgrywania
i odkodowywania p³yt DVD.

%prep
%setup -q

%build
%{__perl} Makefile.PL \
        INSTALLDIRS=vendor

%{__make} \
        OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -c %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install -c %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG TODO
%attr(755,root,root) %{_bindir}/*
%dir %{perl_vendorlib}/AcidRip
%{perl_vendorlib}/AcidRip/*.pm
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
%{_mandir}/man1/*
