from django import template

register = template.Library()


@register.inclusion_tag('blog/navmenu.html')
def show_navmenu(current_path=None):
    nav_menu = [{'title': "Home", 'url_name': 'home'},
                {'title': "Blog", 'url_name': 'blog_list'},
                # {'title': "Register", 'url_name': 'register'},
                # {'title': "Login", 'url_name': 'login'},
                ]
    return {'nav_menu': nav_menu, 'current_path': current_path}


@register.inclusion_tag('blog/authnavmenu.html')
def show_authnavmenu(current_path=None, is_authenticated=False, username=None):
    auth_nav_menu_f = [{'title': "Register", 'url_name': 'register'},
                       {'title': "Login", 'url_name': 'login'}, ]
    auth_nav_menu_s = [{'title': username, 'url_name': 'home'},
                       {'title': "Logout", 'url_name': 'logout'}, ]

    if is_authenticated:
        return {'auth_nav_menu': auth_nav_menu_s,
                'current_path': current_path}
    else:
        return {'auth_nav_menu': auth_nav_menu_f,
                'current_path': current_path}
