from django.shortcuts import render
from .models import Message,Group,UserID
from .forms import MessageForm,MessageTestForm
from linebot import LineBotApi
from linebot.models import TextSendMessage
from .AccessToken import channel_access_token
# Create your views here.
def showtemplate(request):
    message_list = Message.objects.all()
    context = {'message_list': message_list}
    
    return render(request, 'MessageSet.html', context)

def Message_create_view(request):
    form = MessageForm(request.POST or None)
    if form.is_valid():
        form.save()

        form = MessageForm()

    context = {'form': form}
    return render(request, "MessageCreate.html", context)

def MessagePush(request):
    form = MessageForm(request.POST or None)
    if form.is_valid():
        form.save()

    response = request.POST
    group_id = response['group']
    message_title = response['message_title']
    text = response['message_push']
    group_id_query = Group.objects.get(id=group_id).group
    print(response)
    post=[group_id_query,message_title,text]
    print(group_id)
    print(text)
    print(group_id_query)
    
    user_id_query = UserID.objects.filter(group = group_id)
    user_id_list = list(user_id_query.values())
    user_id=[]
    for user in user_id_list:
        user_id.append(user.get('user_id'))

    print(user_id_query)
    print(user_id_list)
    print(user_id)

    line_bot_api = LineBotApi(channel_access_token)
    for user in user_id:
        line_bot_api.push_message(user,TextSendMessage(text=text))
    
    return render(request,"MessageSend.html",locals())

def MessageCreateTest_Create(request):
    form = MessageTestForm(request.POST or None)
    if form.is_valid():
        form.save()

        form = MessageTestForm()

    context = {'form': form}
    return render(request,'MessageCreateTest_Create.html',context)
    #response = request.POST or None
    #user_id = response['user_id']
    #text = response['text']

    
    
def MessageCreateTest_Send(request):
    form = MessageTestForm(request.POST or None)
    if form.is_valid():
        form.save()
    response = request.POST or None
    user_id = response['user_id']
    text = response['text']    

    print(user_id,text)
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.push_message(user_id,TextSendMessage(text=text))
    return render(request,"MessageCreateTest_Send.html")
