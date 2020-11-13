import attr
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import make_password, check_password
from django.db.models import Q
from django.contrib.auth.models import User
from madmin.models import (Bank_Configuration,Default_Image_Icon_Gallery,Bot_Details,Custom_User_Model)

def auto_generated_bank_id():
	generated_bankid = None
	bank_id_dict_obj=Custom_User_Model.objects.values('bankid').distinct()
	if not bank_id_dict_obj:
		generated_bankid = 'B' + '-' + '0000'
	else:
		bank_id_list=[]	
		for bank_id in bank_id_dict_obj:
			bank_id_list.append(int((bank_id.get("bankid"))[2:6]))	
		latest_bank_id=max(bank_id_list)
		generated_bankid = 'B' + '-' + str(int(latest_bank_id) + 1).zfill(4)
	return generated_bankid

def validation_for_user_signup(request):
	try:
		user_obj=User.objects.get(Q(username=request.POST.get('username')) | Q(email=request.POST.get('email')))
		if user_obj.username==request.POST.get('username'):
			messages_info='Username is already available'
		elif user_obj.email==request.POST.get('email'):
			messages_info="Email is already registered"
		else:
			messages_info='Something went wrong'	
	except User.DoesNotExist:
		messages_info=None
	return messages_info

def create_main_user(**kwagrs):
	main_user_obj=User.objects.create(username=kwagrs.get("username"),password=make_password(kwagrs.get('password')),
		email=kwagrs.get('email'),first_name=kwagrs.get('first_name',None),is_active=True)
	return main_user_obj

def create_bank_configuration():
	bank_obj=Bank_Configuration.objects.create(bnk_id=auto_generated_bank_id())
	return bank_obj

def create_bot_details(bank_obj):
	bot_obj=Bot_Details.objects.create(bnk_id=bank_obj)
	return bot_obj

def create_custom_user(**kwagrs):
	if  kwagrs.get("bankid") is None:
		kwagrs["bankid"]=auto_generated_bank_id()
	custom_user_obj=Custom_User_Model.objects.create(user=kwagrs.get("user"),urole=kwagrs.get("urole"),bot_id=kwagrs.get("bot_id"),bankid=kwagrs.get("bankid"))

def get_urole_expression(urole):
	urole_expression=None
	if urole=="1":
		urole_expression='super admin'
	elif urole=="2":
		urole_expression='teammate'
	else:
		urole_expression='operator'
	return urole_expression

@attr.s
class User_Info(object):
	name=attr.ib()
	email_id=attr.ib()
	agent_id=attr.ib()
	team=attr.ib()
	role=attr.ib()
	status=attr.ib()
	is_active=attr.ib()

@attr.s
class Bank_Info(object):
	bnk_name= attr.ib()
	bnk_urls= attr.ib()
	bnk_dbrd_urls= attr.ib()
	max_act_user= attr.ib()
	bnk_id= attr.ib()
	bank_user_list= attr.ib(default=attr.Factory(list))

# custom_user_obj=Custom_User_Model.objects.select_related('user','bot_id','bot_id__cid').get(user=request.user)
def prepare_teammates_data(user):
	context={}
	login_user_bot_id=None
	login_user_bank_id=None
	custom_user_obj=Custom_User_Model.objects.select_related('user','bot_id__bnk_id').filter(bankid=user.custom_user_model.bankid)
	all_bank_user=[]
	for user_obj in custom_user_obj:
		status="Offline"
		if user.username == user_obj.user.username:
			status="Online"
			bank_info_obj = Bank_Info(
				bnk_name=user_obj.bot_id.bnk_id.bnk_name,
				bnk_urls=user_obj.bot_id.bnk_id.bnk_urls,
				bnk_dbrd_urls=user_obj.bot_id.bnk_id.bnk_dbrd_urls,
				max_act_user=user_obj.bot_id.bnk_id.max_act_user,
				bnk_id=user_obj.bot_id.bnk_id.bnk_id,
				bank_user_list=[],)
			login_user_bot_id=user_obj.bot_id
			login_user_bank_id=user_obj.bankid
		user_info_obj = User_Info(
			name= user_obj.user.username,
			email_id=user_obj.user.email,
			agent_id=user_obj.bankid,
			team="team",
			role=get_urole_expression(user_obj.urole),
			status=status,
			is_active=user_obj.user.is_active,
			)
		all_bank_user.append(user_info_obj)	
	context["login_user_bot_id"]=login_user_bot_id
	context["login_user_bank_id"]=login_user_bank_id
	bank_info_obj.bank_user_list=all_bank_user
	context["bank_info_obj"]=bank_info_obj
	context["bot_count"]=0
	context["total_team"]=1
	return context

def chat_widget_dict(username):
	default_image_icon_gallery_obj=Default_Image_Icon_Gallery.objects.all()
	bot_obj=Bot_Details.objects.get(custom_user_model__user__username=username)
	context={
		"bot_id":bot_obj.bot_id,
		"bnk_id":bot_obj.bnk_id,
		"ct_pos":bot_obj.ct_pos,
		"ct_clr":bot_obj.ct_clr,
		"dflt_icn":bot_obj.dflt_icn,
		"ct_cstm_icn":bot_obj.ct_cstm_icn,
		"ct_ntn_snd":bot_obj.ct_ntn_snd,
		"default_img_model_obj":default_image_icon_gallery_obj,
		"cf_hx_rml":bot_obj.cf_hx_rml,
		"cf_rml_dys":bot_obj.cf_rml_dys,
		"cf_rml_hrs":bot_obj.cf_rml_hrs,
		"cf_rml_mnts":bot_obj.cf_rml_mnts,
		"cf_rpls_dly":bot_obj.cf_rpls_dly,
		"cf_dply_inditr":bot_obj.cf_dply_inditr,
		"cf_clct_fdk":bot_obj.cf_clct_fdk}
	return context

def default_img_handling(context,updated_field_dict):
	all_image_obj=context.get("default_img_model_obj")
	updated_img_obj=all_image_obj.get(image_name=updated_field_dict.get("dflt_icn"))
	updated_field_dict.update({"dflt_icn":updated_img_obj})
	return updated_field_dict

def bot_details_update_methods(context,updated_field_dict):
	Bot_Details.objects.filter(bot_id=context.get("bot_id"),bnk_id=context.get("bnk_id")).update(**updated_field_dict)
	if updated_field_dict.get("dflt_icn"):
		updated_field_dict=default_img_handling(context,updated_field_dict)
	context.update(updated_field_dict)
	return context

def invite_teammates_processing(request,context):
	user_active_count=User.objects.filter(custom_user_model__bankid=request.user.custom_user_model.bankid,is_active=True).count()
	if user_active_count>=request.user.custom_user_model.bot_id.bnk_id.max_act_user:
		is_active=False
	else:
		is_active=True	
	main_user_obj=User.objects.create(username=request.POST.get("username"),password=make_password(request.POST.get('password')),
		email=request.POST.get('email'),first_name=request.POST.get('full_name',None),is_active=is_active)
	create_custom_user(user=main_user_obj,bot_id=context.get("login_user_bot_id"),bankid=context.get("login_user_bank_id"),urole=request.POST.get('urole'))