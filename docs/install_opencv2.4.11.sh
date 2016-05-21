#! /bin/bash -x
#sudo yum install -y gcc g++ gtk+-devel libjpeg-devel libtiff-devel jasper-devel libpng-devel zlib-devel cmake unzip
#sudo yum install -y yum-priorities
#wget http://ftp-srv2.kddilabs.jp/Linux/distributions/fedora/epel/6/x86_64/epel-release-6-8.noarch.rpm
#sudo rpm -ivh epel-release-6-8.noarch.rpm
#sudo yum install -y eigen3-devel —enablerepo=epel
#pip install numpy

#wget http://downloads.sourceforge.net/project/opencvlibrary/opencv-unix/2.4.11/opencv-2.4.11.zip
#unzip opencv-2.4.11
cd opencv-2.4.11
mkdir build
cd build
export PYTHON_EXECUTABLE=$(readlink -e $(which python))
export PYTHON_INCLUDE_PATH=${PYTHON_EXECUTABLE%/*/*}/include
export PYTHON_LIBRARY=${PYTHON_EXECUTABLE%/*/*}/lib/libpython2.7.a
export PYTHON_NUMPY_INCLUDE_DIR=${PYTHON_EXECUTABLE%/*/*}/lib/python2.7/site-packages/numpy/core/include/numpy
export PYTHON_PACKAGES_PATH=${PYTHON_EXECUTABLE%/*/*}/lib/python2.7/site-packages
cmake  \
-DBUILD_DOCS=OFF  \
-DBUILD_EXAMPLES=OFF  \
-DBUILD_JPEG=OFF  \
-DBUILD_OPENEXR=OFF  \
-DBUILD_PACKAGE=OFF  \
-DBUILD_PERF_TESTS=OFF  \
-DBUILD_PNG=OFF  \
-DBUILD_SHARED_LIBS=OFF  \
-DBUILD_TBB=OFF  \
-DBUILD_TESTS=OFF  \
-DBUILD_TIFF=OFF  \
-DBUILD_WITH_DEBUG_INFO=OFF  \
-DBUILD_ZLIB=OFF  \
-DWITH_1394=ON  \
-DWITH_EIGEN=ON  \
-DWITH_FFMPEG=ON  \
-DWITH_GIGEAPI=ON  \
-DWITH_GSTREAMER=ON  \
-DWITH_GTK=ON  \
-DWITH_IPP=OFF  \
-DWITH_JASPER=ON  \
-DWITH_JPEG=ON  \
-DWITH_LIBV4L=ON  \
-DWITH_OPENCL=OFF  \
-DWITH_OPENCLAMDBLAS=OFF  \
-DWITH_OPENCLAMDFFT=OFF  \
-DWITH_OPENEXR=OFF  \
-DWITH_OPENGL=OFF  \
-DWITH_OPENMP=OFF  \
-DWITH_OPENNI=OFF  \
-DWITH_PNG=ON  \
-DWITH_PVAPI=OFF  \
-DWITH_QT=OFF  \
-DWITH_TBB=OFF  \
-DWITH_TIFF=ON  \
-DWITH_UNICAP=OFF  \
-DWITH_V4L=OFF  \
-DWITH_XIMEA=OFF  \
-DWITH_XINE=OFF  \
-DPYTHON_EXECUTABLE=$PYTHON_EXECUTABLE  \
-DPYTHON_INCLUDE_PATH=$PYTHON_INCLUDE_PATH \
-DPYTHON_LIBRARY=$PYTHON_LIBRARY \
-DPYTHON_NUMPY_INCLUDE_DIR=$PYTHON_NUMPY_INCLUDE_DIR \
-DPYTHON_PACKAGES_PATH=$PYTHON_PACKAGES_PATH \
-Wno-dev ../
make
sudo make install
