import os
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Comment, Comment1, Comment2, Comment3, Comment4, Comment5, Comment6, Comment7, Comment8, Comment9, Comment10, Comment11, Comment12, Comment13, Comment14, Comment15, Comment16, Comment17, Comment18, Comment19, Comment20, Comment21, Comment22, Comment23, Comment24, Comment25, Comment26, Comment27, Comment28, Comment29, Comment30, Comment31, Comment32, Comment33, Comment34, Comment35, Comment36, Comment37, Comment38, Comment39, Comment40
from .forms import CommentForm, CommentForm1, CommentForm2, CommentForm3, CommentForm4, CommentForm5, CommentForm6, CommentForm7, CommentForm8, CommentForm9, CommentForm10, CommentForm11, CommentForm12, CommentForm13, CommentForm14, CommentForm15, CommentForm16, CommentForm17, CommentForm18, CommentForm19, CommentForm20, CommentForm21, CommentForm22, CommentForm23, CommentForm24, CommentForm25, CommentForm26, CommentForm27, CommentForm28, CommentForm29, CommentForm30, CommentForm31, CommentForm32, CommentForm33, CommentForm34, CommentForm35, CommentForm36, CommentForm37, CommentForm38, CommentForm39, CommentForm40
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import json
def sait(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CommentForm12(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.save()
                return redirect('sait')
        else:
            form = CommentForm12()
    else:
        form = None
    comments = Comment12.objects.all().order_by('-created_at')
    return render(request, 'sait.html', {'form': form, 'comments': comments})

def task1(request):
    return render(request,'task1.html')

def task2(request):
    return render(request,'task2.html')

def task3(request):
    return render(request,'task3.html')

def css(request):
    return render(request,'css.html')

def user_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        if password != password_confirm:
            return HttpResponse('Passwords do not match')

        if User.objects.filter(username=username).exists():
            return HttpResponse('Username already exists')

        user = User.objects.create_user(username=username, password=password)
        user.save()

        return redirect('login') 

    return render(request, 'register.html')  

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['username'] = username  
            return redirect('sait')
        else:
            return HttpResponse('Invalid credentials')

    return render(request, 'login.html')  



from django.shortcuts import render, redirect
from .models import Comment
from .forms import CommentForm

def comment_v(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('comments')
    else:
        form = CommentForm()

    comments = Comment.objects.all().order_by('-created_at')
    return render(request, 'comments.html', {'form': form, 'comments': comments})

def choice(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.save()
                return redirect('choice')
        else:
            form = CommentForm()
    else:
        form = None

    comments = Comment.objects.all().order_by('-created_at')
    return render(request, 'choice.html', {'form': form, 'comments': comments})


def user_logout(request):
    logout(request)
    request.session.flush() 
    return redirect('login')

def regestr1(request):
    return render(request,'regestr1.html')
def html_page(request):
    return render(request,'html.html')

def testkod(request):
    return render(request,'testkod.html')
def kod1(request):
    return render(request,'kod1.html')

def kod2(request):
    return render(request,'kod2.html')

def kod3(request):
    return render(request,'kod3.html')

def kod4(request):
    return render(request,'kod4.html')

def kod5(request):
    return render(request,'kod5.html')

def kod6(request):
    return render(request,'kod6.html')

def kod7(request):
    return render(request,'kod7.html')



def study(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CommentForm1(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.save()
                return redirect('study')
        else:
            form = CommentForm1()
    else:
        form = None

    comments = Comment1.objects.all().order_by('-created_at')
    return render(request, 'study.html', {'form': form, 'comments': comments})
    

def definition(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CommentForm2(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.save()
                return redirect('definition')
        else:
            form = CommentForm2()
    else:
        form = None

    comments = Comment2.objects.all().order_by('-created_at')
    return render(request, 'definition.html', {'form': form, 'comments': comments})

def discovery(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CommentForm3(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.save()
                return redirect('discovery')
        else:
            form = CommentForm3()
    else:
        form = None

    comments = Comment3.objects.all().order_by('-created_at')
    return render(request, 'discovery.html', {'form': form, 'comments': comments})

def addition(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CommentForm4(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.save()
                return redirect('addition')
        else:
            form = CommentForm4()
    else:
        form = None

    comments = Comment4.objects.all().order_by('-created_at')
    return render(request, 'addition.html', {'form': form, 'comments': comments})



def gathering(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CommentForm5(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.save()
                return redirect('gathering')
        else:
            form = CommentForm5()
    else:
        form = None
    comments = Comment5.objects.all().order_by('-created_at')
    return render(request, 'gathering.html', {'form': form, 'comments': comments})


def writing(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CommentForm6(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.save()
                return redirect('writing')
        else:
            form = CommentForm6()
    else:
        form = None
    comments = Comment6.objects.all().order_by('-created_at')
    return render(request, 'writing.html', {'form': form, 'comments': comments})


def organization(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CommentForm7(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.save()
                return redirect('organization')
        else:
            form = CommentForm7()
    else:
        form = None
    comments = Comment7.objects.all().order_by('-created_at')
    return render(request, 'organization.html', {'form': form, 'comments': comments})


def connection(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CommentForm8(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.save()
                return redirect('connection')
        else:
            form = CommentForm8()
    else:
        form = None
    comments = Comment8.objects.all().order_by('-created_at')
    return render(request, 'connection.html', {'form': form, 'comments': comments})


def semantics(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CommentForm9(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.save()
                return redirect('semantics')
        else:
            form = CommentForm9()
    else:
        form = None
    comments = Comment9.objects.all().order_by('-created_at')
    return render(request, 'semantics.html', {'form': form, 'comments': comments})


def creation(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CommentForm10(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.save()
                return redirect('creation')
        else:
            form = CommentForm10()
    else:
        form = None
    comments = Comment10.objects.all().order_by('-created_at')
    return render(request, 'creation.html', {'form': form, 'comments': comments})


def connectionn(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CommentForm11(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.save()
                return redirect('connectionn')
        else:
            form = CommentForm11()
    else:
        form = None
    comments = Comment11.objects.all().order_by('-created_at')
    return render(request, 'creationn.html', {'form': form, 'comments': comments})



def cssGlav(request):
    return render(request, 'cssGlav.html')

def jsGlav(request):
    return render(request, 'jsGlav.html')

def vstypOneCss(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CommentForm13(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.save()
                return redirect('vstypOneCss')
        else:
            form = CommentForm13()
    else:
        form = None
    comments = Comment13.objects.all().order_by('-created_at')
    return render(request, 'vstypOneCss.html', {'form': form, 'comments': comments})

def vstypTwoCss(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CommentForm14(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.save()
                return redirect('vstypTwoCss')
        else:
            form = CommentForm14()
    else:
        form = None
    comments = Comment14.objects.all().order_by('-created_at')
    return render(request, 'vstypTwoCss.html', {'form': form, 'comments': comments})

def osnoviOneCss(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CommentForm15(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.save()
                return redirect('osnoviOneCss')
        else:
            form = CommentForm15()
    else:
        form = None
    comments = Comment15.objects.all().order_by('-created_at')
    return render(request, 'osnoviOneCss.html', {'form': form, 'comments': comments})

def osnoviTwoCss(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CommentForm16(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.save()
                return redirect('osnoviTwoCss')
        else:
            form = CommentForm16()
    else:
        form = None
    comments = Comment16.objects.all().order_by('-created_at')
    return render(request, 'osnoviTwoCss.html', {'form': form, 'comments': comments})

def workOneCss(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CommentForm17(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.save()
                return redirect('workOneCss')
        else:
            form = CommentForm17()
    else:
        form = None
    comments = Comment17.objects.all().order_by('-created_at')
    return render(request, 'workOneCss.html', {'form': form, 'comments': comments})

def workTwoCss(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CommentForm18(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.save()
                return redirect('workTwoCss')
        else:
            form = CommentForm18()
    else:
        form = None
    comments = Comment18.objects.all().order_by('-created_at')
    return render(request, 'workTwoCss.html', {'form': form, 'comments': comments})

def blokOneCss(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CommentForm19(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.save()
                return redirect('blokOneCss')
        else:
            form = CommentForm19()
    else:
        form = None
    comments = Comment19.objects.all().order_by('-created_at')
    return render(request, 'blokOneCss.html', {'form': form, 'comments': comments})

def blokTwoCss(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CommentForm20(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.save()
                return redirect('blokTwoCss')
        else:
            form = CommentForm20()
    else:
        form = None
    comments = Comment20.objects.all().order_by('-created_at')
    return render(request, 'blokTwoCss.html', {'form': form, 'comments': comments})

def oforOneCss(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CommentForm21(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.save()
                return redirect('oforOneCss')
        else:
            form = CommentForm21()
    else:
        form = None
    comments = Comment21.objects.all().order_by('-created_at')
    return render(request, 'oforOneCss.html', {'form': form, 'comments': comments})

def oforTwoCss(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CommentForm22(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.save()
                return redirect('oforTwoCss')
        else:
            form = CommentForm22()
    else:
        form = None
    comments = Comment22.objects.all().order_by('-created_at')
    return render(request, 'oforTwoCss.html', {'form': form, 'comments': comments})

def animOneCss(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CommentForm23(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.save()
                return redirect('animOneCss')
        else:
            form = CommentForm23()
    else:
        form = None
    comments = Comment23.objects.all().order_by('-created_at')
    return render(request, 'animOneCss.html', {'form': form, 'comments': comments})

def animTwoCss(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CommentForm24(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.save()
                return redirect('animTwoCss')
        else:
            form = CommentForm24()
    else:
        form = None
    comments = Comment24.objects.all().order_by('-created_at')
    return render(request, 'animTwoCss.html', {'form': form, 'comments': comments})

def adapOneCss(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CommentForm25(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.save()
                return redirect('adapOneCss')
        else:
            form = CommentForm25()
    else:
        form = None
    comments = Comment25.objects.all().order_by('-created_at')
    return render(request, 'adapOneCss.html', {'form': form, 'comments': comments})

def adapTwoCss(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CommentForm26(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.save()
                return redirect('adapTwoCss')
        else:
            form = CommentForm26()
    else:
        form = None
    comments = Comment26.objects.all().order_by('-created_at')
    return render(request, 'adapTwoCss.html', {'form': form, 'comments': comments})

def vstypTwoJs(request):
    return render(request, 'vstypTwoJs.html')

def vstypOneJs(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CommentForm27(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.save()
                return redirect('vstypOneJs')
        else:
            form = CommentForm27()
    else:
        form = None
    comments = Comment27.objects.all().order_by('-created_at')
    return render(request, 'vstypOneJs.html', {'form': form, 'comments': comments})

def vstypTwoJs(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CommentForm28(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.save()
                return redirect('vstypTwoJs')
        else:
            form = CommentForm28()
    else:
        form = None
    comments = Comment28.objects.all().order_by('-created_at')
    return render(request, 'vstypTwoJs.html', {'form': form, 'comments': comments})

def osnoviTwoJs(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CommentForm30(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.save()
                return redirect('osnoviTwoJs')
        else:
            form = CommentForm30()
    else:
        form = None
    comments = Comment30.objects.all().order_by('-created_at')
    return render(request, 'osnoviTwoJs.html', {'form': form, 'comments': comments})

def osnoviOneJs(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CommentForm29(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.save()
                return redirect('osnoviOneJs')
        else:
            form = CommentForm29()
    else:
        form = None
    comments = Comment29.objects.all().order_by('-created_at')
    return render(request, 'osnoviOneJs.html', {'form': form, 'comments': comments})

def functionsOneJs(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CommentForm32(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.save()
                return redirect('functionsOneJs')
        else:
            form = CommentForm32()
    else:
        form = None
    comments = Comment32.objects.all().order_by('-created_at')
    return render(request, 'functionsOneJs.html', {'form': form, 'comments': comments})

def cyclesOneJs(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CommentForm31(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.save()
                return redirect('cyclesOneJs')
        else:
            form = CommentForm31()
    else:
        form = None
    comments = Comment31.objects.all().order_by('-created_at')
    return render(request, 'cyclesOneJs.html', {'form': form, 'comments': comments})

def domTwoJs(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CommentForm34(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.save()
                return redirect('domTwoJs')
        else:
            form = CommentForm34()
    else:
        form = None
    comments = Comment34.objects.all().order_by('-created_at')
    return render(request, 'domTwoJs.html', {'form': form, 'comments': comments})

def domOneJs(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CommentForm33(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.save()
                return redirect('domOneJs')
        else:
            form = CommentForm33()
    else:
        form = None
    comments = Comment33.objects.all().order_by('-created_at')
    return render(request, 'domOneJs.html', {'form': form, 'comments': comments})

def objectOneJs(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CommentForm36(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.save()
                return redirect('objectOneJs')
        else:
            form = CommentForm36()
    else:
        form = None
    comments = Comment36.objects.all().order_by('-created_at')
    return render(request, 'objectOneJs.html', {'form': form, 'comments': comments})

def arrayOneJs(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CommentForm35(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.save()
                return redirect('arrayOneJs')
        else:
            form = CommentForm35()
    else:
        form = None
    comments = Comment35.objects.all().order_by('-created_at')
    return render(request, 'arrayOneJs.html', {'form': form, 'comments': comments})

def practiceTwoJs(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CommentForm38(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.save()
                return redirect('practiceTwoJs')
        else:
            form = CommentForm38()
    else:
        form = None
    comments = Comment38.objects.all().order_by('-created_at')
    return render(request, 'practiceTwoJs.html', {'form': form, 'comments': comments})

def practiceOneJs(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CommentForm37(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.save()
                return redirect('practiceOneJs')
        else:
            form = CommentForm37()
    else:
        form = None
    comments = Comment37.objects.all().order_by('-created_at')
    return render(request, 'practiceOneJs.html', {'form': form, 'comments': comments})

def advancedTwoJs(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CommentForm40(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.save()
                return redirect('advancedTwoJs')
        else:
            form = CommentForm40()
    else:
        form = None
    comments = Comment40.objects.all().order_by('-created_at')
    return render(request, 'advancedTwoJs.html', {'form': form, 'comments': comments})

def advancedOneJs(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CommentForm39(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.save()
                return redirect('advancedOneJs')
        else:
            form = CommentForm39()
    else:
        form = None
    comments = Comment39.objects.all().order_by('-created_at')
    return render(request, 'advancedOneJs.html', {'form': form, 'comments': comments})

def test_html_basic(request):
    return render(request, 'test_html_basic.html')

def test_html_advanced(request):
    return render(request, 'test_html_advanced.html')

def test_css_basic(request):
    return render(request, 'test_css_basic.html')

def test_css_layout(request):
    return render(request, 'test_css_layout.html')

def test_js_basic(request):
    return render(request, 'test_js_basic.html')

def test_js_dom(request):
    return render(request, 'test_js_dom.html')

def test_all(request):
    return render(request, 'test_all.html')
def testGlav(request):
    return render(request, 'testGlav.html')



import os, re, requests
from dotenv import load_dotenv
from django.shortcuts import render
from django.http import JsonResponse

load_dotenv()

def chat_page(request):
    return render(request, "chat.html")

def clean_answer(text):
    """Удаляем служебные теги вроде [OUT], [/s], и т.п."""
    if not text:
        return "🤖 Модель ничего не ответила."
    text = re.sub(r"\[/?[A-Z]+\]", "", text)
    return text.strip()

def ask_ai(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST-запросы только!"})

    user_message = request.POST.get("message", "").strip()
    if not user_message:
        return JsonResponse({"answer": "⚠️ Пожалуйста, введите сообщение."})

    # читаем ключ из окружения
    api_key = os.getenv("COHERE_API_KEY")
    model_name = os.getenv("COHERE_MODEL", "command-xlarge-nightly")
    if not api_key:
        return JsonResponse({"answer": "⚠️ COHERE_API_KEY не задан в окружении. Добавьте ключ в .env как COHERE_API_KEY=your_key"})

    try:
        import cohere

        client = cohere.Client(api_key)

        lang = (request.POST.get('lang') or request.GET.get('lang') or 'auto').lower()
        if lang == 'uk':
            system_prompt = (
                "Ти дружній і балакучий помічник. "
                "Відповідай природно, лаконічно та тільки українською мовою. "
                "Без службових тегів на кшталт [OUT] або [/s]."
            )
        elif lang == 'en':
            system_prompt = (
                "You are a friendly, conversational assistant. "
                "Answer naturally, concisely, and only in English. "
                "Do not include system tags like [OUT] or [/s]."
            )
        elif lang == 'pl':
            system_prompt = (
                "Jesteś przyjaznym i rozmownym asystentem. "
                "Odpowiadaj naturalnie, zwięźle i wyłącznie po polsku. "
                "Nie używaj znaczników systemowych typu [OUT] czy [/s]."
            )
        else:
 
            system_prompt = (
                "Detect the user's language from the message and reply in that language. "
                "If the user's language is Russian, do NOT reply in Russian — reply in Ukrainian instead. "
                "Answer naturally and concisely. Do not include system tags like [OUT] or [/s]."
            )

        # Cohere API
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message},
        ]

        try:
            resp = client.chat(
                message=user_message,
                preamble=system_prompt,
                model=model_name,
                max_tokens=400,
                temperature=0.7,
            )

            raw = None
            if hasattr(resp, 'message'):
                raw = getattr(resp.message, 'content', None) or getattr(resp.message, 'content', '')
            if not raw and hasattr(resp, 'output'):
                raw = getattr(resp, 'output', None)
            if not raw and hasattr(resp, 'generations'):
                raw = "".join([g.text for g in resp.generations])
            if not raw and hasattr(resp, 'text'):
                raw = getattr(resp, 'text', None)
            if raw is None:
                raw = str(resp)

            answer = clean_answer(raw)
            return JsonResponse({"answer": answer})

        except Exception as e:
            return JsonResponse({"answer": f"Ошибка Cohere Chat API: {str(e)}"})

    except Exception as e:
        return JsonResponse({"answer": f"Ошибка инициализации Cohere: {str(e)}"})
