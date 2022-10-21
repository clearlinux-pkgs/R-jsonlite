#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-jsonlite
Version  : 1.8.3
Release  : 108
URL      : https://cran.r-project.org/src/contrib/jsonlite_1.8.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/jsonlite_1.8.3.tar.gz
Summary  : A Simple and Robust JSON Parser and Generator for R
Group    : Development/Tools
License  : MIT
Requires: R-jsonlite-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
data and the web. Offers simple, flexible tools for working with JSON in R, and
    is particularly powerful for building pipelines and interacting with a web API. 
    The implementation is based on the mapping described in the vignette (Ooms, 2014).
    In addition to converting JSON data from/to R objects, 'jsonlite' contains 
    functions to stream, validate, and prettify JSON data. The unit tests included 
    with the package verify that all edge cases are encoded and decoded consistently 
    for use with dynamic data in systems and applications.

%package lib
Summary: lib components for the R-jsonlite package.
Group: Libraries

%description lib
lib components for the R-jsonlite package.


%prep
%setup -q -n jsonlite
cd %{_builddir}/jsonlite

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1666366135

%install
export SOURCE_DATE_EPOCH=1666366135
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


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
/usr/lib64/R/library/jsonlite/tests/testthat/test-toJSON-sf.R
/usr/lib64/R/library/jsonlite/tests/testthat/test-toJSON-zerovec.R
/usr/lib64/R/library/jsonlite/tests/testthat/test_rbind_pages.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/jsonlite/libs/jsonlite.so
/usr/lib64/R/library/jsonlite/libs/jsonlite.so.avx2
/usr/lib64/R/library/jsonlite/libs/jsonlite.so.avx512
