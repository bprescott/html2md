from collections import defaultdict

try:
    import htmlentitydefs as entities
except ImportError:
    from html import entities # Py3k

from lxml import html
from lxml.etree import ElementTree, ElementBase

from .options import DEFAULT_OPTIONS

class Html2Md(object):
    def __init__(self, source, options=None):
        # override options
        self.options = dict(DEFAULT_OPTIONS)
        if options: self.options.update(options)

        if isinstance(source, (str, unicode)):
            self.source = self.parse_source_string(source)
        elif isinstance(source, ElementBase):
            self.source = ElementTree(source)
        else:
            self.source = source # already ElementTree

        # set output buffer
        self.out = []

        # assign tag handlers
        self.tags = defaultdict (lambda: self.undefined, {
            '!doctype': {'cb': self.drop},
            'a': {},
            'abbr': {},
            'acronym': {},
            'address': {},
            'applet': {'cb': self.drop},
            'area': {'cb': self.drop},
            'article': {},
            'aside': {},
            'audio': {'cb': self.drop},
            'b': {},
            'base': {'cb': self.drop}, # base url for relative links
            'basefont': {'cb': self.drop},
            'bdi': {},
            'bdo': {},
            'big': {},
            'blockquote': {},
            'body': {'cb': self.ignore},
            'br': {},
            'button': {'cb': self.drop},
            'canvas': {'cb': self.drop},
            'caption': {},
            'center': {'cb': self.ignore},
            'cite': {},
            'code': {},
            'col': {},
            'colgroup': {'cb': self.ignore},
            'command': {'cb': self.drop},
            'data': {},
            'datagrid': {'cb': self.drop},
            'datalist': {'cb': self.drop},
            'dd': {},
            'del': {},
            'details': {},
            'dfn': {},
            'dir': {'cb': self.ignore},
            'div': {},
            'dl': {},
            'dt': {},
            'em': {},
            'embed': {'cb': self.drop},
            'eventsource': {'cb': self.drop},
            'fieldset': {'cb': self.drop},
            'figcaption': {},
            'figure': {'cb': self.ignore},
            'font': {'cb': self.ignore},
            'footer': {},
            'form': {'cb': self.drop},
            'frame': {'cb': self.drop},
            'frameset': {'cb': self.ignore},
            'h1': {},
            'h2': {},
            'h3': {},
            'h4': {},
            'h5': {},
            'h6': {},
            'head': {'cb': self.drop},
            'header': {},
            'hgroup': {'cb': self.ignore},
            'hr': {},
            'html': {'cb': self.ignore},
            'i': {},
            'iframe': {'cb': self.drop},
            'img': {},
            'input': {'cb': self.drop},
            'ins': {},
            'isindex': {'cb': self.drop},
            'kbd': {},
            'keygen': {'cb': self.drop},
            'label': {'cb': self.drop},
            'legend': {'cb': self.drop},
            'li': {},
            'link': {'cb': self.drop},
            'map': {'cb': self.drop},
            'mark': {},
            'menu': {'cb': self.drop},
            'meta': {'cb': self.drop},
            'meter': {'cb': self.drop},
            'nav': {'cb': self.ignore},
            'noframes': {'cb': self.drop},
            'noscript': {'cb': self.ignore},
            'object': {'cb': self.drop},
            'ol': {},
            'optgroup': {'cb': self.drop},
            'option': {'cb': self.drop},
            'output': {'cb': self.drop},
            'p': {},
            'param': {'cb': self.drop},
            'pre': {},
            'progress': {'cb': self.drop},
            'q': {},
            'rp': {},
            'rt': {},
            'ruby': {},
            's': {},
            'samp': {},
            'script': {'cb': self.drop},
            'section': {},
            'select': {'cb': self.drop},
            'small': {},
            'source': {'cb': self.drop},
            'span': {},
            'strike': {},
            'strong': {},
            'style': {'cb': self.drop},
            'sub': {},
            'summary': {},
            'sup': {},
            'table': {},
            'tbody': {},
            'td': {},
            'textarea': {'cb': self.drop},
            'tfoot': {},
            'th': {},
            'thead': {},
            'time': {},
            'title': {},
            'tr': {},
            'track': {},
            'tt': {},
            'u': {},
            'ul': {},
            'var': {},
            'video': {'cb': self.drop},
            'wbr': {},
        })

    def parse_source_string(self, source):
        # feel free to override and use custom self.options here
        return ElementTree(html.fromstring(source))

    def parse(self):
        for element in self.source.iter():
            self.handle(element)

    def handle(self, element):
        pass

    def undefined(self):
        print "WARNING, undefined tag"
        pass

    def ignore(self):
        pass

    def drop(self):
        pass
