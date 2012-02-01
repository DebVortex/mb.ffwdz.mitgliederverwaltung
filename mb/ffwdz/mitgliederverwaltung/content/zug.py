from five import grok
from zope import schema

from plone.directives import form, dexterity

from mb.ffwdz.mitgliederverwaltung import _

class IZug(form.Schema):
    """
    """
    
    title = schema.TextLine(
        title = _(u"Name des Zuges"),
        required = True,
    )
        
    ehrenjahre = schema.TextLine(
        title = _(u"Ehrenjahre"),
        description = _(u"An welche Dienstjahre soll gesondert errinert werden?" + \
                         " Bitte separieren Sie mit Komma ohne Leerzeichen."),
        required = False,
    )