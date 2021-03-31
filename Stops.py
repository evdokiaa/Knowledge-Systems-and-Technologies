import sys, os
import itertools, operator
import numpy as np
import readline
from pylab import rcParams


stops=open('stops.txt', 'r')
rdf_file = open('rdf-stops.txt' , 'a')
stops.readline()

for line in stops:
    line=line.split(',')

    stop_id = line[0]
    stop_name = line[2]
    longtitude = line[4]
    lattitude = line[5]
    stop_coordinates = 'POINT('+longtitude+' '+lattitude+')' 

    rdf1 = '<owl:NamedIndividual rdf:about="http://www.semanticweb.org/myOntology#' + stop_id + '"> \n'
    rdf2=  '      <rdf:type rdf:resource="http://www.semantciweb.org/myOntology#Stop"/>' + '\n'
    rdf3 = '      <Coordinates rdf:datatype="http://www.openlinksw.com/schemas/virtrdf#Geometry">' +stop_coordinates + '</Coordinates>\n'
    rdf5 = '      <StopName>' +stop_name + '</StopName>\n'
    rdf6 = '</owl:NamedIndividual>\n \n '
    rdf=rdf1+rdf2+rdf3+rdf5+rdf6
    rdf_file.write(rdf)

stops.close()
rdf_file.close()
