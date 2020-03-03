from django.db import models

class List(models.Model):
      id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
      title = models.CharField(db_column='TITLE', max_length=200, blank=True, null=True)  # Field name made lowercase.
      description = models.CharField(db_column='DESCRIPTION', max_length=1000, blank=True, null=True)  # Field name made lowercase.
      created_at = models.DateTimeField(db_column='CREATED_AT', blank=True, null=True)  # Field name made lowercase.
      updated_at = models.DateTimeField(db_column='UPDATED_AT', blank=True, null=True)  # Field name made lowercase.

      class Meta:
          managed = False
          db_table = 'list'
