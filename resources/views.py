from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.template import loader

from .models import Resource
from .models import Upvotes
from .forms import ResourceForm
from .forms import FilterForm

from django.db.models import Sum

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  # Redirect to your home page or any desired page after registration
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            from django.contrib.auth import login
            login(request, form.get_user())
            return redirect('/studyres/')
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})

@login_required(login_url='/studyres/login')
def logout_view(request):
    logout(request)
    return redirect("/studyres/")

@login_required(login_url='/studyres/login')
def saveResource(request):
    if request.method == "POST":
        form = ResourceForm(request.POST)
        if form.is_valid():
            title_inp = form.cleaned_data['title']
            course_inp = form.cleaned_data['course']
            type_inp = form.cleaned_data['type']
            url_inp = form.cleaned_data['url']
            semester = form.cleaned_data['semester']
            current_user = request.user
            user_id = current_user.id
            res = Resource(user_id = user_id, title= title_inp, course = course_inp, type = type_inp, semester = semester, url = url_inp)
            res.save()
            return redirect('/studyres/confirmation/')  
    else:
        form = ResourceForm()
    return render(request, "resources/post2.html", {"form": form})

@login_required(login_url='/studyres/login')
def home_view(request):
    if request.method == "POST":
        form = FilterForm(request.POST)
        if form.is_valid():
            course_inp = form.cleaned_data['course']
            type_inp = form.cleaned_data['type']
            up_inp = form.cleaned_data['upvotes']
            date_inp = form.cleaned_data['date']
            result = Resource.objects
            if course_inp is not '':
                result = result.filter(course = course_inp)
            if type_inp is not '':
                result = result.filter(type= type_inp)
            if up_inp is not '':
                if up_inp == 'Descending':
                    result = result.order_by('-upvotes')
                else:
                    result = result.order_by('upvotes')
            if date_inp is not '':
                if date_inp == 'Descending':
                    result = result.order_by('-date')
                else:
                    result = result.order_by('date')
            result = result.select_related('user')
            return render(request, 'resources/result.html', {'data': result})
    else:
        form = FilterForm()
    allRes = Resource.objects.all()
    allRes = allRes.select_related('user')
    return render(request, "resources/home.html", {"form": form, "all": allRes})

def profile_view(request):
    current_user = request.user
    id = current_user.id
    ownPosts = Resource.objects.filter(user_id = id)
    ownPosts = ownPosts.select_related('user')
    totPosts = ownPosts.count()
    agg = Resource.objects.aggregate(
    totalUpvotes=Sum("upvotes", default = 0),
    )
    totUpvotes = agg["totalUpvotes"]
    return render(request, "resources/profile.html", {"totalUpvotes": totUpvotes, "totalPosts": totPosts, "all": ownPosts})

def resource_view(request, id):
    current_user = request.user
    uid = current_user.id
    resource = Resource.objects.filter(sl_no = id).first()
    resource.clicks += 1
    resource.save()
    votedRes = Upvotes.objects.filter(user_id= uid).filter(res_no = id)
    count = votedRes.count()
    if count < 1:
        canVote = True
    else:
        canVote = False
    return render(request, "resources/resource.html", {"res": resource, "id":id, "canVote": canVote})

def upvote(request, id):
    current_user = request.user
    uid = current_user.id
    resource = Upvotes.objects.filter(user_id= uid).filter(res_no = id)
    count = resource.count()
    if count<1:
        resource = Resource.objects.filter(sl_no = id).first()
        resource.upvotes += 1
        resource.save()
        upvote = Upvotes(res_no = id, user_id = id)
        upvote.save()
    return redirect('/studyres/resource/'+str(id))

@login_required(login_url='/studyres/login')
def confirmation(request):
    template = loader.get_template("resources/confirmation.html")
    return HttpResponse(template.render(None,request))