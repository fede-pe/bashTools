# This bash script copies files from different folders with colliding names and rename them
# Usage:
# copyRename.sh fileNameRoot copyFilesQuery

FILENAME_EXTENSION='.mrc';
COUNTER=0;


for FILE in "${@:2}";
do
	echo "cp $FILE $1_$COUNTER$FILENAME_EXTENSION";
	cp $FILE $1_$COUNTER$FILENAME_EXTENSION;
	COUNTER=$[$COUNTER +1];
done
