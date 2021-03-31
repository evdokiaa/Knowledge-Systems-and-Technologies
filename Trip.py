import sys, os
import itertools, operator
import numpy as np
import readline
from pylab import rcParams

trips=open('trips.txt', 'r')
rdf_file = open('rdf-trips.txt' , 'a')
trips.readline()

for line in trips:
    line=line.split(',')

    route_id = line[0]
    trip_id = line[2]
    direction=line[4]

    print(route_id ,trip_id , direction) 

    rdf1 = '<owl:NamedIndividual rdf:about="http://www.semanticweb.org/myOntology#' + trip_id + '"> \n'
    rdf2=  '      <rdf:type rdf:resource="http://www.semantciweb.org/myOntology#Trip"/>' + '\n'
    rdf3 = '      <TripOnRoute rdf:resource="http://www.semanticweb.org/myOntology#' +route_id +'"/>' + '\n'
    rdf4 = '      <Direction rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">' +direction +'</Direction>\n' 
    rdf5 = '</owl:NamedIndividual>\n \n '
    rdf=rdf1+rdf2+rdf3+rdf4+rdf5
    rdf_file.write(rdf)

trips.close()
rdf_file.close()


