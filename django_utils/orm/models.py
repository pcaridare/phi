from django.contrib.gis.db import models

class Sensor(models.Model):
    pems_id = models.IntegerField(null=True, blank=True)
    freeway = models.CharField(null=True, blank=True, max_length=50)
    direction = models.CharField(null=True, blank=True, max_length=2) # N, S, E, W
    district_id = models.IntegerField(null=True, blank=True)
    county_id = models.IntegerField(null=True, blank=True)
    city_id = models.IntegerField(null=True, blank=True)
    state_pm = models.CharField(null=True, blank=True, max_length=50)
    absolute_pm = models.FloatField(null=True, blank=True)

    location = models.PointField(srid=4326)
    location_dist = models.PointField(srid=900913, null=True, blank=True)
    objects = models.GeoManager()

    sensor_length = models.FloatField(null=True, blank=True)
    sensor_type = models.CharField(null=True, blank=True, max_length=50)
    lanes = models.IntegerField(null=True, blank=True)
    name = models.CharField(null=True, blank=True, max_length=50)
    user_id_1 = models.IntegerField(null=True, blank=True)
    user_id_2 = models.IntegerField(null=True, blank=True)
    user_id_3 = models.IntegerField(null=True, blank=True)
    user_id_4 = models.IntegerField(null=True, blank=True)
    shape_length = models.FloatField(null=True, blank=True)
    shape_area = models.FloatField(null=True, blank=True)
    cnty = models.FloatField(null=True, blank=True)
    taz_id = models.FloatField(null=True, blank=True)
    pop_20 = models.FloatField(null=True, blank=True)
    hh_20 = models.FloatField(null=True, blank=True)
    emp_20 = models.FloatField(null=True, blank=True)
    pop_35 = models.FloatField(null=True, blank=True)
    hh_35 = models.FloatField(null=True, blank=True)
    emp_35 = models.FloatField(null=True, blank=True)
    cnty_1 = models.FloatField(null=True, blank=True)
    taz_id_1 = models.FloatField(null=True, blank=True)
    pop_08 = models.FloatField(null=True, blank=True)
    hh_08 = models.FloatField(null=True, blank=True)
    emp_08 = models.FloatField(null=True, blank=True)

    def location_wgs84(self):
        return self.location.transform(4326, clone=True)

    # Returns the string representation of the model.
    def __unicode__(self):
        return "%s %s" % (self.name, repr(self.location_wgs84().coords))

class Origin(models.Model):
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    cnty = models.FloatField()
    taz_id = models.FloatField()
    pop20 = models.FloatField()
    hh20 = models.FloatField()
    emp20 = models.FloatField()
    pop35 = models.FloatField()
    hh35 = models.FloatField()
    emp35 = models.FloatField()
    cnty_1 = models.FloatField()
    taz_id_1 = models.FloatField()
    pop08 = models.FloatField()
    hh08 = models.FloatField()
    emp08 = models.FloatField()
    geom = models.PolygonField(srid=4326)
    geom_dist = models.PolygonField(srid=900913, null=True, blank=True)
    objects = models.GeoManager()

# Auto-generated `LayerMapping` dictionary for Origin model
origin_mapping = {
    'shape_leng' : 'Shape_Leng',
    'shape_area' : 'Shape_Area',
    'cnty' : 'CNTY',
    'taz_id' : 'TAZ_ID',
    'pop20' : 'POP20',
    'hh20' : 'HH20',
    'emp20' : 'EMP20',
    'pop35' : 'POP35',
    'hh35' : 'HH35',
    'emp35' : 'EMP35',
    'cnty_1' : 'CNTY_1',
    'taz_id_1' : 'TAZ_ID_1',
    'pop08' : 'POP08',
    'hh08' : 'HH08',
    'emp08' : 'EMP08',
    'geom' : 'POLYGON',
}