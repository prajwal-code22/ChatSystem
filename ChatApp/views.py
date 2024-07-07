from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import ChatMessagesCreateForm
# Create your views here.
def chat_view(request):
    chat_groups=get_object_or_404(ChatGroup,group_name="techsayatri")
    chat_messages=chat_groups.chat_messages.all()[:20]
    form=ChatMessagesCreateForm()
    if request.htmx:
        form=ChatMessagesCreateForm(request.POST)
        if form.is_valid():
            message=form.save(commit=False)
            message.author=request.user
            message.group= chat_groups
            message.save()
            context={
                'message':message,
                'user':request.user
            }
            return render(request,'ChatApp/Partials/chat_message_p.html',context)

    return render(request,'ChatApp/chat.html',{'messages':chat_messages,'form':form})