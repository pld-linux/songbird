%define		_snap 20070101
%define		_rel 0.1
Summary:	Songbird Web Player
Name:		songbird
Version:	0.2
Release:	0.%{_snap}.%{_rel}
License:	GPL v2
Group:		X11/Applications/Networking
Source0:	http://developer.songbirdnest.com/nightly/snapshots/%{name}_snapshot_%{_snap}.tar.gz
# Source0-md5:	3139f09a8f3719a2fc88d30b4e74d8a3
Source1:	http://developer.songbirdnest.com/nightly/dependency_snapshots/dependencies_snapshot-linux-i386-%{_snap}.tar.gz
# NoSource1-md5:	63944bb0de1729ebe09d28f5a34a41f3
NoSource:	1
URL:		http://www.songbirdnest.com/
BuildRequires:	gstreamer-devel >= 0.10
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	libstdc++-devel
BuildRequires:	nspr-devel >= 1:4.6.3
BuildRequires:	perl-base
BuildRequires:	unzip
BuildRequires:	xulrunner-devel
BuildRequires:	zip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Songbird Web Player.

%prep
%setup -q -n %{name}
%{__tar} -C trunk/dependencies -zxf %{SOURCE1}

%build
cd trunk
%{__make} -f songbird.mk

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README*
