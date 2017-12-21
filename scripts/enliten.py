from elasticsearch import Elasticsearch
from datapackage import Package
from tableschema_elasticsearch import Storage

package = Package('datasets/enliten/datapackage.json')
resource = package.get_resource('power')
print(resource.descriptor)

engine=Elasticsearch()
storage=Storage(engine)

storage.create('enliten', [('power', resource.schema.descriptor)])
