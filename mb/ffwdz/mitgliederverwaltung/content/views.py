# encoding: utf-8 

from Products.Five.browser import BrowserView                                                                                                      
from Products.CMFCore.utils import getToolByName

from mb.ffwdz.mitgliederverwaltung.content.kamerad import IKamerad
from mb.ffwdz.mitgliederverwaltung.content.zug import IZug
                                                                 
from time import gmtime
                                                                                                                                                   
class KameradView(BrowserView):                                                                                                        
    """
    """
    
    def get_edit_link(self):
        """
        """
        return self.context.absolute_url()+"/edit"
        
    def get_deletion_link(self):
        """
        """
        return self.context.absolute_url()+"/delete_confirmation"
        
    def mitglied_seit(self):
        """
        """
        day = self.context.mitglied_seit.day
        month = self.context.mitglied_seit.month
        year = self.context.mitglied_seit.year
        return "%s.%s.%s" % (day, month, year)
    
    def geburtsdatum(self):
        """
        """
        day = self.context.geburtsdatum.day
        month = self.context.geburtsdatum.month
        year = self.context.geburtsdatum.year
        return "%s.%s.%s" % (day, month, year)
    
    def tech_stand(self):
        """
        """
        parts = []
        if self.context.technischehileleistung_a:
            parts.append("Teil A")
        if self.context.technischehileleistung_b:
            parts.append("Teil B")
        if parts == []:
            return
        else:
            return "(" + ", ".join(parts) + ")"
    
class ZugView(BrowserView):
    """
    """
    
    def get_kameraden(self):
        """
        """
        kameraden = []
        for kamerad in self.context.getChildNodes():
            kameraddict = {}
            kameraddict['name'] = kamerad.title
            kameraddict['anschrift'] = kamerad.anschrift
            kameraddict['telefon'] = kamerad.telefon
            kameraddict['dienstgrad'] = kamerad.dienstgrad
            kameraddict['url'] = kamerad.absolute_url()
            kameraden.append(kameraddict)
        kameraden = self.sortDictBy(kameraden, 'name')
        return kameraden

    def sortDictBy(self, list, key):
        nlist = map(lambda x, key=key: (x[key], x), list)
        nlist.sort()
        return map(lambda (key, x): x, nlist)                
    
    def get_add_link(self):
        """
        """
        return self.context.absolute_url()+"/++add++mb.ffwdz.mitgliederverwaltung.kamerad"
    
    def get_overview_link(self):
        """
        """
        return self.context.absolute_url()+"/@@honour_overview"

    def get_edit_link(self):
        """
        """
        return self.context.absolute_url()+"/edit"
        
    def get_deletion_link(self):
        """
        """
        return self.context.absolute_url()+"/delete_confirmation"

    
class HonourOverview(BrowserView):
    """
    """
    
    def __init__(self, context, request):
        """
        """
        self.context = context
        self.request = request
        self.catalog = getToolByName(self.context, 'portal_catalog')
        if self.context.ehrenjahre:
            self.ehrenjahre = self.context.ehrenjahre.split(",")
    
    def get_back_link(self):
        """
        """
        return self.context.absolute_url()
        
    def get_ehrungen_this_year(self):
        """
        """
        self.honour_list = []
        query = {}
        query['uebergeordneter_zug'] = self.context.id
        self.ehrenjahre.sort()
        diesesjahr = gmtime().tm_year
        for ehrenjahr in self.ehrenjahre:
            honour_dict = {'ehrenjahr':ehrenjahr,
                           'kameraden': []}
            query['eintrittsjahr'] = diesesjahr - int(ehrenjahr)
            results = self.catalog.searchResults(query)
            for result in results:
                kamerad = result.getObject()
                kamerad_dict = {'name': kamerad.title,
                                'url': kamerad.absolute_url()}
                honour_dict['kameraden'].append(kamerad_dict)
            self.honour_list.append(honour_dict)
        return self.honour_list
    
    def get_ehrungen_next_year(self):
        """
        """
        self.honour_list = []
        query = {}
        query['uebergeordneter_zug'] = self.context.id
        self.ehrenjahre.sort()
        nextjahr = gmtime().tm_year + 1
        for ehrenjahr in self.ehrenjahre:
            honour_dict = {'ehrenjahr':ehrenjahr,
                           'kameraden': []}
            query['eintrittsjahr'] = nextjahr - int(ehrenjahr)
            results = self.catalog.searchResults(query)
            for result in results:
                kamerad = result.getObject()
                kamerad_dict = {'name': kamerad.title,
                                'url': kamerad.absolute_url()}
                honour_dict['kameraden'].append(kamerad_dict)
            self.honour_list.append(honour_dict)
        return self.honour_list
    
class ExportView(BrowserView):                                                                                                        
    """
    """
    
    def __call__(self):
        """
        """
        from zope.app.component import hooks
        from elementtree import ElementTree as ET
        kamerad_attr = ["title", "geburtsdatum", "mitglied_seit", "telefon", "anschrift", "dienstgrad", 
            "hauptamtlich", "ausb_tmft", "ausb_maschinist", "ausb_atemschutz", "ausb_sprechfunk", "ausb_kettensaege", 
            "ausb_jugend", "geraetewart", "atemschutz_geraetewart", "wehrleiter", "verbandsfuehrer", "zugfuehrer",
            "gruppenfuehrer", "maschinist", "atemschutz", "truppfuehrer", "sprechfunker", "truppmann"]
        site = hooks.getSite()
        brains = site.portal_catalog(portal_type="mb.ffwdz.mitgliederverwaltung.zug")
        root = ET.Element(u"Mitgliederverwaltung")
        for brain in brains:
            zug = brain.getObject()
            zug_as_xml = ET.Element(
                zug.id.encode('utf-8'), 
                attrib={
                    'ehrenjahre' : zug.ehrenjahre.encode('utf-8'),
                    'name' : zug.title.encode('utf-8')
                },
            )
            users = zug.getChildNodes()
            for user in users:
                user_as_xml = ET.Element(
                    user.id.encode('utf-8')
                )
                for attr in kamerad_attr:
                    user_as_xml[attr] = user.get(attr, "")
                zug_as_xml.append(user_as_xml)
            root.append(zug_as_xml)
        self.request.response.setHeader('Content-Type', 'application/xml')
        return ET.tostring(root)