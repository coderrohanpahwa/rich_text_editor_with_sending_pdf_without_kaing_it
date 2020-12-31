from django.core.files.base import ContentFile
from django.shortcuts import render
from .forms import PostForm,Post,Client,ClientForm,VendorForm,Vendor,NumberOfPhasesForm,NumberOfPhases,NumberOfPhasesInlineForm
from django.http import HttpResponse
from .models import Match,NumberOfPhases,Client
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.http import HttpResponse
from django.views.generic import View
from .utils import render_to_pdf
from django.http import HttpResponseRedirect
from django.contrib import messages
from post_office import mail
import PyPDF2

import datetime
# Create your views here.
def index(request):
    if request.method=="POST":
        fm=PostForm(request.POST)
        if fm.is_valid():
            # print(fm.cleaned_data['content'])
            fm.save()
            return HttpResponse("Your data has been saved")
    fm=PostForm()
    return render(request,'api/index1.html',{'form':fm})
def send(request):
    subject = 'Subject'
    # html_message = render_to_string('mail_template.html', {'context': 'Rohan Pahwa'})
    obj=Post.objects.get(id=1)
    # print(obj.content)
    html_message = render_to_string('api/send.html', {'context': obj.content})
    plain_message = strip_tags(html_message)
    from_email = 'hackerrohanpahwa@gmail.com'
    to = 'rohanpahwa1@gmail.com'
    mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)
    return HttpResponse("Sent")
class GeneratePdf(View):
    def get(self, request ,id,*args, **kwargs):
        obj=Post.objects.get(id=id)
        # print(obj.content)
        # Jo buyer requirements dalega cke editor me vo yhn se aaenge
        client_obj=Client.objects.get(post=obj)
        vendor_obj=Vendor.objects.get(id=1)
        match_obj=Match.objects.get(client=client_obj,vendor=vendor_obj)
        #Number of phases wali requirements
        obj_phase=NumberOfPhases.objects.filter(macth=match_obj)
        # print(obj_phase)

        data={'data':obj.content,'data_o':obj_phase}
        '''This code is for only generating pdfs in a browser'''
        pdf = render_to_pdf('pdf/index.html', data)
        # return HttpResponse(pdf, content_type='application/pdf')

        # print(type(pdf))

        # print(pdf.getvalue())
        # print(dir(pdf))
        # print(pdf)
        mail.send('rohanpahwa1@gmail.com',
                  'hackerrohanpahwa@gmail.com',
                  attachments={'pdf.pdf':ContentFile(pdf.getvalue())}
                      )

        return HttpResponse("Sent")

# <--------   Iske bd ka sara database design wali backchodi hai --------------------->

def clientForm(request):
    if request.method=="POST":
        fm=ClientForm(request.POST)
        if fm.is_valid():
            fm.save()
    fm=ClientForm()
    return render(request,'api/clientform.html',{'form':fm})
def vendorForm(request):
    if request.method=="POST":
        fm=VendorForm(request.POST)
        if fm.is_valid():
            fm.save()
    fm=VendorForm()
    return render(request,'api/vendorform.html',{'form':fm})
def match_view(request):
    data={'client_obj':Client.objects.get(id=1),'vendor_obj':Vendor.objects.all()}
    return render(request,'api/match_view.html',data)
def match_client_vendor(request,cid,vid):
    try:
        client_obj=Client.objects.get(id=cid)
        vendor_obj=Vendor.objects.get(id=vid)
        # print("id",type(Match.objects.get(id=1)))
        if client_obj is not None and vendor_obj is not None:
            obj=Match(client=client_obj,vendor=vendor_obj)
            obj.save()
            messages.success(request,"You have successfully matched vendor")
    except:
        messages.error(request,"You have already matched with this vendor")
    return HttpResponseRedirect('/matchview')

def number_of_phases(request,cid,vid):
    if request.method=="POST":
        client_obj=Client.objects.get(id=cid)
        vendor_obj=Vendor.objects.get(id=vid)
        macth=Match.objects.get(client=client_obj,vendor=vendor_obj)
        # obj=NumberOfPhases(phase=phase,description=description,timeline=timeline,payments=payments,macth=macth)
        # obj.save()
        # print(request.POST)
        # print(request.POST.getlist('phase'))
        for i in range(len(request.POST.getlist('phase'))):
            phase=request.POST.getlist('phase')[i]
            description=request.POST.getlist('description')[i]
            timeline=request.POST.getlist('timeline')[i]
            payments=request.POST.getlist('payments')[i]
            obj=NumberOfPhases(phase=phase,description=description,timeline=timeline,payments=payments,macth=macth)
            obj.save()

    # print(fm)
    return render(request,'api/number_of_phases_again.html')
def get_phases(request,cid,vid):
    client_obj=Client.objects.get(id=cid)
    vendor_obj=Vendor.objects.get(id=vid)
    match_obj=Match.objects.get(client=client_obj,vendor=vendor_obj)
    obj=NumberOfPhases.objects.filter(macth=match_obj)

    return render(request,'api/get_phases.html',{'data':obj})