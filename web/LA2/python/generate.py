import csv
import operator
import json
from django.contrib.gis.geos import GEOSGeometry

polylines = {}
for row in csv.DictReader(open('/var/www/LA2/data/routes.csv'), delimiter='#'):
  ot = row['origin_taz']
  dt = row['destination_taz']
  pl = row['route']
  
  if not ot in polylines:
    polylines[ot] = {}
  if not dt in polylines[ot]:
    polylines[ot][dt] = []
  polylines[ot][dt].append(GEOSGeometry(pl))

routes = {}
for row in csv.DictReader(open('/var/www/LA2/data/trips.csv'), delimiter=','):
  ot = row['origin']
  dt = row['destination']
  t = float(row['trips'])
  
  if not ot in routes:
    routes[ot] = {}
  if not dt in routes[ot]:
    routes[ot][dt] = t

data = {}
# Only keep the top 10 destinations for each origin
for o in routes:
  for d, value in sorted(routes[o].iteritems(), key=operator.itemgetter(1), reverse=True)[:20]:
    if not o in data:
      data[o] = {}
    if not d in data[o]:
      data[o][d] = {}
    polys = []
    for p in polylines[o][d]:
      p.srid = 900913
      p.transform(4326)
      polys.append(p.coords)
    data[o][d] = {'value': value, 'polys': polys}

json.dump(data, open('/var/www/LA2/data/data.json', 'w'))
