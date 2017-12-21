# Add license information
# modified from: https://github.com/frictionlessdata/datapackage-pipelines/blob/4afffbeb4e5ce9f6646ce9d07e8cac119f87d912/datapackage_pipelines/lib/set_types.py

import re
from datapackage_pipelines.wrapper import process
from datapackage_pipelines.utilities.resource_matcher import ResourceMatcher

def match_fields(field_name_re, expected):
    def filt(field):
        return (field_name_re.fullmatch(field['name']) is not None) is expected
    return filt

def modify_datapackage(datapackage, parameters, stats):
    descriptions = parameters.get('descriptions', {})
    resources = ResourceMatcher(parameters.get('resources'))
    for resource in datapackage['resources']:
        name = resource['name']
        if not resources.match(name):
            continue
        fields = resource.setdefault('schema', {}).get('fields', [])
        for field_name, field_description in descriptions.items():
            field_name_re = re.compile(field_name)
            if field_description is not None:
                filtered_fields = list(
                    filter(match_fields(field_name_re, True), fields)
                )
                for field in filtered_fields:
                    field.update(field_description)
                assert len(filtered_fields) > 0, \
                    "No field found matching %r" % field_name
        resource['schema']['fields'] = fields
    return datapackage

process(modify_datapackage=modify_datapackage)
