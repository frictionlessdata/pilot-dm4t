all: archive/Processed_Data_CSV.7z
	mkdir -p data/
	7z x archive/Processed_Data_CSV.7z -aos -odata/ 

archive/Processed_Data_CSV.7z:
	mkdir -p archive/
	curl -o archive/Processed_Data_CSV.7z "https://pure.strath.ac.uk/portal/files/52873459/Processed_Data_CSV.7z"

clean:
	rm -r archive/ data/
