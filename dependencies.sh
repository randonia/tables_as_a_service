#!/bin/bash
mkdir bin
cd bin
wget https://download.elasticsearch.org/elasticsearch/release/org/elasticsearch/distribution/zip/elasticsearch/2.1.1/elasticsearch-2.1.1.zip
unzip elasticsearch-2.1.1.zip
rm elasticsearch-2.1.1.zip
cd ../