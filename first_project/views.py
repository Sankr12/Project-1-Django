from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import userForms
from service.models import Service
from News.models import news
from django.core import paginator
from django.core.paginator import Paginator
from ContactEnquiry.models import contactform
from django.core.mail import send_mail



def homepage(request):
 
    # send_mail(
    #     "Testing Mail",
    #     "Here is the message.",
    #     "from",
    #     ["to"],
    #     fail_silently=False,
    # )
    servicedata = Service.objects.all().order_by('service_title')[0:7]
    newsdata = news.objects.all()
    # for a in servicedata:
    #     print(a.service_icon)
    data = {
        'servicedata':servicedata,
        'newsdata':newsdata
    }
    return render(request, "index.html", data)



def Newsdetails(request,slug):
    newsdetails=news.objects.get(news_slug=slug)
    data = {
        'newsdetails':newsdetails
    }
    return render(request,"newsdetails.html",data)



def AboutUs(request):
    if request.method=="GET":
        name = request.GET.get('name')
        contact = request.GET.get('contact')
        people = request.GET.get('people')
        message = request.GET.get('message')

        output = f'Name: {name}<br> Contact: {contact}<br> People: {people}<br> Message: {message}'\
        f'<p style="font-size: 36px; text-align: center;">Thank You!</p>'
        return HttpResponse(output)
    return HttpResponse('This is a GET request')




def course(request):
    return HttpResponse('Choose your course and complete the payment')



def  coursedetails(request, courseid):
    return HttpResponse(courseid)



def userform(request):
    my_form = userForms()
    data={'form':my_form}
    try:
        if request.method=="POST":
            n1 = request.POST.get('value1')
            n3 = request.POST.get('value3')
            n2 = request.POST.get('value2')
            n4 = request.POST.get('value4')
            data = {
                'n1':n1,
                'n2':n2,
                'n3':n3,
                'n4':n4,
                'form':my_form
            }
            url="/about-us/?name={}&contact={}&people={}&message={}".format(my_form.name,my_form.contact,my_form.people,my_form.message)    
            return HttpResponseRedirect(url)
    except:
        pass
    return render(request,"userform.html",data)



def submitform(request):
    data={}
    try:
        if request.method=="POST":
            n1 = request.POST.get('value1')
            n3 = request.POST.get('value3')
            n2 = request.POST.get('value2')
            n4 = request.POST.get('value4')
            data = {
                'n1':n1,
                'n2':n2,
                'n3':n3,
                'n4':n4
            }
    
        output = f'Name: {n1}<br> Contact: {n2}<br> People: {n3}<br> Message: {n4}'\
        f'<p style="font-size: 36px; text-align: center;">Thank You!</p>'
        return HttpResponse(output)
    except:
        pass



def calculator(request):
    c = ''
    try:
        if request.method == "POST":
            n1 = eval(request.POST.get('num1'))
            n2 = eval(request.POST.get('num2'))
            option = request.POST.get('option')
            if option == "+":
                c = n1 + n2
            elif option == "-":
                c = n1 - n2
            elif option == "×":
                c = n1 * n2
            elif option == "÷":
                if n2 != 0:  # Avoid division by zero
                    c = n1 / n2
                else:
                    c = "Error: Division by zero"
        else:
            c = "Please submit the form."
    except Exception as e:
        c = f"An error occurred: {e}"

    return render(request, "calculator.html", {"c": c})



def checkevenodd(request):
    c=''
    if request.method == "POST":
        if request.POST.get('num1')=="":
            return render(request, "evenodd.html", {'error':True})
        num = eval(request.POST.get('num1'))  # Convert to integer
        if num % 2 == 0:
            c = 'Even'
        else:
            c = 'Odd'
    return render(request, "evenodd.html", {'c': c})



def marksheet(request):
    data={}
    p=0
    t=0
    d=''
    try:
        if request.method=="POST":
            s1=eval(request.POST.get('subject1'))
            s2=eval(request.POST.get('subject2'))               
            s3=eval(request.POST.get('subject3'))
            s4=eval(request.POST.get('subject4'))
            s5=eval(request.POST.get('subject5'))
            t=s1+s2+s3+s4+s5
            p=t/5
            if p>80:
                d='First Division'
            elif p>70:
                d="Second Division"
            elif p>60:
                d="Third Division"
            else:
                d="Forth Division"
        data = {
            'total':t,
            'percentage':p,
            'division':d
        }
    except Exception as e:
        data = f"Error occurred: {e}"
    return render(request, 'marksheet.html', data)



# def services(request):
#     servicedata = Service.objects.all()
#     if request.method=='GET':
#         st=request.GET.get('servicename')
#         if st!=None:
#             servicedata = Service.objects.filter(service_icon__icontains=st)
#     data = {
#         'servicedata':servicedata,
#     }
#     return render(request, "index.html", data)


def services(request):
    servicedata = Service.objects.all()
    paginator=Paginator(servicedata,1)
    page_number=request.GET.get('page')
    servicedatafinal = paginator.get_page(page_number)
    totalpage = servicedatafinal.paginator.num_pages

    data = {
        'servicedata':servicedatafinal,
        'lastpage':totalpage,
        'totalpagelist':[n+1 for n in range(totalpage-1)]
    }
    return render(request,'index.html',data)

def saveEnquiry(request):
    if request.method=="POST":
        name=request.POST.get('name')
        contact=request.POST.get('contact')
        people=request.POST.get('people')
        message=request.POST.get('message')
        en=contactform(Name=name,Contact=contact,People=people,Message=message)
        en.save()
    return render(request,'index.html')

# ...

def saveEnquiry(request):
    if request.method == "POST":
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        people = request.POST.get('people')
        message = request.POST.get('message')
        
        en = contactform(Name=name, Contact=contact, People=people, Message=message)
        en.save()
        
        # Redirect to a different page after successful submission # Replace 'success_page' with the actual URL name

    return render(request, 'index.html')