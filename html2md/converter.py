try:
    import htmlentitydefs as entities
except ImportError:
    from html import entities # Py3k

from .options import DEFAULT_OPTIONS

class Html2Md(object):
    def __init__(self, options=None):
        self.options = dict(DEFAULT_OPTIONS)
        if options: self.options.update(options)

        self.tags = {
            '!doctype': {self.drop},
            'a': {},
            'abbr': {},
            'acronym': {},
            'address': {},
            'applet': {self.drop},
            'area': {self.drop},
            'article': {},
            'aside': {},
            'audio': {self.drop},
            'b': {},
            'base': {self.drop}, # base url for relative links
            'basefont': {self.drop},
            'bdi': {},
            'bdo': {},
            'big': {},
            'blockquote': {},
            'body': {self.ignore},
            'br': {},
            'button': {self.drop},
            'canvas': {self.drop},
            'caption': {},
            'center': {self.ignore},
            'cite': {},
            'code': {},
            'col': {},
            'colgroup': {self.ignore},
            'command': {self.drop},
            'data': {},
            'datagrid': {self.drop},
            'datalist': {self.drop},
            'dd': {},
            'del': {},
            'details': {},
            'dfn': {},
            'dir': {self.ignore},
            'div': {},
            'dl': {},
            'dt': {},
            'em': {},
            'embed': {self.drop},
            'eventsource': {self.drop},
            'fieldset': {self.drop},
            'figcaption': {},
            'figure': {self.ignore},
            'font': {self.ignore},
            'footer': {},
            'form': {self.drop},
            'frame': {self.drop},
            'frameset': {self.ignore},
            'h1': {},
            'h2': {},
            'h3': {},
            'h4': {},
            'h5': {},
            'h6': {},
            'head': {self.drop},
            'header': {},
            'hgroup': {self.ignore},
            'hr': {},
            'html': {self.ignore},
            'i': {},
            'iframe': {self.drop},
            'img': {},
            'input': {self.drop},
            'ins': {},
            'isindex': {self.drop},
            'kbd': {},
            'keygen': {self.drop},
            'label': {self.drop},
            'legend': {self.drop},
            'li': {},
            'link': {self.drop},
            'map': {self.drop},
            'mark': {},
            'menu': {self.drop},
            'meta': {self.drop},
            'meter': {self.drop},
            'nav': {self.ignore},
            'noframes': {self.drop},
            'noscript': {self.ignore},
            'object': {self.drop},
            'ol': {},
            'optgroup': {self.drop},
            'option': {self.drop},
            'output': {self.drop},
            'p': {},
            'param': {self.drop},
            'pre': {},
            'progress': {self.drop},
            'q': {},
            'rp': {},
            'rt': {},
            'ruby': {},
            's': {},
            'samp': {},
            'script': {self.drop},
            'section': {},
            'select': {self.drop},
            'small': {},
            'source': {self.drop},
            'span': {},
            'strike': {},
            'strong': {},
            'style': {self.drop},
            'sub': {},
            'summary': {},
            'sup': {},
            'table': {},
            'tbody': {},
            'td': {},
            'textarea': {self.drop},
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
            'video': {self.drop},
            'wbr': {},
        }

    def ignore(self):
        pass

    def drop(self):
        pass
