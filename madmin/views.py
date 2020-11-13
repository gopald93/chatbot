from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,reverse,redirect,get_object_or_404
from Chatbot.decorators import admin_only,allowed_user
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from madmin.common_methods import (auto_generated_bank_id,validation_for_user_signup,create_main_user,create_bank_configuration,create_bot_details,create_custom_user,prepare_teammates_data,
								invite_teammates_processing,chat_widget_dict,bot_details_update_methods)
from django.db.models import Q
from madmin.models import (Bank_Configuration,Default_Image_Icon_Gallery,Bot_Details,Custom_User_Model)

def user_signup(request):
	if request.method == 'POST':
		messages_info=validation_for_user_signup(request)
		if messages_info is None:
			main_user_obj=create_main_user(username=request.POST.get('username'),password=request.POST.get('password'),email=request.POST.get('email'),first_name=request.POST.get('full_name'))
			bank_obj=create_bank_configuration()
			bot_obj=create_bot_details(bank_obj)
			create_custom_user(user=main_user_obj,bot_id=bot_obj,bankid=None,urole='1')
			return redirect('user_login')
		else:
			messages.info(request,messages_info)
	return render(request, "madmin/signup.html")       

def user_login(request):
	if request.user.is_authenticated:
		custom_user_obj=Custom_User_Model.objects.get(user=request.user)
		bank_obj=Bank_Configuration.objects.get(bnk_id=custom_user_obj.bankid)
		if custom_user_obj.urole=='1':
			return redirect('madmin_dashboard',bname=bank_obj.bnk_name)
		else:
			return redirect('conversation',bname=bank_obj.bnk_name)
	else:    
		if request.method == 'POST':
			user = authenticate(request,username=request.POST.get('username'),password=request.POST.get('password'))
			if user is not None:
				login(request,user)
				custom_user_obj=Custom_User_Model.objects.get(user=request.user)
				bank_obj=Bank_Configuration.objects.get(bnk_id=custom_user_obj.bankid)
				if custom_user_obj.urole=='1':
					return redirect('madmin_dashboard',bname=bank_obj.bnk_name)
				else: 
					return redirect('conversation',bname=bank_obj.bnk_name)
			else:
				messages_info='Username OR password is incorrect'
				messages.info(request,messages_info)
	return render(request,"madmin/login.html")

@login_required(login_url="/user_login/")
def user_logout(request):
	logout(request)
	return redirect('user_login')

@login_required(login_url="/user_login/")	
@admin_only
def madmin_dashboard(request,bname=None):
	context={}
	context["bname"]=bname
	return render(request,"madmin/madmin_dashboard.html",context)

@login_required(login_url="/user_login/")
@admin_only
def chat_widget(request,bname=None):
	html_page="madmin/chat-widget_second.html"
	context=chat_widget_dict(request.user.username)
	context["bname"]=bname
	if request.method=='POST':
		
		if "chat_hist_form" in request.POST:
			updated_field_dict={"cf_hx_rml":request.POST.get("cf_hx_rml"),"cf_rml_dys":request.POST.get("cf_rml_dys"),"cf_rml_hrs":request.POST.get("cf_rml_hrs"),"cf_rml_mnts":request.POST.get("cf_rml_mnts")}
			context=bot_details_update_methods(context,updated_field_dict)

		elif "chat_delayed_form" in request.POST:
			updated_field_dict={"cf_rpls_dly":request.POST.get("cf_rpls_dly")} 
			context=bot_details_update_methods(context,updated_field_dict)

		elif "chat_disp_form" in request.POST:
			updated_field_dict={"cf_dply_inditr":request.POST.get("cf_dply_inditr")} 
			context=bot_details_update_methods(context,updated_field_dict)	

		elif "chat_widget_look" in request.POST:
			updated_field_dict={'ct_pos':request.POST.get('ct_pos'),'ct_clr':request.POST.get('ct_clr'),'dflt_icn':request.POST.get('dflt_icn'),'ct_cstm_icn':request.POST.get("custom-icon-url")} 
			context=bot_details_update_methods(context,updated_field_dict)
			
		elif "chat_widget_sound" in request.POST:
			updated_field_dict={"ct_ntn_snd":request.POST.get("ct_ntn_snd")}
			context=bot_details_update_methods(context,updated_field_dict)
		
		else:
			return render(request,"madmin/chat-widget.html",context) 
	return render(request,"madmin/chat-widget.html",context)

@login_required(login_url="/user_login/")
@admin_only
def teammates(request,bname=None):
	context=prepare_teammates_data(request.user)
	context["bname"]=bname
	if request.method == 'POST':
		if "company_update" in request.POST:
			Bank_Configuration.objects.filter(bnk_id=context.get("bank_info_obj").bnk_id).update(
				bnk_name=request.POST.get('bnk_name'),bnk_urls=request.POST.get('bnk_urls'),
				max_act_user=request.POST.get('max_act_user'))
			return redirect('madmin_dashboard',bname=bname)
		if "invite_teammates" in request.POST:
			invite_teammates_processing(request,context)
			return redirect('madmin_dashboard',bname=bname)
	return render(request,"madmin/company.html",context)

@login_required(login_url="/user_login/")	
@admin_only
def user_data(request,bname=None):
	context={}
	context["bname"]=bname
	return render(request,"madmin/users.html",context)	
