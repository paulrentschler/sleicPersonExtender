sleicPersonExtender: customize the person object for SLEIC


Dependencies

  * Plone 3.x
  * FacultyStaffDirectory 2.x (http://plone.org/products/faculty-staff-directory/)
  * archetypes.schemaextender 1.x


Description
  
  Developed for Plone 3.3.1 and copied from the dasHorseExtender product.
  https://weblion.psu.edu/trac/weblion/browser/dairyAnimalScience/dasHorseExtender

  Fields added:
    * campus: campus they are located at

  Fields hidden:
    * OfficeCity
    * OfficeState
    * OfficePostalCode
    * Committees

  Other changes:
    * Updated the labels and descriptions on may fields to make them
      more user friendly
    * Moved some fields around to improve the flow
    * Hide some of the schemata from all users except Managers
          

Installing the Extender

  1. Install FacultyStaffDirectory according to that product's README.txt.
  
  2. Place sleicPersonExtender folder in the Products folder.
  
  3. Restart Zope.
  
  4. Go to your-plone-site -> site setup -> Add/Remove Products, and 
     install sleicPersonExtender.


Version History
  
      1.0 -- Initial release for Plone 3.x


Authorship

  This product was developed by Paul Rentschler of the Huck Institutes of the 
  Life Sciences at Penn State University.

  
Contact

    Huck Institutes Web Team
    Penn State University
    401 Life Sciences Building
    University Park, PA 16802
    webteam@huck.psu.edu


License

    Copyright (c) 2006-2010 The Pennsylvania State University. WebLion is
    developed and maintained by the WebLion Project Team, its partners, and
    members of the Penn State Zope Users Group.

    This program is free software; you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by the Free
    Software Foundation; either version 2 of the License, or (at your option)
    any later version.

    This program is distributed in the hope that it will be useful, but WITHOUT
    ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
    FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
    more details.

    You should have received a copy of the GNU General Public License along with
    this program; if not, write to the Free Software Foundation, Inc., 59 Temple
    Place, Suite 330, Boston, MA 02111-1307 USA.

    This document is written using the Structured Text format for conversion
    into alternative formats.
