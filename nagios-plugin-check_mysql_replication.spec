%include	/usr/lib/rpm/macros.perl
Summary:	Nagios plugin to check replication between MySQL database instances
Name:		nagios-plugin-check_mysql_replication
Version:	0.03
Release:	0.1
License:	Opensource
Group:		Networking
Source0:	http://opensource.fotango.com/svn/trunk/systems/nagios_plugins/check_replication.pl
# Source0-md5:	d8b3b3f133416d2d813fa43343ed4ae9
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	nagios-core
Requires:	perl-DBD-mysql
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_plugindir	%{_libdir}/nagios/plugins
%define		_sysconfdir	/etc/nagios/plugins

%description
Check if a MySQL slave is running (IO thread), plus check the master
and server to see their current replication BINLOG positions.

%prep
%setup -q -c -T
install %{SOURCE0} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_plugindir}}
install check_replication.pl $RPM_BUILD_ROOT%{_plugindir}/check_mysql_replication

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_plugindir}/*
