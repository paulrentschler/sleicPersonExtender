#from Products.CMFCore.DirectoryView import registerDirectory
#from Products.CMFPlone.interfaces import IPloneSiteRoot
from Products.FacultyStaffDirectory.extenderInstallation import installExtenderGloballyIfLocallyIsNotSupported
#from Products.GenericSetup import EXTENSION, profile_registry

from Products.sleicPersonExtender.person import addSleicFields
from Products.sleicPersonExtender.person import modifySleicFields

installExtenderGloballyIfLocallyIsNotSupported(addSleicFields, 'sleicPersonExtender')
installExtenderGloballyIfLocallyIsNotSupported(modifySleicFields, 'sleicPersonExtender')

#registerDirectory('skins', globals())

#def initialize(context):
#    profile_registry.registerProfile(
#        "default",
#        "sleicPersonExtender",
#        "Customize the Faculty/Staff Directory's Person type for SLEIC.",
#        "profiles/default",
#        product="Products.sleicPersonExtender",
#        profile_type=EXTENSION,
#        for_=IPloneSiteRoot)
#    profile_registry.registerProfile(
#        "uninstall",
#        "sleicPersonExtender Uninstall",
#        "Removes the changes to the Faculty/Staff Directory's Person type to customize it for SLEIC.",
#        "profiles/uninstall",
#        product="Products.sleicPersonExtender",
#        profile_type=EXTENSION,
#        for_=IPloneSiteRoot)








