# 1. compile usw
## 1. command
 ./run configs/polaris_ppu_multicore_sle_uboot.py -j96
## 2. copy to u-boot
build/configs/polaris_ppu_multicore_sle_uboot/ppu_arm0/ppu_arm0.strip
build/configs/polaris_ppu_multicore_sle_uboot/ppu_arm_bios/ppu_arm_bios.strip
# 2. compile u-boot
## 1. command
