from django.db import models


# 新增：指定上传路径（图片会存在 media/images/ 下）
def image_upload_path(instance, filename):
    return f'images/{filename}'


class Movie(models.Model):
    title = models.CharField(max_length=200, verbose_name='网文名称')
    category = models.CharField(max_length=100, verbose_name='分类')
    link = models.URLField(verbose_name='下载链接')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    description = models.TextField(blank=True, null=True, verbose_name='简介')
    score = models.FloatField(default=0, verbose_name='评分')

    # 替换原 image_path（如果之前有这个字段就替换，没有就直接新增）
    image = models.ImageField(upload_to=image_upload_path, blank=True, verbose_name='封面图')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '网文'
        verbose_name_plural = '网文列表'
        ordering = ['-update_time']