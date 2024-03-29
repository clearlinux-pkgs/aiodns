#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : aiodns
Version  : 3.0.0
Release  : 18
URL      : https://files.pythonhosted.org/packages/27/79/df72e25df0fdd9bf5a5ab068539731d27c5f2ae5654621ae0c92ceca94cf/aiodns-3.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/27/79/df72e25df0fdd9bf5a5ab068539731d27c5f2ae5654621ae0c92ceca94cf/aiodns-3.0.0.tar.gz
Summary  : Simple DNS resolver for asyncio
Group    : Development/Tools
License  : MIT
Requires: aiodns-license = %{version}-%{release}
Requires: aiodns-python = %{version}-%{release}
Requires: aiodns-python3 = %{version}-%{release}
Requires: pycares
BuildRequires : buildreq-distutils3
BuildRequires : pycares

%description
Simple DNS resolver for asyncio
        ===============================

%package license
Summary: license components for the aiodns package.
Group: Default

%description license
license components for the aiodns package.


%package python
Summary: python components for the aiodns package.
Group: Default
Requires: aiodns-python3 = %{version}-%{release}

%description python
python components for the aiodns package.


%package python3
Summary: python3 components for the aiodns package.
Group: Default
Requires: python3-core
Provides: pypi(aiodns)
Requires: pypi(pycares)

%description python3
python3 components for the aiodns package.


%prep
%setup -q -n aiodns-3.0.0
cd %{_builddir}/aiodns-3.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1635701584
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/aiodns
cp %{_builddir}/aiodns-3.0.0/LICENSE %{buildroot}/usr/share/package-licenses/aiodns/b10de517c27f874e95de198bbdc907494110bcea
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/aiodns/b10de517c27f874e95de198bbdc907494110bcea

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
