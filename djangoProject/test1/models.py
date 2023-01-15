# Create your models here.
#onetoonefield（类名，ondete）外键，级联删除
from django.db import models
# Create your models here.

class datainfo(models.Model):
    date=models.DateField('日期',max_length=30,default='',unique=True) #主键
    imagesrc=models.CharField('传感器类型',max_length=30,default='')
    imagename=models.CharField('影像名称',max_length=50,default='')

    class Meta:
        db_table='image_data'
    def __str__(self):
        return '%s|%s|%s'%(self.date,self.imagesrc,self.imagename)