#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-jsonlite
Version  : 0.9.17
Release  : 16
URL      : http://cran.r-project.org/src/contrib/jsonlite_0.9.17.tar.gz
Source0  : http://cran.r-project.org/src/contrib/jsonlite_0.9.17.tar.gz
Summary  : A Robust, High Performance JSON Parser and Generator for R
Group    : Development/Tools
License  : MIT
Requires: R-jsonlite-lib
BuildRequires : R-knitr
BuildRequires : R-testthat
BuildRequires : clr-R-helpers

%description
Changes in yajl code by Jeroen:
- Manually changed the header include paths in some c/h files to avoid cmake dependency.
- Comment out call to abort() in src/yajl/yajl_parser.c (for CMD check)
- Manually generated yajl.version.h from yajl.version.h.in (by running cmake)
- Patch for CMD check warnings on Windows: https://github.com/lloyd/yajl/issues/143
- Patch for error messages in yajl_tree_parse: https://github.com/lloyd/yajl/issues/144
- Fix for windows XP: https://rt.cpan.org/Public/Bug/Display.html?id=69113
- in yajl_tree.c added functions: push_parser_new and push_parser_get

%package lib
Summary: lib components for the R-jsonlite package.
Group: Libraries

%description lib
lib components for the R-jsonlite package.


%prep
%setup -q -c -n jsonlite

%build

%install
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -ffunction-sections -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -ffunction-sections -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --build  -l %{buildroot}/usr/lib64/R/library jsonlite
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library jsonlite || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/jsonlite/CITATION
/usr/lib64/R/library/jsonlite/DESCRIPTION
/usr/lib64/R/library/jsonlite/INDEX
/usr/lib64/R/library/jsonlite/LICENSE
/usr/lib64/R/library/jsonlite/Meta/Rd.rds
/usr/lib64/R/library/jsonlite/Meta/hsearch.rds
/usr/lib64/R/library/jsonlite/Meta/links.rds
/usr/lib64/R/library/jsonlite/Meta/nsInfo.rds
/usr/lib64/R/library/jsonlite/Meta/package.rds
/usr/lib64/R/library/jsonlite/Meta/vignette.rds
/usr/lib64/R/library/jsonlite/NAMESPACE
/usr/lib64/R/library/jsonlite/NEWS
/usr/lib64/R/library/jsonlite/R/jsonlite
/usr/lib64/R/library/jsonlite/R/jsonlite.rdb
/usr/lib64/R/library/jsonlite/R/jsonlite.rdx
/usr/lib64/R/library/jsonlite/doc/index.html
/usr/lib64/R/library/jsonlite/doc/json-aaquickstart.R
/usr/lib64/R/library/jsonlite/doc/json-aaquickstart.Rmd
/usr/lib64/R/library/jsonlite/doc/json-aaquickstart.html
/usr/lib64/R/library/jsonlite/doc/json-apis.Rmd
/usr/lib64/R/library/jsonlite/doc/json-apis.html
/usr/lib64/R/library/jsonlite/doc/json-mapping.pdf
/usr/lib64/R/library/jsonlite/doc/json-mapping.pdf.asis
/usr/lib64/R/library/jsonlite/doc/json-opencpu.R
/usr/lib64/R/library/jsonlite/doc/json-opencpu.Rnw
/usr/lib64/R/library/jsonlite/doc/json-opencpu.pdf
/usr/lib64/R/library/jsonlite/doc/json-paging.Rmd
/usr/lib64/R/library/jsonlite/doc/json-paging.html
/usr/lib64/R/library/jsonlite/help/AnIndex
/usr/lib64/R/library/jsonlite/help/aliases.rds
/usr/lib64/R/library/jsonlite/help/jsonlite.rdb
/usr/lib64/R/library/jsonlite/help/jsonlite.rdx
/usr/lib64/R/library/jsonlite/help/paths.rds
/usr/lib64/R/library/jsonlite/html/00Index.html
/usr/lib64/R/library/jsonlite/html/R.css
/usr/lib64/R/library/jsonlite/tests/flatten.R
/usr/lib64/R/library/jsonlite/tests/helper-toJSON.R
/usr/lib64/R/library/jsonlite/tests/issues.txt
/usr/lib64/R/library/jsonlite/tests/readme.txt
/usr/lib64/R/library/jsonlite/tests/run-all.R
/usr/lib64/R/library/jsonlite/tests/test-fromJSON-NA-values.R
/usr/lib64/R/library/jsonlite/tests/test-fromJSON-array.R
/usr/lib64/R/library/jsonlite/tests/test-fromJSON-dataframe.R
/usr/lib64/R/library/jsonlite/tests/test-fromJSON-datasets.R
/usr/lib64/R/library/jsonlite/tests/test-fromJSON-date.R
/usr/lib64/R/library/jsonlite/tests/test-fromJSON-matrix.R
/usr/lib64/R/library/jsonlite/tests/test-libjson-escaping.R
/usr/lib64/R/library/jsonlite/tests/test-libjson-large.R
/usr/lib64/R/library/jsonlite/tests/test-libjson-utf8.R
/usr/lib64/R/library/jsonlite/tests/test-libjson-validator.R
/usr/lib64/R/library/jsonlite/tests/test-network-Github.R
/usr/lib64/R/library/jsonlite/tests/test-serializeJSON-datasets.R
/usr/lib64/R/library/jsonlite/tests/test-serializeJSON-functions.R
/usr/lib64/R/library/jsonlite/tests/test-serializeJSON-types.R
/usr/lib64/R/library/jsonlite/tests/test-toJSON-AsIs.R
/usr/lib64/R/library/jsonlite/tests/test-toJSON-Date.R
/usr/lib64/R/library/jsonlite/tests/test-toJSON-NA-values.R
/usr/lib64/R/library/jsonlite/tests/test-toJSON-NULL-values.R
/usr/lib64/R/library/jsonlite/tests/test-toJSON-POSIXt.R
/usr/lib64/R/library/jsonlite/tests/test-toJSON-complex.R
/usr/lib64/R/library/jsonlite/tests/test-toJSON-dataframe.R
/usr/lib64/R/library/jsonlite/tests/test-toJSON-factor.R
/usr/lib64/R/library/jsonlite/tests/test-toJSON-keep-vec-names.R
/usr/lib64/R/library/jsonlite/tests/test-toJSON-logical.R
/usr/lib64/R/library/jsonlite/tests/test-toJSON-matrix.R
/usr/lib64/R/library/jsonlite/tests/test-toJSON-numeric.R
/usr/lib64/R/library/jsonlite/tests/test-toJSON-raw.R
/usr/lib64/R/library/jsonlite/tests/test-toJSON-zerovec.R
/usr/lib64/R/library/jsonlite/tests/testS4.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/jsonlite/libs/jsonlite.so
