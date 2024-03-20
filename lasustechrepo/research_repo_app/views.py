
from django.shortcuts import get_object_or_404, render, redirect
from .forms import ThesisForm, ResearchPaperForm, ResearchDataForm
from .models import Thesis, ResearchPaper, ResearchData
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to the desired page after login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def submit_research_data(request):
    
    form = ResearchDataForm(request.POST, request.FILES)
    if form.is_valid():
        data = request.FILES.getlist('research_data')
        author = request.user
        for d in data:
            image_ins = ResearchData(research_data=d, author=author)
            image_ins.save()
        return redirect('index')
    
    context = {'form': form}
    return render(request, "submit_research_data.html", context)

def index(request):
    return render(request,'index.html')

@login_required
def submit_thesis(request):
    if request.method == 'POST':
        form = ThesisForm(request.POST, request.FILES)
        if form.is_valid():
            research_paper = form.save(commit=False)
            research_paper.author = request.user
            research_paper.save()
            return redirect('submit_thesis')
    else:
        form = ThesisForm()
    return render(request, 'submit_thesis.html', {'form': form})

@login_required
def submit_research_paper(request):
    if request.method == 'POST':
        form = ResearchPaperForm(request.POST, request.FILES)
        if form.is_valid():
            research_paper = form.save(commit=False)
            research_paper.author = request.user
            research_paper.save()
            return redirect('submit_research_data')
    else:
        form = ResearchPaperForm()
    return render(request, 'submit_research_paper.html', {'form': form})

@login_required
def submit_research_data(request):
    if request.method == 'POST':
        form = ResearchDataForm(request.POST, request.FILES)
        if form.is_valid():
            research_data = form.save(commit=False)
            research_data.author = request.user
            research_data.save()
            return redirect('submit_research_data')
    else:
        form = ResearchDataForm()
    return render(request, 'submit_research_data.html', {'form': form})

def research_list(request):
    research_papers = ResearchPaper.objects.all()
    return render(request, 'research_list.html', {'research_papers': research_papers})


def research_details(request, paper_id):
    research_paper = get_object_or_404(ResearchPaper, pk=paper_id)
    associated_research_data = ResearchData.objects.filter(title=research_paper)
    return render(request, 'research_details.html', {'research_paper': research_paper, 'associated_research_data': associated_research_data})
