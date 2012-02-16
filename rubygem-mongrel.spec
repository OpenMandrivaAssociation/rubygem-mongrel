# Generated from mongrel-1.1.5.gem by gem2rpm5 0.6.7 -*- rpm-spec -*-
%define	rbname	mongrel

Summary:	A small fast HTTP library and server for Ruby apps
Name:		rubygem-%{rbname}

Version:	1.1.5
Release:	2
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://mongrel.rubyforge.org
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
Patch0:		mongrel-1.1.5-ruby1.9.patch
Patch1:		mongrel-1.1.5-add-licenses-tag.patch
Requires:	rubygem(cgi_multipart_eof_fix)
BuildRequires:	rubygems 
BuildRequires:	ruby-devel

%description
A small fast HTTP library and server that runs Rails, Camping, Nitro and Iowa
apps.

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}
BuildArch:	noarch

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q
%patch0 -p1 -b .ruby19~
gunzip metadata.gz
%patch1 -p1 -b .licenses~
gzip metadata

%build
%gem_build -f '(examples|test|tools)'

%install
%gem_install

%files
%{_bindir}/mongrel_rails
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/bin
%{ruby_gemdir}/gems/%{rbname}-%{version}/bin/mongrel_rails
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/mongrel.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/mongrel
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/mongrel/*.yml
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/mongrel/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/tools
%{ruby_gemdir}/gems/%{rbname}-%{version}/tools/*.rb
%{ruby_sitearchdir}/http11.so
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%{ruby_gemdir}/doc/%{rbname}-%{version}
%{ruby_gemdir}/gems/%{rbname}-%{version}/CHANGELOG
%{ruby_gemdir}/gems/%{rbname}-%{version}/COPYING
%{ruby_gemdir}/gems/%{rbname}-%{version}/LICENSE
%{ruby_gemdir}/gems/%{rbname}-%{version}/README
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/examples
%{ruby_gemdir}/gems/%{rbname}-%{version}/examples/*
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/test
%{ruby_gemdir}/gems/%{rbname}-%{version}/test/*
