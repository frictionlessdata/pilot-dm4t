from elasticsearch import Elasticsearch
from datapackage import Package
from tableschema_elasticsearch import Storage

# Get resource
package = Package('packages/refit-cleaned/datapackage.json')
resource = package.get_resource('house-1')

# Create storage
engine=Elasticsearch()
storage=Storage(engine)

# Write data
storage.create('refit-cleaned', [('house-1', resource.schema.descriptor)])
list(storage.write('refit-cleaned', 'house-1', resource.read(keyed=True), ['Unix']))
