# TODO
# - try not to use dependencies_snapshot, use our system pkgs instead
%define		_snap 20070101
%define		_rel 0.2
Summary:	Songbird Web Player
Summary(pl):	Odtwarzacz WWW Songbird
Name:		songbird
Version:	0.2
Release:	0.%{_snap}.%{_rel}
License:	GPL v2
Group:		X11/Applications/Networking
Source0:	http://developer.songbirdnest.com/nightly/snapshots/%{name}_snapshot_%{_snap}.tar.gz
# Source0-md5:	3139f09a8f3719a2fc88d30b4e74d8a3
%ifarch %{ix86}
Source1:	http://developer.songbirdnest.com/nightly/dependency_snapshots/dependencies_snapshot-linux-i386-%{_snap}.tar.gz
# NoSource1-md5:	63944bb0de1729ebe09d28f5a34a41f3
NoSource:	1
%endif
%ifarch %{x8664}
Source2:	http://developer.songbirdnest.com/nightly/dependency_snapshots/dependencies_snapshot-linux-x86_64-%{_snap}.tar.gz
# NoSource2-md5:	7f4f938851f5fafeebc986d1bfdeda09
NoSource:	2
%endif
URL:		http://www.songbirdnest.com/
BuildRequires:	gstreamer-devel >= 0.10
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	libstdc++-devel
BuildRequires:	nspr-devel >= 1:4.6.3
BuildRequires:	perl-base
BuildRequires:	unzip
BuildRequires:	xulrunner-devel
BuildRequires:	zip
Requires:	xulrunner
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_libdir}/%{name}

%description
Songbird is a desktop Web player, a digital jukebox and Web browser
mash-up. Like Winamp, it supports extensions and feathers. Like
Firefox, it is built from Mozilla, cross-platform and open source.

%description -l pl
Songbird to skrzy¿owanie graficznego odtwarzacza WWW, cyfrowej szafy
graj±cej i przegl±darki WWW. Podobnie jak Winamp obs³uguje
rozszerzenia i skórki. Podobnie jak Firefox jest oparty na Mozilli,
wieloplatformowy i ma otwarte ¼ród³a.

%prep
%setup -q -n %{name}
%ifarch %{ix86}
%{__tar} -C trunk/dependencies -zxf %{SOURCE1}
%endif
%ifarch %{x8664}
%{__tar} -C trunk/dependencies -zxf %{SOURCE2}
%endif

%build
%{__make} -C trunk -f songbird.mk %{?debug:debug}

%install
rm -rf $RPM_BUILD_ROOT
cd trunk/compiled/dist

install -d $RPM_BUILD_ROOT{%{_bindir},%{_appdir}}
cat <<'EOF' > $RPM_BUILD_ROOT%{_bindir}/songbird
#!/bin/sh
exec %{_bindir}/xulrunner %{_appdir}/application.ini
EOF
chmod a+x $RPM_BUILD_ROOT%{_bindir}/songbird
cp -a application.ini $RPM_BUILD_ROOT%{_appdir}
cp -a chrome components defaults plugins scripts $RPM_BUILD_ROOT%{_appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/songbird
%dir %{_appdir}
%{_appdir}/application.ini
%dir %{_appdir}/components
%{_appdir}/components/*.js
%{_appdir}/components/*.xpt
%attr(755,root,root) %{_appdir}/components/*.so
%dir %{_appdir}/plugins
%{_appdir}/chrome
%{_appdir}/defaults
%{_appdir}/scripts
