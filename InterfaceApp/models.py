from django.db import models
from django.contrib.auth.models import User

class PerformanceDB(models.Model):
    seq = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    startDate = models.DateField()
    endDate = models.DateField()
    place = models.CharField(max_length=50)
    realmName = models.CharField(max_length=10)
    area = models.CharField(max_length=10, null=True)
    thumbnail = models.BinaryField()
    gpsX = models.FloatField(null=True)
    gpsY = models.FloatField(null=True)
    site = models.URLField(null=True)

    def __str__(self):
        return f"seq: {self.seq}, title: {self.title}, startDate: {self.startDate}, endDate: {self.endDate}, place: {self.place}, realmName: {self.realmName}, area: {self.area}, thumbnail: {self.thumbnail}, gpsX: {self.gpsX}, gpsY: {self.gpsY}, site: {self.site}"

class WishlistDB(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column="user_id")
    performance_seq = models.ForeignKey(PerformanceDB, on_delete=models.CASCADE, db_column="performance_seq")