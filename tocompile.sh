make clean
export F77=/usr/bin/gfortran
export CPPFLAGS="-I. -I/home/sagnikd/Libraries/libunwind/include -I/home/sagnikd/Libraries/binutils/include -I/home/sagnikd/Libraries/binutils/include/libiberty -I/home/sagnikd/Libraries/mpich-install/include"
export LDFLAGS="-L/home/sagnikd/Libraries/libunwind/lib -lunwind -L/home/sagnikd/Libraries/binutils/lib -lbfd -liberty -L/home/sagnikd/Libraries/mpich-install/lib"
export LIBS="-ldl"
./configure --with-binutils-dir=/home/sagnikd/Libraries/binutils --with-libunwind=/home/sagnikd/Libraries/libunwind --prefix=/home/sagnikd/Libraries/mpiPV --enable-demangling=GNU --enable-stackdepth=15
