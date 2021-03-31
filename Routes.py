import sys, os
import itertools, operator
import numpy as np
import readline
from pylab import rcParams


routes=open('routes.txt', 'r')
rdf_file = open('rdf-routes-short.txt' , 'a')
routes.readline()

for line in range(100):
    line = routes.readline()
    line=line.split(',')

    route_id = line[0]
    route_short_name = line[1]
    route_long_name=line[2]
    route_type=line[4]

    print(route_id ,route_short_name , route_long_name) 

    rdf1 = '<owl:NamedIndividual rdf:about="http://www.semanticweb.org/myOntology#' + route_id + '"> \n'
    rdf2=  '      <rdf:type rdf:resource="http://www.semantciweb.org/myOntology#Route"/>' + '\n'
    rdf3 = '      <LongName>' +route_long_name + '</LongName>\n'
    rdf4 = '      <RouteType rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">' +route_type +'</RouteType>\n' 
    rdf5 = '      <ShortName>' +route_short_name + '</ShortName>\n'
    rdf6 = '</owl:NamedIndividual>\n \n '
    rdf=rdf1+rdf2+rdf3+rdf4+rdf5+rdf6
    rdf_file.write(rdf)

routes.close()
rdf_file.close()
