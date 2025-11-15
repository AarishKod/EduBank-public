from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, PartnerForm, BotForm, OrgForm, AvaForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Partner
from openai import OpenAI
from time import sleep
from django.shortcuts import HttpResponse
from dotenv import load_dotenv
import os

# Create your views here.

def register (request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
    context = {'registerform': form}
    return render(request, 'register.html', context)

def login (request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
    context = {'loginform': form}
    return render(request, 'login.html', context)

def dashboard (request):
    return render(request, "dashboard.html")

def user_logout (request):
    auth.logout(request)
    # return redirect("login")
    return render(request, 'logout.html')

def view_data (request):
    all_partners = Partner.objects.all
    consultative_partners = Partner.objects.filter(organization_Type = "Consultative Partnerships")
    contributory_partners = Partner.objects.filter(organization_Type = "Contributory Partnerships")
    operational_partners = Partner.objects.filter(organization_Type = "Operational Partnerships")
    collaborative_partners = Partner.objects.filter(organization_Type = "Collaborative Partnerships")

    form = OrgForm()
    form1 = AvaForm()

    context = {
        "all": all_partners,
        'consultative': consultative_partners,
        'contributory': contributory_partners,
        'operational': operational_partners,
        'collaborative': collaborative_partners,
        "orgform": form,
        'avaform': form1,
    }

    if 'form-1-submit' in request.POST:
        form = OrgForm(request.POST or None)
        if form.is_valid():
            ait = Partner.objects.filter(organization_Type = request.POST.get('organization_type'))
        
        context = {
            "all": ait,
            'consultative': consultative_partners,
            'contributory': contributory_partners,
            'operational': operational_partners,
            'collaborative': collaborative_partners,
            "orgform": form,
            'avaform': form1,
        }

        return render(request, 'dataview.html', context)
    
    if 'form-2-submit' in request.POST:
        form1 = AvaForm(request.POST or None)
        if form1.is_valid():
            ait = Partner.objects.filter(available_Resources = request.POST.get('available_resources'))

        context = {
                    "all": ait,
                    'consultative': consultative_partners,
                    'contributory': contributory_partners,
                    'operational': operational_partners,
                    'collaborative': collaborative_partners,
                    "orgform": form,
                    'avaform': form1,
        }
        
        return render(request, 'dataview.html', context)




    return render(request, 'dataview.html', context)

def add_data (request):
    form = PartnerForm()
    if request.method == 'POST':
        form = PartnerForm(request.POST or None)
        if form.is_valid():
            form.save()
        context = {'partnerform': form}
        return render(request, 'created.html', context)
    else:
        context = {'partnerform': form}
        return render(request, "datacreate.html", context)
    

def delete_data (request):
    return render(request, 'datadelete.html')

def modify_data (request):
    return render(request, 'datadelete.html')

def ai_assistant (request):
    load_dotenv()
    display = False
    form = BotForm()
    ASSISTANT_ID = f"{os.getenv('assistant_key')}"
    client = OpenAI(api_key=f"{os.getenv('api_key1')}")

    if request.method == 'POST':
        display = True
        form = BotForm(request.POST or None)
        ait = ''
        if form.is_valid():
            ait = request.POST.get('prompt')
            thread = client.beta.threads.create(
                messages=[
                    {
                    "role": "user",
                    "content": ait,
                    }
                ]
            )

        # submit thread to assistant
        run = client.beta.threads.runs.create(thread_id=thread.id, assistant_id=ASSISTANT_ID)
        print(f"Run created: {run.id}")

        # waiting for run to complete
        while run.status != "completed":
            run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
            print(run.status)
            sleep(1)
        else:
            print("run completed")

        message_response = client.beta.threads.messages.list(thread_id=thread.id)
        messages = message_response.data
        latest_message = messages[0]

        context = {
            "message": latest_message.content[0].text.value,
            "form": form,
            "input": ait,
            "display": display,
        }
        return render(request, 'help.html', context)
    else:
        context = {
            "form": form,
            "display": display,
        }
        return render(request, 'help.html', context)