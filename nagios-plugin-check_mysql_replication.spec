%define		plugin	check_mysql_replication
%include	/usr/lib/rpm/macros.perl
Summary:	Nagios plugin to check replication between MySQL database instances
Summary(pl.UTF-8):	Wtyczka Nagiosa do sprawdzania replikacji między instancjami bazy danych MySQL
Name:		nagios-plugin-%{plugin}
Version:	0.03
Release:	4
License:	Opensource
Group:		Networking
Source0:	http://www.james.rcpt.to/svn/trunk/nagios/check_mysql_replication/check_mysql_replication.pl
# Source0-md5:	af8da7807e1a03bf301fa70658fb08c3
Source1:	%{plugin}.cfg
Patch0:		%{name}-defaultpass.patch
URL:		http://www.james.rcpt.to/svn/trunk/nagios/check_mysql_replication/
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	nagios-core
Requires:	perl-DBD-mysql
Conflicts:	nagios-common < 2.9-2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/nagios/plugins
%define		plugindir	%{_prefix}/lib/nagios/plugins

%description
Check if a MySQL slave is running (IO thread), plus check the master
and server to see their current replication BINLOG positions.

%description -l pl.UTF-8
Ta wtyczka sprawdza, czy podrzędny MySQL (wątek IO) działa, oraz
sprawdza instancję nadrzędną i podrzędną, aby sprawdzić ich aktualne
położenia BINLOG replikacji.

%prep
%setup -q -c -T
cp -a %{SOURCE0} %{plugin}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{plugindir}}
install -p %{plugin} $RPM_BUILD_ROOT%{plugindir}
sed -e 's,@plugindir@,%{plugindir},' %{SOURCE1} > $RPM_BUILD_ROOT%{_sysconfdir}/%{plugin}.cfg

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{plugin}.cfg
%attr(755,root,root) %{plugindir}/%{plugin}
