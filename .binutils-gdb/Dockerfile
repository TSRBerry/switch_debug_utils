FROM devkitpro/devkitarm as dkparm
FROM devkitpro/devkita64 as dkparm64

COPY --from=dkparm /opt/devkitpro /opt/devkitpro

ARG MAKE_JOBS=2

ARG DEBIAN_FRONTEND=noninteractive

# install all required packages
RUN apt update && apt upgrade -y \
    && apt install -y \
        make git-core cmake python3-dev build-essential wget \
        bison flex libncurses5-dev libreadline-dev texinfo pkg-config \
        python3-pip python3-setuptools libglib2.0-dev libc6-dbg \
        autotools-dev automake autoconf liblz4-dev libelf-dev \
        libtinfo5 \
        libgmp-dev libmpfr-dev libmpc-dev mesa-common-dev libfreeimage-dev \
        zlib1g-dev libusb-dev libudev-dev libexpat1-dev \
        xz-utils bzip2 \
    && apt clean -y && rm -rf /var/lib/apt/lists/*

# prepare devkitpro env
WORKDIR /root
ENV DEVKITPRO=/opt/devkitpro
ENV DEVKITARM=/opt/devkitpro/devkitARM
ENV DEVKITPPC=/opt/devkitpro/devkitPPC
ENV PATH=${DEVKITPRO}/tools/bin:${DEVKITPRO}/devkitA64/bin:${DEVKITARM}/bin:${PATH}

RUN git clone https://github.com/devkitPro/binutils-gdb -b devkitA64 \
    && cd binutils-gdb \
    && ./configure --with-python=/usr/bin/python3 --prefix=/opt/devkitpro/devkitA64 --target=aarch64-none-elf \
    && make -j ${MAKE_JOBS} && make install

RUN cd binutils-gdb \
    && make clean && git checkout -B devkitARM-gdb --track origin/devkitARM-gdb -f \
    && ./configure --with-python=/usr/bin/python3 --prefix=/opt/devkitpro/devkitARM --target=arm-none-eabi \
    && make -j ${MAKE_JOBS} && make install

ENTRYPOINT [ "/bin/bash" ]
