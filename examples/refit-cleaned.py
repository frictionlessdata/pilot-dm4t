import datetime
import statistics
from datapackage import Package

# Get aggregates
consumption = {}
package = Package('packages/refit-cleaned/datapackage.json')
for resource in package.resources:
    for row in resource.iter(keyed=True):
        hour = row['Time'].hour
        consumption.setdefault(hour, [])
        consumption[hour].append(row['Aggregate'])

# Get averages
for hour in consumption:
    consumption[hour] = statistics.mean(consumption[hour])

# Print results
for hour in sorted(consumption):
    print('Average consumption at %02d hours: %.0f' % (hour, consumption[hour]))
