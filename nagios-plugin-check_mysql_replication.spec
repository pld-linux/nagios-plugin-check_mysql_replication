%include	/usr/lib/rpm/macros.perl
Summary:	Nagios plugin to check replication between MySQL database instances
Summary(pl.UTF-8):	Wtyczka Nagiosa do sprawdzania replikacji między instancjami bazy danych MySQL
Name:		nagios-plugin-check_mysql_replication
Version:	0.03
Release:	3
License:	Opensource
Group:		Networking
Source0:	http://www.james.rcpt.to/svn/trunk/nagios/check_mysql_replication/check_mysql_replication.pl
# Source0-md5:	af8da7807e1a03bf301fa70658fb08c3
Patch0:		%{name}-defaultpass.patch
URL:		http://www.james.rcpt.to/svn/trunk/nagios/check_mysql_replication/
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	nagios-core
Requires:	perl-DBD-mysql
Conflicts:	nagios-common < 2.9-2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_plugindir	%{_prefix}/lib/nagios/plugins
%define		_sysconfdir	/etc/nagios/plugins

%description
Check if a MySQL slave is running (IO thread), plus check the master
and server to see their current replication BINLOG positions.

%description -l pl.UTF-8
Ta wtyczka sprawdza, czy podrzędny MySQL (wątek IO) działa, oraz
sprawdza instancję nadrzędną i podrzędną, aby sprawdzić ich aktualne
położenia BINLOG replikacji.

%prep
%setup -q -c -T
install %{SOURCE0} check_mysql_replication.pl
%patch0 -p1
cat > nagios.cfg <<'EOF'
# Usage:
# check_mysql_replication!$HOSTADDRESS$!3309
# and define $USER3$ + $USER4$ for mysql passwords
define command {
	command_name    check_mysql_replication
	command_line    %{_plugindir}/check_mysql_replication --slave $ARG1$ --slave-port $ARG2$ --slave-user $USER3$ --slave-pass $USER4$ --master-user $USER3$ --master-pass $USER4$
}
EOF

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_plugindir}}
install check_mysql_replication.pl $RPM_BUILD_ROOT%{_plugindir}/check_mysql_replication
cp -a nagios.cfg $RPM_BUILD_ROOT%{_sysconfdir}/check_mysql_replication.cfg

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/check_mysql_replication.cfg
%attr(755,root,root) %{_plugindir}/check_mysql_replication
