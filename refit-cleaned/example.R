# first install Data Package library (datapkg) found here:
# https://github.com/ropenscilabs/datapkg

# depends on having run `make` to download the data

library(datapkg)

# load dataset into memory

refit <- datapkg_read()

house_1 <- refit$data$house_1.csv
house_2 <- refit$data$house_2.csv
start <- '2013-10-09'
end <- '2013-10-10'

# filter dates

filtered_time_1 <- house_1$Time[house_1$Time > start & house_1$Time < end]
filtered_agg_1 <- house_1$Aggregate[house_1$Time > start & house_1$Time < end]

filtered_time_2 <- house_2$Time[house_2$Time > start & house_2$Time < end]
filtered_agg_2 <- house_2$Aggregate[house_2$Time > start & house_2$Time < end]

# plot subsets of two house measurements

plot(filtered_time_1, filtered_agg_1, type='l', col="red")
lines(filtered_time_2, filtered_agg_2, type='l', col="green")

