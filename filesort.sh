#!/bin/bash
SORTDIR=$1
WORKDIR=$2

filesort() {
for file in $SORTDIR/*
do
  MODYEAR=$(date -r $file +%Y)
  MODMONTH=$(date -r $file +%m)
  MODDAY=$(date -r $file +%d)
  DIRNAM="$MODYEAR-$MODMONTH-$MODDAY"
  FILENAM=$(basename $file)
  if [[ -d "$WORKDIR/$DIRNAM" ]]; then
    cp $file "$WORKDIR/$DIRNAM/$FILENAM"
    echo "$file copied to $WORKDIR/$DIRNAM/$FILENAM"
  else
    mkdir "$WORKDIR/$DIRNAM"
    echo "$DIRNAM created"
    cp $file "$WORKDIR/$DIRNAM/$FILENAM"
    echo "$file copied to $WORKDIR/$DIRNAM/$FILENAM"
  fi
done
}

if [[ -z "$SORTDIR" || -z "$WORKDIR" ]]; then
  echo "Sorting and working directories need to be specified!"
else
  filesort
fi
