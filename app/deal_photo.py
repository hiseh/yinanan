import hashlib
import mimetypes
import os
import shutil
import sys
import uuid

from PIL import Image

from tps.converter import FFMpeg

__author__ = 'hiseh'
__datetime__ = 2017 / 2 / 6

PHOTO_TYPE = {'image', 'video'}


class Photo:
    @staticmethod
    def clear_up(original, aim):
        """
        根据日期整理图片
        :param original:
        :param aim:
        :return:
        """
        Photo.remove_unphoto(original)
        for root, _, files in os.walk(original):
            for file in files:
                original_path = '{root}/{file}'.format(root=root, file=file)
                file_ctime = Photo.getctime(original_path)
                aim_path = '{root}/{path}'.format(root=aim,
                                                  path=file_ctime)
                try:
                    os.makedirs(aim_path)
                except OSError:
                    pass

                try:
                    shutil.move(original_path, aim_path)
                    print('moved', original_path, 'to', aim_path)
                except shutil.Error:
                    original_md5 = Photo.md5_file(original_path)
                    aim_md5 = Photo.md5_file('{root}/{file}'.format(root=aim_path, file=file))
                    if original_md5 == aim_md5:
                        os.remove(original_path)
                        print('removed the same file\t', original_path)
                    else:
                        file_list = os.path.splitext(file)
                        new_path = '{path}/{file}'.format(path=aim_path,
                                                          file=''.join((file_list[0] + '_' + uuid.uuid4().hex,
                                                                        file_list[1])))
                        shutil.move(original_path, new_path)
                        print('renamed', original_path, 'to', new_path)

    @staticmethod
    def remove_unphoto(path):
        """
        删掉非图片和视频文件
        :param path:
        :return:
        """
        for root, _, files in os.walk(path):
            for file in files:
                file_path = '{root}/{file}'.format(root=root, file=file)
                try:
                    file_type = os.path.split(mimetypes.guess_type(file_path)[0])[0]
                    if file_type not in PHOTO_TYPE:
                        raise AttributeError
                except AttributeError:
                    try:
                        os.remove(file_path)
                        print('removed', file_path)
                    except OSError:
                        pass

    @staticmethod
    def remove_repeat(path):
        """
        删除重复图片
        :param path:
        :return:
        """
        unique_files = set()
        for root, _, files in os.walk(path):
            for file in files:
                file_path = '{root}/{file}'.format(root=root, file=file)
                file_md5 = Photo.md5_file(file_path)
                if file_md5 in unique_files:
                    try:
                        os.remove(file_path)
                        print('removed', file_path)
                    except OSError:
                        pass
                else:
                    print('\tunique file', file_path)
                    unique_files.add(file_md5)

    @staticmethod
    def getctime(file):
        """
        获取创建日期
        :param file:
        :return:
        """
        ctime = None
        try:
            file_type = os.path.split(mimetypes.guess_type(file)[0])[0]
            ctime = {'image': lambda f: Photo._image_ctime_(f),
                     'video': lambda f: Photo._video_ctime_(f)}[file_type](file)
        except AttributeError:
            pass
        finally:
            return ctime

    @staticmethod
    def _image_ctime_(file):
        img = Image.open(file)
        exif_data = img._getexif()[36867]
        return ''.join(exif_data[0:7].split(':'))

    @staticmethod
    def _video_ctime_(file):
        f = FFMpeg()
        info = f.probe(file)
        return ''.join(info.video.metadata['creation_time'][0:7].split('-'))

    @staticmethod
    def md5_file(file_path):
        hash_md5 = hashlib.md5()
        try:
            with open(file_path, "rb") as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hash_md5.update(chunk)
            return hash_md5.hexdigest()
        except FileNotFoundError:
            return None

if __name__ == '__main__':
    args = sys.argv[1:]
    if '-?' in args:
        print('一个整理照片/视频的脚本\n'
              '能够根据照片和视频的拍摄日期自动归纳整理到相应月份文件夹里，如果有同名照片/视频，'
              '可以判断内容是否一样，不一样的话，会改名保存\n'
              '-mv moving files python deal_photo.py -mv original_path aim_path\n'
              '-cl cleaning up repeat files python deal_photo.py -cl path')
    elif '-mv' in args:
        Photo.clear_up(original=args[1], aim=args[2])
    elif '-cl' in args:
        Photo.remove_repeat(args[1])
