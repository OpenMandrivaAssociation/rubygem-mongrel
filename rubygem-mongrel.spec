# Generated from mongrel-1.0.1.gem by gem2rpm -*- rpm-spec -*-
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname mongrel
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}
%define ruby_sitearch %(ruby -rrbconfig -e "puts Config::CONFIG['sitearchdir']")
# Shortcuts for Cgi_Multipart_Eof_Fix (cmef)
%define cmef_version 2.5.0

Summary: A small fast HTTP library and server for Ruby apps
Name: rubygem-%{gemname}

Version: 1.1.5
Release: %mkrel 1
Group: Development/Ruby 
# The entire source code is (GPLv2+ or Ruby) except for the code in
# cgi_multipart_eof_fix-2.5.0.gem  which is AFL
License: (GPLv2+ or Ruby) and AFL
URL: http://mongrel.rubyforge.org
Source0: http://gems.rubyforge.org/gems/%{gemname}-%{version}.gem
Source1: http://gems.rubyforge.org/gems/cgi_multipart_eof_fix-%{cmef_version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root-%(%{__id_u} -n)
Requires: rubygems
BuildRequires: ruby-devel
Requires: rubygem(daemons) >= 1.0.3
Requires: rubygem(fastthread) >= 0.6.2
Requires: rubygem(gem_plugin) >= 0.2.2
BuildRequires: rubygems
BuildRequires: ruby-rdoc
Provides: rubygem(%{gemname}) = %{version}

%description
A small fast HTTP library and server that runs Rails, Camping, Nitro and Iowa
apps.

%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}
gem install --local --install-dir %{buildroot}%{gemdir} \
            --force --rdoc %{SOURCE0}
gem install --local --install-dir %{buildroot}%{gemdir} \
            --force --rdoc %{SOURCE1}
install -d -m0755 %{buildroot}%{ruby_sitearch}
mv %{buildroot}%{geminstdir}/lib/http11.so %{buildroot}%{ruby_sitearch}
strip %{buildroot}%{ruby_sitearch}/http11.so
chmod 0755 %{buildroot}%{ruby_sitearch}/http11.so
rm -rf %{buildroot}%{geminstdir}/ext
rm -rf %{buildroot}/%{geminstdir}/.require_paths
mkdir -p %{buildroot}/%{_bindir}

# % {geminstdir}/bin/mongrel_rails does not have a shebang, but it doesn't have to (it's loaded by % {_bindir}/mongrel_rails
chmod a-x %{buildroot}/%{geminstdir}/bin/mongrel_rails
mv %{buildroot}/%{gemdir}/bin/mongrel_rails %{buildroot}/%{_bindir}/mongrel_rails
rm -rf %{buildroot}/%{gemdir}/bin

sed 's.#!/usr/local/bin/ruby.#!/usr/bin/env ruby.' -i %{buildroot}%{geminstdir}/examples/webrick_compare.rb
chmod a+x %{buildroot}%{geminstdir}/examples/webrick_compare.rb
chmod a+x %{buildroot}%{geminstdir}/examples/camping/blog.rb
chmod a+x %{buildroot}%{geminstdir}/examples/camping/tepee.rb
chmod a+x %{buildroot}%{gemdir}/gems/cgi_multipart_eof_fix-%{cmef_version}/test/*.rb

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%{_bindir}/mongrel_rails
%{ruby_sitearch}/http11.so
%dir %{geminstdir}
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/COPYING
%doc %{geminstdir}/CHANGELOG
%doc %{geminstdir}/README
%doc %{geminstdir}/LICENSE
%doc %{geminstdir}/Manifest
%doc %{geminstdir}/TODO
%doc %{geminstdir}/%{gemname}.gemspec
%{geminstdir}/mongrel-public_cert.pem
%{geminstdir}/bin/
%{geminstdir}/examples/
%{geminstdir}/lib/
%{geminstdir}/setup.rb
%{geminstdir}/test/
%{geminstdir}/tools/
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec

%dir %{gemdir}/gems/cgi_multipart_eof_fix-%{cmef_version}/
%{gemdir}/gems/cgi_multipart_eof_fix-%{cmef_version}/lib/
%{gemdir}/gems/cgi_multipart_eof_fix-%{cmef_version}/test/
%doc %{gemdir}/gems/cgi_multipart_eof_fix-%{cmef_version}/CHANGELOG
%doc %{gemdir}/gems/cgi_multipart_eof_fix-%{cmef_version}/LICENSE
%doc %{gemdir}/gems/cgi_multipart_eof_fix-%{cmef_version}/Manifest
%doc %{gemdir}/gems/cgi_multipart_eof_fix-%{cmef_version}/README
%doc %{gemdir}/gems/cgi_multipart_eof_fix-%{cmef_version}/cgi_multipart_eof_fix.gemspec
%doc %{gemdir}/doc/cgi_multipart_eof_fix-%{cmef_version}
%{gemdir}/cache/cgi_multipart_eof_fix-%{cmef_version}.gem
%{gemdir}/specifications/cgi_multipart_eof_fix-%{cmef_version}.gemspec
