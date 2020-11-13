from django.contrib import admin
from madmin.models import (Bank_Configuration,Default_Image_Icon_Gallery,Bot_Details,Custom_User_Model)

class Custom_User_Model_Admin(admin.ModelAdmin):
	list_display=['user','id','urole','bankid','bot_id']

admin.site.register(Custom_User_Model,Custom_User_Model_Admin)

class Bank_Configuration_Admin(admin.ModelAdmin):
	list_display=['bnk_id','bnk_name','bnk_urls','bnk_dbrd_urls','max_act_user','crted_dt','uptd_dt']

admin.site.register(Bank_Configuration,Bank_Configuration_Admin)

class Default_Image_Icon_Gallery_Admin(admin.ModelAdmin):
	list_display=['image_name','image_path']

admin.site.register(Default_Image_Icon_Gallery,Default_Image_Icon_Gallery_Admin)

class Bot_Details_Admin(admin.ModelAdmin):
	list_display=["bot_id","ct_pos","ct_clr","dflt_icn","ct_cstm_icn","ct_ntn_snd","ct_popup",
				"cf_hx_rml","cf_rml_dys","cf_rml_hrs","cf_rml_mnts","cf_rpls_dly","cf_dply_inditr",
				"cf_clct_fdk"]

admin.site.register(Bot_Details,Bot_Details_Admin)
