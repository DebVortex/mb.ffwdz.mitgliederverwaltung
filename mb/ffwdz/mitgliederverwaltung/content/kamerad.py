from five import grok
from zope import schema
from zope.interface import Interface, implements

from plone.directives import form, dexterity
from plone.indexer import indexer
from plone.dexterity.content import Item

from mb.ffwdz.mitgliederverwaltung import _

class IKamerad(Interface):
    """
    """
    
    title = schema.TextLine(
        title=_(u"Name des Kameraden"),
        required = True,
    )
    
    geburtsdatum = schema.Date(
        title=_(u"Geburtsdatum"),
        required = False,
    )
    
    mitglied_seit = schema.Date(
        title=_(u"Eintrittsdatum"),
        required = True,
    )
    
    telefon = schema.TextLine(
        title=_(u"Telefon"),
        required = False,
    )
    
    anschrift = schema.Text(
        title=_(u"Anschrift"),
        required = True,
    )
    
    dienstgrad = schema.TextLine(
        title=_(u"Dienstgrad"),
        required = False,
    )
    
    hauptamtlich = schema.Bool(
        title=_(u"Hauptamtlich"),
        required = False,
    )
    
    ausb_tmft = schema.Bool(
        title=_(u"Kreisausbilder: TM / TF"),
        required = False,
    )
    
    ausb_tmft_fort = schema.Bool(
        title=_(u"Kreisausbilder: TM / TF (Fortbildung)"),
        required = False,
    )
    
    ausb_maschinist = schema.Bool(
        title=_(u"Kreisausbilder: Maschinist"),
        required = False,
    )
    
    ausb_maschinist_fort = schema.Bool(
        title=_(u"Kreisausbilder: Maschinist (Fortbildung)"),
        required = False,
    )
    
    ausb_atemschutz = schema.Bool(
        title=_(u"Kreisausbilder: Atemschutz"),
        required = False,
    )
    
    ausb_atemschutz_fort = schema.Bool(
        title=_(u"Kreisausbilder: Atemschutz (Fortbildung)"),
        required = False,
    )
    
    ausb_sprechfunk = schema.Bool(
        title=_(u"Kreisausbilder: Sprechfunk"),
        required = False,
    )
    
    ausb_sprechfunk_fort = schema.Bool(
        title=_(u"Kreisausbilder: Sprechfunk (Fortbildung)"),
        required = False,
    )
    
    ausb_kettensaege = schema.Bool(
        title=_(u"Kreisausbilder: Kettensaege"),
        required = False,
    )
    
    ausb_jugend = schema.Bool(
        title=_(u"Kreisausbilder: Jugend-FW"),
        required = False,
    )
    
    ausb_jugend_fort = schema.Bool(
        title=_(u"Kreisausbilder: Jugend-FW (Fortbildung)"),
        required = False,
    )
    
    kreisjugendwart = schema.Bool(
        title=_(u"Kreisjugendfeuerwehrwart"),
        required = False,
    )
    
    kreisjugendwart_fort = schema.Bool(
        title=_(u"Kreisjugendfeuerwehrwart (Fortbildung)"),
        required = False,
    )
    
    geraetewart = schema.Bool(
        title=_(u"Geraetewartausbildung"),
        required = False,
    )
    
    atemschutz_geraetewart = schema.Bool(
        title=_(u"Atemschutz-Geraetewartausbildung"),
        required = False,
    )
    
    atemschutz_geraetewart_fort = schema.Bool(
        title=_(u"Atemschutz-Geraetewartausbildung (Fortbildung)"),
        required = False,
    )
    
    wehrleiter = schema.Bool(
        title=_(u"Wehrleiter"),
        required = False,
    )

    wehrleiter_fort = schema.Bool(
        title=_(u"Wehrleiter (Fortbildung)"),
        required = False,
    )
    
    verbandsfuehrer = schema.Bool(
        title=_(u"Verbandsfuehrer"),
        required = False,
    )
    
    zugfuehrer = schema.Bool(
        title=_(u"Zugfuehrer"),
        required = False,
    )
    
    zugfuehrer_fort = schema.Bool(
        title=_(u"Zugfuehrer (Fortbildung)"),
        required = False,
    )
    
    gruppenfuehrer = schema.Bool(
        title=_(u"Gruppenfuehrer"),
        required = False,
    )
    
    gruppenfuehrer_fort = schema.Bool(
        title=_(u"Gruppenfuehrer (Fortbildung)"),
        required = False,    
    )
    
    maschinist = schema.Bool(
        title=_(u"Maschinist"),
        required = False,
    )
    
    drehleitermaschinist = schema.Bool(
        title=_(u"Drehleitermaschinist"),
        required = False,
    )
    
    technischehileleistung = schema.Bool(
        title=_(u"technische Hilfeleistung"),
        required = False,
    )
    
    technischehileleistung_a = schema.Bool(
        title=_(u"technische Hilfeleistung (Teil A)"),
        required = False,
    )
    
    technischehileleistung_b = schema.Bool(
        title=_(u"technische Hilfeleistung (Teil B)"),
        required = False,
    )
    
    technischehileleistung_part_rettung = schema.Bool(
        title=_(u"technische Hilfeleistung (Patientengerechte Rettung)"),
        required = False,
    )
    
    technischehileleistung_hoehen_u_tiefen = schema.Bool(
        title=_(u"technische Hilfeleistung (Retten aus Hoehen und Tiefen)"),
        required = False,
    )
        
    sicherheitsbeauftragter = schema.Bool(
        title=_(u"Sicherheitsbeauftragter"),
        required = False,
    )
    
    strahlenschutzbeauftragter = schema.Bool(
        title=_(u"Strahlenschutzbeauftragter"),
        required = False,
    )
    
    strahlenschutzbeauftragter_fort = schema.Bool(
        title=_(u"Strahlenschutzbeauftragter (Fortbildung)"),
        required = False,
    )
    
    sichtung_stab_u_tel = schema.Bool(
        title=_(u"Sichtung Stab und TEL"),
        required = False,
    )
    
    einweisung_stab_u_tel = schema.Bool(
        title=_(u"Einweisung Stab und TEL"),
        required = False,
    )
    
    jugendwart = schema.Bool(
        title=_(u"Jugendfeuerwehrarbeit"),
        required = False,
    )
    
    kampfrichter_sport = schema.Bool(
        title=_(u"Kampfrichter Feuerwehrsport"),
        required = False,
    )
    
    richter_leistungsabzeichen = schema.Bool(
        title=_(u"Wertungsrichter Leistungsabzeichen"),
        required = False,
    )
    
    abc = schema.Bool(
        title=_(u"ABC-Basislehrgang"),
        required = False,
    )
    
    abc_messen = schema.Bool(
        title=_(u"ABC-Messen"),
        required = False,
    )
    
    abc_technik = schema.Bool(
        title=_(u"ABC-Technik"),
        required = False,
    )
    
    abc_dekonp = schema.Bool(
        title=_(u"ABC-DekonP"),
        required = False,
    )
    
    dekon_maschinist = schema.Bool(
        title=_(u"Dekon-Maschinist"),
        required = False,
    )
    
    abcfuehrung = schema.Bool(
        title=_(u"Fuehren in ABC-Einsaetzen"),
        required = False,
    )
    
    abcfuehrung_fort = schema.Bool(
        title=_(u"Fuehren in ABC-Einsaetzen (Fortbildung)"),
        required = False,
    )
    
    messleitwagen = schema.Bool(
        title=_(u"Fuehrer Messleitwagen"),
        required = False,
    )
    
    messleitwagen_fort = schema.Bool(
        title=_(u"Fuehrer Messleitwagen (Fortbildung)"),
        required = False,
    )
    
    vorb_brandschutz = schema.Bool(
        title=_(u"Vorbeugender Brandschutz"),
        required = False,
    )
    
    disma = schema.Bool(
        title=_(u"Arbeiten mit DISMA 4"),
        required = False,
    )
    
    disma_fort = schema.Bool(
        title=_(u"Arbeiten mit DISMA4 (Fortbildung)"),
        required = False,
    )
    
    sysadmin = schema.Bool(
        title=_(u"Schulung in Systemadministration"),
        required = False,
    )
    
    kettensaege = schema.Bool(
        title=_(u"Kettensaegenlehrgang"),
        required = False,
    )

    
    atemschutz = schema.Bool(
        title=_(u"Atemschutzgeraetetraeger"),
        required = False,
    )
    
    truppfuehrer = schema.Bool(
        title=_(u"Truppfuehrer"),
        required = False,
    )
    
    sprechfunker = schema.Bool(
        title=_(u"Sprechfunker"),
        required = False,
    )
    
    truppmann = schema.Bool(
        title=_(u"Truppmann"),
        required = False,
    )
    

    
@indexer(IKamerad)
def eintrittsjahr_indexer(obj):
    return obj.mitglied_seit.year
grok.global_adapter(eintrittsjahr_indexer, name="eintrittsjahr")

@indexer(IKamerad)
def zug_indexer(obj):
    return obj.getParentNode().id
grok.global_adapter(zug_indexer, name="uebergeordneter_zug")