from logging import PercentStyle
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.http import request
from django.views import View

from myface_project.settings import MEDIA_ROOT, MEDIA_URL
from .models import PhotoList
from .forms import PhotoListForm
from .train import train
# os.chmod("./media/photo/", 755)
def top(request):
    
    return render(request, 'top.html')

# class next(TemplateView):
#     def get_context_data(self,**kwargs):
#         context = super().get_context_data(**kwargs)
#         img = request.POST.get("img")
#         context["img"] = img
#         return render(request, 'next.html' , context)


def next(request):
    return render(request, 'next.html')

import glob
ALLOWED_MIME = [ "application/pdf" ]

class PhotoView(View):

    def get(self, request, *args, **kwargs):

        data    = PhotoList.objects.all()
        form    = PhotoListForm()

        context = { "data":data,
                    "form":form,
                    }

        return render(request,"index.html",context)

    def post(self, request, *args, **kwargs):
        
        form = PhotoListForm(request.POST, request.FILES)
        if form.is_valid():
            print("バリデーションOK")
            form.save()
        data = PhotoList.objects.all().reverse()
        photo = request.FILES["photo"].name
        print(photo)
        # data = data.reverse()
        data = train().loop(f"./media/photo/{photo}") # ＜-選択されたファイルのパスが必要train.py
        percent = round(data[0], 2) * 100
        name = data[1]
        context = { "data":data,
                    "form":form,
                    "percent":int(percent),
                    "name":name,
                    }
        return render(request, "next.html", context)

index = PhotoView.as_view()

# class DocumentView(View):

#     def get(self, request, *args, **kwargs):

#         data    = DocumentList.objects.all()
#         form    = DocumentListForm()
#         context = { "data":data,
#                     "form":form,
#                     }

#         return render(request,"document.html",context)

#     def post(self, request, *args, **kwargs):
#         import magic
#         ALLOWED_MIME = [ "application/pdf" ]
#         form        = DocumentListForm(request.POST,request.FILES)
#         mime_type   = magic.from_buffer(request.FILES["document"].read(1024) , mime=True)

#         if form.is_valid():
#             print("バリデーションOK")

#             if mime_type in ALLOWED_MIME:
#                 form.save()
#             else:
#                 print("このファイルは許可されていません。")


#         return redirect("udocument")

# document    = DocumentView.as_view()
