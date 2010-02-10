from archetypes.schemaextender.field import ExtensionField
from archetypes.schemaextender.interfaces import ISchemaExtender, ISchemaModifier
from Products.Archetypes.atapi import *
from zope.interface import implements, Interface
from zope.component import adapts, provideAdapter

from Products.FacultyStaffDirectory.interfaces.person import IPerson


# Any field you tack on must have ExtensionField as its first subclass:
class _StringExtensionField(ExtensionField, StringField):
    pass


# Add fields for a fax number and the campus the person is located at
# Add fields for use in building the data file for the Building Directory computers
class addSleicFields(object):
    """Adapter that adds a campus field to Person."""
    adapts(IPerson)
    implements(ISchemaExtender)

    _fields = [
            _StringExtensionField('campus',
                required=False,
                searchable=True,
                schemata="Contact Information",
                widget=MultiSelectionWidget(
                    label=u"Campus",
                    description=u"Campus name",
                    format="checkbox"
                ),
                enforceVocabulary=True,
                vocabulary=[
                    ("University Park", "University Park"),
                    ("Hershey", "Hershey"),
                ]
            ),
        ]


    def __init__(self, context):
        self.context = context
    
    def getFields(self):
        return self._fields


# Change the wording and order of a few fields; hide fields that will not be used
class modifySleicFields(object):
    adapts(IPerson)
    implements(ISchemaModifier)

    def __init__(self, context):
        self.context = context

    from Products.FacultyStaffDirectory.Person import schema

    def fiddle(object, schema):

        # move some fields around
        schema.moveField('education', before='jobTitles')
        schema.moveField('websites', after='classifications')
        schema.moveField('campus', before='officeAddress')


        # define some new labels to use
        labels = { 'biography': 'Responsibilities / Research interests',
                   'classifications': 'Choose a categroy that best describes you',
                   'websites': 'Other websites about you',
                   'officeAddress': 'Office Address (room and building)' }
        
        # define some new descriptions to use
        descriptions = { 'education': 'One degree per line. Example: PhD (1995) Penn State: Subject area or thesis title',
                         'firstName': 'Required',
                         'id': 'Required. Example: abc123 (the part of your default Penn State email address before @psu.edu)',
                         'image': 'You can upload an image up to 200px wide by 250px high',
                         'lastName': 'Required',
                         'specialities': 'Browse to choose one or more areas where you have expertise or research interests. Note: some areas have sub-areas you can select (e.g. cognitive neuroscience is a sub-area of neuroscience).',
                         'websites': 'You can specify one or more websites (one per line) that people can go to read more about you, for instance, your departmental web page and/or lab website. Example: http://www.example.com/' }

        # define some fields to hide
        hideFields = { 'officeCity': { 'edit': 'invisible', 'view': 'invisible' },
                       'officeState': { 'edit': 'invisible', 'view': 'invisible' },
                       'officePostalCode': { 'edit': 'invisible', 'view': 'invisible' },
                       'committees': { 'edit': 'invisible', 'view': 'invisible' } }
        
        # define some schemata to hide from all but the Managers
        hiddenSchemata = ['categorization', 'dates', 'ownership', 'settings']
        
        
        
        # update the labels
        for index, value in labels:
            new_field = schema[index].copy()
            new_field.widget.label = value
            schema[index] = new_field
            
        # update the descriptions
        for index, value in descriptions:
            new_field = schema[index].copy()
            new_field.widget.description = value
            schema[index] = new_field
            
        # hide the fields
        for index, value in hideFields:
            new_field = schema[index].copy()
            new_field.widget.visible = value
            schema[index] = new_field
            

        # hide the schemata
        for schemata in hiddenSchemata:
            for fieldName in schema.getSchemataFields(schemata):
                fieldName.widget.condition="python:member.has_role('Manager')"
                

        return schema
