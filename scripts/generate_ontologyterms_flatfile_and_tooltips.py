#!/usr/bin/env python
# coding: utf-8
from owlready2 import *
import csv

# import and parse the OWL ontology
onto = get_ontology("working_copy/eu-cm-ontology.owl").load()

# get classes, object properties and data properties
classes = list(onto.classes())
object_properties = list(onto.object_properties())
data_properties = list(onto.data_properties())

# gather classes and properties into one set of entities
entities = []
entities.extend(classes)
entities.extend(object_properties)
entities.extend(data_properties)

# write flat list of ontology entities to file - with prefix abbreviation "cbcm:"
with open("working_copy/cbcm_ontology_terms_flatlist.csv", 'w', newline='') as flatlistfile:
    writer = csv.writer(flatlistfile)
    for entity in entities:
        entityNameParts = str(entity).split(".")
        entityName = "cbcm:" + entityNameParts[1]
        writer.writerow([entityName])

# write mapping file of ontology entities to human-readable labels and human-readable definitions (candidates for tooltip texts)
with open("working_copy/cbcm_ontology_terms_tooltip_texts.csv", 'w', newline='') as tooltipsfile:
    writer = csv.writer(tooltipsfile, quotechar='"', quoting=csv.QUOTE_ALL)
    writer.writerow(["ontology_term","ontology_term_label","ontology_term_definition"])
    for entity in entities:
        entityNameParts = str(entity).split(".")
        entityName = "cbcm:" + entityNameParts[1]
        entityComment = "None"
        entityLabel = "None"
        if (len(entity.comment) > 0):
            entityComment = entity.comment[0]
        if (len(entity.label) > 0):
            entityLabel = entity.label[0]
        writer.writerow([entityName,entityLabel,entityComment])

