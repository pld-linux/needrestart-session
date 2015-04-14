%include	/usr/lib/rpm/macros.perl
Summary:	check for processes need to be restarted in user sessions
Name:		needrestart-session
Version:	0.3
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	https://github.com/liske/needrestart-session/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	ea07cb200f2ac2162198ac0475f0213e
URL:		https://github.com/liske/needrestart-session
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	dbus
Requires:	grep
Requires:	needrestart >= 2.0
Requires:	polkit
Requires:	procps
Requires:	wmctrl
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_prefix}/lib/%{name}

%description
needrestart checks which processes need to be restarted after library
upgrades. needrestart-session implements a notification of user
sessions about their obsolete processes after system upgrades.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README.md ChangeLog
%attr(755,root,root) %{_sysconfdir}/needrestart/notify.d/300-needrestart-session
%attr(755,root,root) %{_bindir}/needrestart-session
%{_desktopdir}/needrestart-session.desktop
%{_desktopdir}/needrestart.desktop
/etc/dbus-1/system.d/net.ibh.NeedRestart.System.conf
/etc/xdg/autostart/needrestart-dbus-session.desktop
%{_datadir}/dbus-1/system-services/net.ibh.NeedRestart.System.service
%dir %{_datadir}/needrestart-session
%{_datadir}/needrestart-session/needrestart.svg
%{_datadir}/needrestart-session/needrestart.xpm
%dir %{_libexecdir}
%attr(755,root,root) %{_libexecdir}/needrestart-dbus-session
%attr(755,root,root) %{_libexecdir}/needrestart-dbus-system
%attr(755,root,root) %{_libexecdir}/needrestart-x11
