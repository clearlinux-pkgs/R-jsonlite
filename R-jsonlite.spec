#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-jsonlite
Version  : 1.6
Release  : 68
URL      : https://cran.r-project.org/src/contrib/jsonlite_1.6.tar.gz
Source0  : https://cran.r-project.org/src/contrib/jsonlite_1.6.tar.gz
Summary  : A Robust, High Performance JSON Parser and Generator for R
Group    : Development/Tools
License  : MIT
Requires: R-jsonlite-lib = %{version}-%{release}
BuildRequires : R-knitr
BuildRequires : R-testthat
BuildRequires : buildreq-R

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
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1548095183

%install
export SOURCE_DATE_EPOCH=1548095183
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library jsonlite
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library jsonlite
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library jsonlite
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library jsonlite|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/jsonlite/CITATION
/usr/lib64/R/library/jsonlite/DESCRIPTION
/usr/lib64/R/library/jsonlite/INDEX
/usr/lib64/R/library/jsonlite/LICENSE
/usr/lib64/R/library/jsonlite/Meta/Rd.rds
/usr/lib64/R/library/jsonlite/Meta/features.rds
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
/usr/lib64/R/library/jsonlite/doc/json-opencpu.pdf
/usr/lib64/R/library/jsonlite/doc/json-opencpu.pdf.asis
/usr/lib64/R/library/jsonlite/doc/json-paging.Rmd
/usr/lib64/R/library/jsonlite/doc/json-paging.html
/usr/lib64/R/library/jsonlite/help/AnIndex
/usr/lib64/R/library/jsonlite/help/aliases.rds
/usr/lib64/R/library/jsonlite/help/jsonlite.rdb
/usr/lib64/R/library/jsonlite/help/jsonlite.rdx
/usr/lib64/R/library/jsonlite/help/paths.rds
/usr/lib64/R/library/jsonlite/html/00Index.html
/usr/lib64/R/library/jsonlite/html/R.css
/usr/lib64/R/library/jsonlite/tests/testthat.R
/usr/lib64/R/library/jsonlite/tests/testthat/flatten.R
/usr/lib64/R/library/jsonlite/tests/testthat/helper-toJSON.R
/usr/lib64/R/library/jsonlite/tests/testthat/issues.txt
/usr/lib64/R/library/jsonlite/tests/testthat/readme.txt
/usr/lib64/R/library/jsonlite/tests/testthat/test-fromJSON-NA-values.R
/usr/lib64/R/library/jsonlite/tests/testthat/test-fromJSON-array.R
/usr/lib64/R/library/jsonlite/tests/testthat/test-fromJSON-dataframe.R
/usr/lib64/R/library/jsonlite/tests/testthat/test-fromJSON-datasets.R
/usr/lib64/R/library/jsonlite/tests/testthat/test-fromJSON-date.R
/usr/lib64/R/library/jsonlite/tests/testthat/test-fromJSON-matrix.R
/usr/lib64/R/library/jsonlite/tests/testthat/test-libjson-escaping.R
/usr/lib64/R/library/jsonlite/tests/testthat/test-libjson-large.R
/usr/lib64/R/library/jsonlite/tests/testthat/test-libjson-utf8.R
/usr/lib64/R/library/jsonlite/tests/testthat/test-libjson-validator.R
/usr/lib64/R/library/jsonlite/tests/testthat/test-network-Github.R
/usr/lib64/R/library/jsonlite/tests/testthat/test-serializeJSON-S4.R
/usr/lib64/R/library/jsonlite/tests/testthat/test-serializeJSON-datasets.R
/usr/lib64/R/library/jsonlite/tests/testthat/test-serializeJSON-functions.R
/usr/lib64/R/library/jsonlite/tests/testthat/test-serializeJSON-types.R
/usr/lib64/R/library/jsonlite/tests/testthat/test-toJSON-AsIs.R
/usr/lib64/R/library/jsonlite/tests/testthat/test-toJSON-Date.R
/usr/lib64/R/library/jsonlite/tests/testthat/test-toJSON-NA-values.R
/usr/lib64/R/library/jsonlite/tests/testthat/test-toJSON-NULL-values.R
/usr/lib64/R/library/jsonlite/tests/testthat/test-toJSON-POSIXt.R
/usr/lib64/R/library/jsonlite/tests/testthat/test-toJSON-complex.R
/usr/lib64/R/library/jsonlite/tests/testthat/test-toJSON-dataframe.R
/usr/lib64/R/library/jsonlite/tests/testthat/test-toJSON-factor.R
/usr/lib64/R/library/jsonlite/tests/testthat/test-toJSON-keep-vec-names.R
/usr/lib64/R/library/jsonlite/tests/testthat/test-toJSON-logical.R
/usr/lib64/R/library/jsonlite/tests/testthat/test-toJSON-matrix.R
/usr/lib64/R/library/jsonlite/tests/testthat/test-toJSON-numeric.R
/usr/lib64/R/library/jsonlite/tests/testthat/test-toJSON-raw.R
/usr/lib64/R/library/jsonlite/tests/testthat/test-toJSON-zerovec.R
/usr/lib64/R/library/jsonlite/tests/testthat/testS4.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/jsonlite/libs/jsonlite.so
/usr/lib64/R/library/jsonlite/libs/jsonlite.so.avx2
/usr/lib64/R/library/jsonlite/libs/jsonlite.so.avx512
