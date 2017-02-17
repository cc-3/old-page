#!/bin/sh
qemu-system-aarch64 -smp 2 -m 1024 -M virt -bios QEMU_EFI.fd -nographic \
       -device virtio-blk-device,drive=image \
       -drive if=none,id=image,file=xenial-server-cloudimg-arm64-uefi1.img \
       -device virtio-blk-device,drive=cloud \
       -drive if=none,id=cloud,file=cloud.img \
       -netdev user,id=user0 -device virtio-net-device,netdev=user0 -redir tcp:2222::22 \
       -cpu cortex-a57