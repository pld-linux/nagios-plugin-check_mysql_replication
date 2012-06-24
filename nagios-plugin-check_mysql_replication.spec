%include	/usr/lib/rpm/macros.perl
Summary:	Nagios plugin to check replication between MySQL database instances
Summary(pl):	Wtyczka Nagiosa do sprawdzania replikacji mi�dzy instancjami bazy danych MySQL
Name:		nagios-plugin-check_mysql_replication
Version:	0.03
Release:	1
License:	Opensource
Group:		Networking
Source0:	http://www.james.rcpt.to/svn/trunk/nagios/check_mysql_replication/check_mysql_replication.pl
# Source0-md5:	af8da7807e1a03bf301fa70658fb08c3
URL:		http://www.james.rcpt.to/svn/trunk/nagios/check_mysql_replication/
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	nagios-core
Requires:	perl-DBD-mysql
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_plugindir	%{_libdir}/nagios/plugins
%define		_sysconfdir	/etc/nagios/plugins

%description
Check if a MySQL slave is running (IO thread), plus check the master
and server to see their current replication BINLOG positions.

%description -l pl
Ta wtyczka sprawdza, czy podrz�dny MySQL (w�tek IO) dzia�a, oraz
sprawdza instancj� nadrz�dn� i podrz�dn�, aby sprawdzi� ich aktualne
po�o�enia BINLOG replikacji.

%prep
%setup -q -c -T
install %{SOURCE0} check_mysql_replication.pl

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_plugindir}}
install check_mysql_replication.pl $RPM_BUILD_ROOT%{_plugindir}/check_mysql_replication

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_plugindir}/*
