# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1419402269.049585
_enable_loop = True
_template_filename = u'/home/shanks/Envs/Nikola/local/lib/python2.7/site-packages/nikola/data/themes/base/templates/tag.tmpl'
_template_uri = u'tag.tmpl'
_source_encoding = 'utf-8'
_exports = [u'content', u'extra_head']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'list_post.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        kind = context.get('kind', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        title = context.get('title', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        len = context.get('len', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        tag = context.get('tag', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        date_format = context.get('date_format', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer(u'\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        generate_rss = context.get('generate_rss', UNDEFINED)
        kind = context.get('kind', UNDEFINED)
        title = context.get('title', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        len = context.get('len', UNDEFINED)
        def content():
            return render_content(context)
        posts = context.get('posts', UNDEFINED)
        tag = context.get('tag', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        date_format = context.get('date_format', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n<article class="tagpage">\n    <header>\n        <h1>')
        __M_writer(unicode(title))
        __M_writer(u'</h1>\n        <div class="metadata">\n')
        if len(translations) > 1 and generate_rss:
            for language in translations:
                __M_writer(u'                <p class="feedlink">\n                    <a href="')
                __M_writer(unicode(_link(kind + "_rss", tag, language)))
                __M_writer(u'" hreflang="')
                __M_writer(unicode(language))
                __M_writer(u'" type="application/rss+xml">')
                __M_writer(unicode(messages('RSS feed', language)))
                __M_writer(u' (')
                __M_writer(unicode(language))
                __M_writer(u')</a>&nbsp;\n                </p>\n')
        elif generate_rss:
            __M_writer(u'                <p class="feedlink"><a href="')
            __M_writer(unicode(_link(kind + "_rss", tag)))
            __M_writer(u'" type="application/rss+xml">')
            __M_writer(unicode(messages('RSS feed')))
            __M_writer(u'</a></p>\n')
        __M_writer(u'        </div>\n    </header>\n')
        if posts:
            __M_writer(u'    <ul class="postlist">\n')
            for post in posts:
                __M_writer(u'        <li><a href="')
                __M_writer(unicode(post.permalink()))
                __M_writer(u'" class="listtitle">')
                __M_writer(unicode(post.title()))
                __M_writer(u'</a> <time class="listdate" datetime="')
                __M_writer(unicode(post.date.isoformat()))
                __M_writer(u'" title="')
                __M_writer(unicode(post.formatted_date(date_format)))
                __M_writer(u'">')
                __M_writer(unicode(post.formatted_date(date_format)))
                __M_writer(u'</time></li>\n')
            __M_writer(u'    </ul>\n')
        __M_writer(u'</article>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def extra_head():
            return render_extra_head(context)
        kind = context.get('kind', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        len = context.get('len', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        tag = context.get('tag', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        __M_writer(unicode(parent.extra_head()))
        __M_writer(u'\n')
        if len(translations) > 1 and generate_rss:
            for language in translations:
                __M_writer(u'            <link rel="alternate" type="application/rss+xml" type="application/rss+xml" title="RSS for ')
                __M_writer(unicode(kind))
                __M_writer(u' ')
                __M_writer(unicode(tag))
                __M_writer(u' (')
                __M_writer(unicode(language))
                __M_writer(u')" href="')
                __M_writer(unicode(_link(kind + "_rss", tag, language)))
                __M_writer(u'">\n')
        elif generate_rss:
            __M_writer(u'        <link rel="alternate" type="application/rss+xml" type="application/rss+xml" title="RSS for ')
            __M_writer(unicode(kind))
            __M_writer(u' ')
            __M_writer(unicode(tag))
            __M_writer(u'" href="')
            __M_writer(unicode(_link(kind + "_rss", tag)))
            __M_writer(u'">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"133": 4, "134": 5, "135": 5, "136": 6, "137": 7, "138": 8, "139": 8, "140": 8, "141": 8, "142": 8, "143": 8, "144": 8, "145": 8, "146": 8, "147": 10, "148": 11, "149": 11, "150": 11, "151": 11, "152": 11, "153": 11, "26": 0, "154": 11, "160": 154, "46": 2, "51": 13, "56": 40, "62": 16, "78": 16, "79": 19, "80": 19, "81": 21, "82": 22, "83": 23, "84": 24, "85": 24, "86": 24, "87": 24, "88": 24, "89": 24, "90": 24, "91": 24, "92": 27, "93": 28, "94": 28, "95": 28, "96": 28, "97": 28, "98": 30, "99": 32, "100": 33, "101": 34, "102": 35, "103": 35, "104": 35, "105": 35, "106": 35, "107": 35, "108": 35, "109": 35, "110": 35, "111": 35, "112": 35, "113": 37, "114": 39, "120": 4}, "uri": "tag.tmpl", "filename": "/home/shanks/Envs/Nikola/local/lib/python2.7/site-packages/nikola/data/themes/base/templates/tag.tmpl"}
__M_END_METADATA
"""
