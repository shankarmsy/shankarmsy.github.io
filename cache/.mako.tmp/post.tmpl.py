# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1419402269.70353
_enable_loop = True
_template_filename = u'/home/shanks/Envs/Nikola/local/lib/python2.7/site-packages/nikola/data/themes/bootstrap/templates/post.tmpl'
_template_uri = u'post.tmpl'
_source_encoding = 'utf-8'
_exports = [u'content', u'extra_head', u'sourcelink']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'pheader', context._clean_inheritance_tokens(), templateuri=u'post_header.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'pheader')] = ns

    ns = runtime.TemplateNamespace(u'comments', context._clean_inheritance_tokens(), templateuri=u'comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'comments')] = ns

    ns = runtime.TemplateNamespace(u'helper', context._clean_inheritance_tokens(), templateuri=u'post_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'helper')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        pheader = _mako_get_namespace(context, 'pheader')
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        parent = context.get('parent', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        def sourcelink():
            return render_sourcelink(context._locals(__M_locals))
        messages = context.get('messages', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        def content():
            return render_content(context._locals(__M_locals))
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        post = context.get('post', UNDEFINED)
        show_sourcelink = context.get('show_sourcelink', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'sourcelink'):
            context['self'].sourcelink(**pageargs)
        

        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        pheader = _mako_get_namespace(context, 'pheader')
        helper = _mako_get_namespace(context, 'helper')
        messages = context.get('messages', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        def content():
            return render_content(context)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        post = context.get('post', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n<article class="post-')
        __M_writer(unicode(post.meta('type')))
        __M_writer(u' h-entry hentry postpage" itemscope="itemscope" itemtype="http://schema.org/Article">\n    ')
        __M_writer(unicode(pheader.html_post_header()))
        __M_writer(u'\n    <div class="e-content entry-content" itemprop="articleBody text">\n    ')
        __M_writer(unicode(post.text()))
        __M_writer(u'\n    </div>\n    <aside class="postpromonav">\n    <nav>\n    ')
        __M_writer(unicode(helper.html_tags(post)))
        __M_writer(u'\n    ')
        __M_writer(unicode(helper.html_pager(post)))
        __M_writer(u'\n    </nav>\n    </aside>\n')
        if not post.meta('nocomments') and site_has_comments:
            __M_writer(u'        <section class="comments">\n        <h2>')
            __M_writer(unicode(messages("Comments")))
            __M_writer(u'</h2>\n        ')
            __M_writer(unicode(comments.comment_form(post.permalink(absolute=True), post.title(), post._base_path)))
            __M_writer(u'\n        </section>\n')
        __M_writer(u'    ')
        __M_writer(unicode(helper.mathjax_script(post)))
        __M_writer(u'\n</article>\n')
        __M_writer(unicode(comments.comment_link_script()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def extra_head():
            return render_extra_head(context)
        post = context.get('post', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        __M_writer(unicode(parent.extra_head()))
        __M_writer(u'\n')
        if post.meta('keywords'):
            __M_writer(u'    <meta name="keywords" content="')
            __M_writer(filters.html_escape(unicode(post.meta('keywords'))))
            __M_writer(u'">\n')
        if post.description():
            __M_writer(u'    <meta name="description" itemprop="description" content="')
            __M_writer(unicode(post.description()))
            __M_writer(u'">\n')
        __M_writer(u'    <meta name="author" content="')
        __M_writer(unicode(post.author()))
        __M_writer(u'">\n')
        if post.prev_post:
            __M_writer(u'        <link rel="prev" href="')
            __M_writer(unicode(post.prev_post.permalink()))
            __M_writer(u'" title="')
            __M_writer(unicode(post.prev_post.title()))
            __M_writer(u'" type="text/html">\n')
        if post.next_post:
            __M_writer(u'        <link rel="next" href="')
            __M_writer(unicode(post.next_post.permalink()))
            __M_writer(u'" title="')
            __M_writer(unicode(post.next_post.title()))
            __M_writer(u'" type="text/html">\n')
        __M_writer(u'    ')
        __M_writer(unicode(helper.open_graph_metadata(post)))
        __M_writer(u'\n    ')
        __M_writer(unicode(helper.twitter_card_information(post)))
        __M_writer(u'\n    ')
        __M_writer(unicode(helper.meta_translations(post)))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sourcelink(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def sourcelink():
            return render_sourcelink(context)
        post = context.get('post', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        show_sourcelink = context.get('show_sourcelink', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if show_sourcelink:
            __M_writer(u'    <li>\n    <a href="')
            __M_writer(unicode(post.source_link()))
            __M_writer(u'" id="sourcelink">')
            __M_writer(unicode(messages("Source")))
            __M_writer(u'</a>\n    </li>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"128": 9, "129": 10, "130": 10, "131": 10, "132": 12, "133": 13, "134": 13, "135": 13, "136": 15, "137": 15, "138": 15, "139": 16, "140": 17, "141": 17, "142": 17, "143": 17, "144": 17, "145": 19, "146": 20, "147": 20, "148": 20, "149": 20, "22": 3, "151": 22, "152": 22, "25": 4, "154": 23, "155": 23, "28": 2, "157": 24, "150": 20, "34": 0, "163": 50, "156": 24, "172": 50, "173": 51, "174": 52, "175": 53, "176": 53, "177": 53, "178": 53, "53": 2, "54": 3, "55": 4, "56": 5, "61": 25, "66": 48, "71": 56, "77": 27, "184": 178, "89": 27, "90": 28, "91": 28, "92": 29, "93": 29, "94": 31, "95": 31, "96": 35, "97": 35, "98": 36, "99": 36, "100": 39, "101": 40, "102": 41, "103": 41, "104": 42, "105": 42, "106": 45, "107": 45, "108": 45, "109": 47, "110": 47, "116": 7, "153": 22, "125": 7, "126": 8, "127": 8}, "uri": "post.tmpl", "filename": "/home/shanks/Envs/Nikola/local/lib/python2.7/site-packages/nikola/data/themes/bootstrap/templates/post.tmpl"}
__M_END_METADATA
"""
