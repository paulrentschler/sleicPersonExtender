#from Products.CMFCore.utils import getToolByName
from Products.FacultyStaffDirectory.extenderInstallation import declareInstallRoutines
#localAdaptersAreSupported, installExtender, uninstallExtender
from Products.sleicPersonExtender.person import addSleicFields
from Products.sleicPersonExtender.person import modifySleicFields

#_adapterName = 'sleicPersonExtender'

#def _runProfile(profile, portal):
#    setupTool = getToolByName(portal, 'portal_setup')
#    setupTool.runAllImportStepsFromProfile(profile)

def install(portal):
#    if localAdaptersAreSupported:
#        installExtender(portal, addHuckFields, _adapterName)
#        installExtender(portal, modifyHuckFields, _adapterName)
#    _runProfile('profile-Products.huckPersonExtender:default', portal)
    """Register the extender so it takes effect on this Plone site."""
    sm = portal.getSiteManager()
    sm.registerAdapter(addSleicFields, name='sleicPersonExtender-addSleicFields')
    sm.registerAdapter(modifySleicFields, name='sleicPersonExtender-modifySleicFields')
    
    return "Registered the extender at the root of the Plone site."

def uninstall(portal):
#    if localAdaptersAreSupported:
#        uninstallExtender(portal, addHuckFields, _adapterName)
#        uninstallExtender(portal, modifyHuckFields, _adapterName)
#    _runProfile('profile-Products.huckPersonExtender:uninstall', portal)
    sm = portal.getSiteManager()
    sm.unregisterAdapter(addSleicFields, name='sleicPersonExtender-addSleicFields')
    sm.unregisterAdapter(modifySleicFields, name='sleicPersonExtender-modifySleicFields')
    
    return "Removed the extender from the root of the Plone site."
