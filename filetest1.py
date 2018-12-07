# 进行文件夹的增量备份
import os
import filecmp
import shutil
import sys


def auto_backup(scr_dir, dst_dir):
    if (not os.path.isdir(scr_dir)) or (not os.path.isdir(dst_dir)) or (
            os.path.abspath(scr_dir) != scr_dir) or (
            os.path.abspath(dst_dir) != dst_dir):
        for item in os.listdir(scr_dir):
            scr_item = os.path.join(scr_dir, item)
            dst_item = scr_item.replace(scr_dir, dst_dir)
            if os.path.isdir(scr_item):
                # 创建新增的文件夹，保证目标文件夹的结构于原来文件夹一致
                if not os.path.exists(dst_item):
                    os.makedirs(dst_item)
                    print('make directory' + dst_item)
                auto_backup(scr_item, dst_item)

            elif os.path.isfile(scr_item):
                # 只复制新增的或修改过的文件
                if ((not os.path.exists(dst_item)) or (
                        not filecmp.cmp(scr_item, dst_item, shallow=False))):
                    shutil.copyfile(scr_item, dst_item)
                    print('file:' + scr_item + '==>' + dst_item)


def usage():
    print("scr_dir和dst_dir 必须是存于当前的相对目录下")
    print("例如：{0} c:\\olddir c:\\newdir".format(sys.argv[0]))
    sys.exit(0)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        usage()
    scrDir, dstDir = sys.argv[1], sys.argv[2]
    auto_backup(scrDir, dstDir)
