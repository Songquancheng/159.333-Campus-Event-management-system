from django.db import models
from django.contrib.auth.models import User




class Activity(models.Model):
    STATUS = (
        ('checking', '审核中'),
        ('upcoming', '即将开始'),
        ('ongoing', '进行中'),
        ('ended', '已结束'),
    )

    name = models.CharField(max_length=100)
    time = models.DateTimeField()
    location = models.CharField(max_length=200)
    organizer = models.ForeignKey('Organizer', on_delete=models.SET_NULL, null=True, related_name='activities')
    description = models.TextField()
    QR = models.ImageField(upload_to='qr_codes/', null=True, blank=True)
    ticket = models.ImageField(upload_to='tickets/', null=True, blank=True)
    feedback = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default='checking')


    def __str__(self):
        return self.name

class Participation(models.Model):
    STATUS = (
        ('waiting', '等待中'),
        ('ongoing', '进行中'),
        ('ended', '已结束'),
    )

    student = models.ForeignKey('Student', on_delete=models.CASCADE, related_name='participations')
    activity = models.ForeignKey('Activity', on_delete=models.CASCADE, related_name='participants')
    status = models.CharField(max_length=10, choices=STATUS, default='waiting')
    jointime = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'activity')

    def __str__(self):
        return f"{self.student.name} - {self.activity.name}"

class Student(models.Model):
    GENDER = (
        ('M', '男'),
        ('F', '女'),
        ('O', '其他'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=GENDER)
    age = models.IntegerField()

    def __str__(self):
        return self.user.username

class Organizer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.user.username

class Attendant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


#charfield 字符串   DateTimefield 日期  InterField 数字
#textfield 长文本   ImageField 图片路径 ForeignKey 与其他class关联