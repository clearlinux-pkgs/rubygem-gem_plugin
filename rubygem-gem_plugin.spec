#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-gem_plugin
Version  : 0.2.3
Release  : 4
URL      : https://rubygems.org/downloads/gem_plugin-0.2.3.gem
Source0  : https://rubygems.org/downloads/gem_plugin-0.2.3.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1 Ruby
Requires: rubygem-gem_plugin-bin
BuildRequires : ruby
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-test-unit

%description
= GemPlugin:  Gem Based Plugin System
GemPlugin is a system that lets your users install gems and lets you load
them as additional features to use in your software.  It originated from the
Mongrel (http://mongrel.rubyforge.org) project but proved useful enough to
break out into a separate project.

%package bin
Summary: bin components for the rubygem-gem_plugin package.
Group: Binaries

%description bin
bin components for the rubygem-gem_plugin package.


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n gem_plugin-0.2.3
gem spec %{SOURCE0} -l --ruby > rubygem-gem_plugin.gemspec

%build
gem build rubygem-gem_plugin.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
gem_plugin-0.2.3.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/gem_plugin-0.2.3
ruby -v -I.:lib:test test*/test_*.rb || :
popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/gem_plugin-0.2.3.gem
/usr/lib64/ruby/gems/2.3.0/gems/gem_plugin-0.2.3/CHANGELOG
/usr/lib64/ruby/gems/2.3.0/gems/gem_plugin-0.2.3/COPYING
/usr/lib64/ruby/gems/2.3.0/gems/gem_plugin-0.2.3/LICENSE
/usr/lib64/ruby/gems/2.3.0/gems/gem_plugin-0.2.3/Manifest
/usr/lib64/ruby/gems/2.3.0/gems/gem_plugin-0.2.3/README
/usr/lib64/ruby/gems/2.3.0/gems/gem_plugin-0.2.3/bin/gpgen
/usr/lib64/ruby/gems/2.3.0/gems/gem_plugin-0.2.3/gem_plugin.gemspec
/usr/lib64/ruby/gems/2.3.0/gems/gem_plugin-0.2.3/lib/gem_plugin.rb
/usr/lib64/ruby/gems/2.3.0/gems/gem_plugin-0.2.3/resources/COPYING
/usr/lib64/ruby/gems/2.3.0/gems/gem_plugin-0.2.3/resources/LICENSE
/usr/lib64/ruby/gems/2.3.0/gems/gem_plugin-0.2.3/resources/README
/usr/lib64/ruby/gems/2.3.0/gems/gem_plugin-0.2.3/resources/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/gem_plugin-0.2.3/resources/lib/project/init.rb
/usr/lib64/ruby/gems/2.3.0/gems/gem_plugin-0.2.3/resources/resources/defaults.yaml
/usr/lib64/ruby/gems/2.3.0/gems/gem_plugin-0.2.3/setup.rb
/usr/lib64/ruby/gems/2.3.0/gems/gem_plugin-0.2.3/test/test_plugins.rb
/usr/lib64/ruby/gems/2.3.0/specifications/gem_plugin-0.2.3.gemspec

%files bin
%defattr(-,root,root,-)
/usr/bin/gpgen
