import os
import shutil
paths="./root/"
ss='genisoimage -o disk.iso -input-charset utf-8 -b "isolinux/isolinux.bin" -no-emul-boot -boot-load-size 4  -boot-info-table "./root" '
print(ss)
os.system(ss)
