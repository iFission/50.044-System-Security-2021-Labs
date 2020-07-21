#!/bin/sh

# Download and install phantomjs; 
if [ ! -e "$HOME/phantomjs" ]; then
  echo "One moment, Unpacking PhantomJS..."
  tar -xjf phantomjs.tar.bz2
  mv "phantomjs" "$HOME"
  echo "Done"
fi
