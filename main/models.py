from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
class Home(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False) 
    name = models.CharField(max_length=100)#집이름
    images = models.ImageField(blank=True, upload_to="images", null=True)#방이미지
    deposit = models.FloatField(default=0.0)
    Monthly_rent = models.FloatField(default=0.0)#월세
    administration_cost = models.FloatField(default=0.0)#관리비
    room = models.CharField(max_length=30)#방종류
    floor = models.FloatField(default=0.0)#건물층
    hitter = models.CharField(max_length=20)#난방종류
    parking = models.FloatField(default=0.0)#주차여부
    Veranda = models.CharField(max_length=30)#베란다여부
    address = models.CharField(max_length=40)#주소
    number = models.CharField(max_length=11)#연락처
    distance = models.CharField(max_length=30)#통학거리
    option = models.TextField()#옵션
    


    #foreignkey 설정할 때 web에서 primary key의 name으로 보여주게됨. but db에는 id로 저장됨
    #아니면 primary key 그대로 1번 2번 이렇게 보임. 
    def __str__(self):
        return self.name

class Comment(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=True)
    home = models.ForeignKey(Home, null=False, blank=False, on_delete=models.CASCADE)
    user = models.CharField(max_length=4)#ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True, null=False, blank=False)
    comment = models.TextField()
    clean = models.FloatField(default=0.0)
    hit = models.FloatField(default=0.0)
    noise = models.FloatField(default=0.0)
    optionrate = models.FloatField(default=0.0)
    secu = models.FloatField(default=0.0)
    day_light = models.FloatField(default=0.0)
    
    

    def __str__(self):
        return self.comment
    
    

class Rating(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=True)
    homes = models.ForeignKey(Home, null=False, blank=False, on_delete=models.CASCADE)
    ave = models.FloatField(default=0.0)