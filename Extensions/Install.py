from Products.FacultyStaffDirectory.extenderInstallation import declareInstallRoutines
from Products.sleicPersonExtender.person import addSleicFields
from Products.sleicPersonExtender.person import modifySleicFields

def install(portal):
    """Register the extender so it takes effect on this Plone site."""
    sm = portal.getSiteManager()
    sm.registerAdapter(addSleicFields, name='sleicPersonExtender-addSleicFields')
    sm.registerAdapter(modifySleicFields, name='sleicPersonExtender-modifySleicFields')
    
    return "Registered the extender at the root of the Plone site."

def uninstall(portal):
    sm = portal.getSiteManager()
    sm.unregisterAdapter(addSleicFields, name='sleicPersonExtender-addSleicFields')
    sm.unregisterAdapter(modifySleicFields, name='sleicPersonExtender-modifySleicFields')
    
    return "Removed the extender from the root of the Plone site."
