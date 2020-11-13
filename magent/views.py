from django.http import HttpResponse,HttpResponseRedirect
from Chatbot.decorators import admin_only,allowed_user
from django.shortcuts import render,reverse,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from madmin.models import *
@login_required(login_url="/user_login/")	
@allowed_user(allowed_roles=['1','2','3'])
def conversation(request,bname=None):
	return render(request,"magent/conversation.html")