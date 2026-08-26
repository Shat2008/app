from django.urls import path
from django.contrib import admin
from .views import (
    task1, task2, task3, css, comment_v, regestr1, testkod, kod1, kod2, kod3, 
    kod4, kod5, kod6, kod7, user_login, user_logout, user_register, sait, 
    html_page, choice, study, definition, discovery, addition, gathering, 
    writing, organization, connection, semantics, creation, connectionn, 
    cssGlav, jsGlav, vstypOneCss,vstypTwoCss,osnoviOneCss,osnoviTwoCss,workOneCss,workTwoCss,blokOneCss,blokTwoCss,
    oforOneCss,oforTwoCss,animOneCss,animTwoCss,adapOneCss,adapTwoCss,vstypTwoJs,vstypOneJs,osnoviTwoJs,osnoviOneJs,functionsOneJs,cyclesOneJs,domTwoJs,domOneJs,
    objectOneJs,arrayOneJs,practiceTwoJs,practiceOneJs,advancedOneJs,advancedTwoJs, chat_page,ask_ai,test_js_dom,test_js_basic
    ,test_css_layout,test_css_basic,test_html_advanced,test_html_basic,testGlav,test_all,
)

urlpatterns = [
    path('', regestr1, name='regestr1'),  # главная страница (титульная)
    path('admin/', admin.site.urls),

    # Авторизация и пользователи
    path('register/', user_register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),

    # Основные страницы
    path('sait/', sait, name='sait'),
    path('html/', html_page, name='html_page'),
    path('choice/', choice, name='choice'),

    # Страницы с комментариями
    path('comments/', comment_v, name='comments'),
    path('study/', study, name='study'),
    path('definition/', definition, name='definition'),
    path('discovery/', discovery, name='discovery'),
    path('addition/', addition, name='addition'),
    path('gathering/', gathering, name='gathering'),
    path('writing/', writing, name='writing'),
    path('organization/', organization, name='organization'),
    path('connection/', connection, name='connection'),
    path('semantics/', semantics, name='semantics'),
    path('creation/', creation, name='creation'),
    path('connectionn/', connectionn, name='connectionn'),

    # Дополнительные страницы
    path('testkod/', testkod, name='testkod'),
    path('kod1/', kod1, name='kod1'),
    path('kod2/', kod2, name='kod2'),
    path('kod3/', kod3, name='kod3'),
    path('kod4/', kod4, name='kod4'),
    path('kod5/', kod5, name='kod5'),
    path('kod6/', kod6, name='kod6'),
    path('kod7/', kod7, name='kod7'),

    # CSS / JS разделы
    path('css/', css, name='css'),
    path('cssGlav/', cssGlav, name='cssGlav'),
    path('jsGlav/', jsGlav, name='jsGlav'),
    path('vstypOneCss/', vstypOneCss, name='vstypOneCss'),
    path('vstypTwoCss/', vstypTwoCss, name='vstypTwoCss'),
    path('osnoviOneCss/', osnoviOneCss, name='osnoviOneCss'),
    path('osnoviTwoCss/', osnoviTwoCss, name='osnoviTwoCss'),
    path('workOneCss/', workOneCss, name='workOneCss'),
    path('workTwoCss/', workTwoCss, name='workTwoCss'),
    path('blokOneCss/', blokOneCss, name='blokOneCss'),
    path('blokTwoCss/', blokTwoCss, name='blokTwoCss'),
    path('oforOneCss/', oforOneCss, name='oforOneCss'),
    path('oforTwoCss/', oforTwoCss, name='oforTwoCss'),
    path('animOneCss/', animOneCss, name='animOneCss'),
    path('animTwoCss/', animTwoCss, name='animTwoCss'),
    path('adapOneCss/', adapOneCss, name='adapOneCss'),
    path('adapTwoCss/', adapTwoCss, name='adapTwoCss'),
    path('vstypTwoJs/', vstypTwoJs, name='vstypTwoJs'),
    path('vstypOneJs/', vstypOneJs, name='vstypOneJs'),
    path('osnoviTwoJs/', osnoviTwoJs, name='osnoviTwoJs'),
    path('osnoviOneJs/', osnoviOneJs, name='osnoviOneJs'),
    path('functionsOneJs/', functionsOneJs, name='functionsOneJs'),
    path('cyclesOneJs/', cyclesOneJs, name='cyclesOneJs'),
    path('domTwoJs/', domTwoJs, name='domTwoJs'),
    path('domOneJs/', domOneJs, name='domOneJs'),
    path('objectOneJs/', objectOneJs, name='objectOneJs'),
    path('arrayOneJs/', arrayOneJs, name='arrayOneJs'),
    path('practiceTwoJs/', practiceTwoJs, name='practiceTwoJs'),
    path('practiceOneJs/', practiceOneJs, name='practiceOneJs'),
    path('advancedTwoJs/', advancedTwoJs, name='advancedTwoJs'),
    path('advancedOneJs/', advancedOneJs, name='advancedOneJs'),
    # Задачи
    path('task1/', task1, name='task1'),
    path('task2/', task2, name='task2'),
    path('task3/', task3, name='task3'),
    path('chat/', chat_page, name='chat'),
    path('ask/', ask_ai, name='ask_ai'),


    path('test_all/', test_all, name='test_all'),
    path('test_js_dom/', test_js_dom, name='test_js_dom'),
    path('test_js_basic/', test_js_basic, name='test_js_basic'),
    path('test_css_layout/', test_css_layout, name='test_css_layout'),
    path('test_css_basic/', test_css_basic, name='test_css_basic'),
    path('test_html_advanced/', test_html_advanced, name='test_html_advanced'),
    path('test_html_basic/', test_html_basic, name='test_html_basic'),
    path('testGlav/', testGlav, name='testGlav'),
]
