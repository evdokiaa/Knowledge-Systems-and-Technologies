import sys, os
import itertools, operator
import numpy as np
import readline
from pylab import rcParams


stops=open('stop_times.txt', 'r')
rdf_file = open('rdf-stoptimes.txt' , 'a')
stops.readline()

for line in stops:
    line=line.split(',')

    trip_id = line[0]
    arrival_time = line[1]
    departure_time = line[2]
    stop_id = line[3]
    stop_sequence = line[4]
    stoptime_id = trip_id+'-'+stop_id
 

    rdf1 = '<owl:NamedIndividual rdf:about="http://www.semanticweb.org/myOntology#' + stoptime_id + '"> \n'
    rdf2=  '      <rdf:type rdf:resource="http://www.semantciweb.org/myOntology#Stop-Time"/>' + '\n'
    rdf3 = '      <StopOnRoute rdf:resource="http://www.semanticweb.org/myOntology#'+ trip_id +'"/>' + '\n'
    rdf4 = '      <isStop rdf:resource="http://www.semanticweb.org/myOntology#'+ stop_id+'"/>' + '\n'
    rdf5 = '      <Arrival>' +arrival_time + '</Arrival>\n'
    rdf6 = '      <Departure>' +departure_time + '</Departure>\n'
    rdf7 = '</owl:NamedIndividual>\n \n '
    rdf=rdf1+rdf2+rdf3+rdf4+rdf5+rdf6+rdf7
    rdf_file.write(rdf)

rdf_file.write('</rdf:RDF>')

stops.close()
rdf_file.close()
