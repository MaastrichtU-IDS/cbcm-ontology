from owlready2 import *
import csv

onto = get_ontology("working_copy/eu-cm-ontology.owl").load()

def process(entities):
    newEntities = []
    for e in entities:
        if "org." in str(e):
            newEntities.append(str(e).replace("org.","cbcm:"));
        else:
            newEntities.append(str(e).replace("eu-cm-ontology.","cbcm:"));
    return newEntities

classes = process(list(onto.classes()))
object_properties = process(list(onto.object_properties()))
data_properties = process(list(onto.data_properties()))

entities = []
entities.extend(classes)
entities.extend(object_properties)
entities.extend(data_properties)

with open("working_copy/cbcm_ontology_terms_flatlist.csv", 'w', newline='') as myfile:
    writer = csv.writer(myfile)
    for val in entities:
        writer.writerow([val])
