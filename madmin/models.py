from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

def auto_generated_bankid():
   return "B-0000"

class Bank_Configuration(models.Model):
    bnk_id = models.CharField(max_length=6,default=auto_generated_bankid)
    bnk_name = models.CharField("Bank Name",max_length=50,default="example")
    bnk_urls=models.URLField("Bank Urls",max_length=100,default="example.com")
    bnk_dbrd_urls=models.URLField("Bank Dashboard Urls",max_length=100,default="example.com",blank=True,null=True)
    max_act_user=models.IntegerField('Maximum Activate User Allow',default=1)
    crted_dt = models.DateTimeField("Bank Created Date",auto_now_add=True)
    uptd_dt = models.DateTimeField("Bank Updated Date",auto_now=True)
    def __str__(self):
        return self.bnk_id

class Default_Image_Icon_Gallery(models.Model):
  image_name = models.CharField(primary_key=True,max_length=200)
  image_path= models.ImageField(upload_to='images/',unique=True)
  def __str__(self):
    return self.image_name

BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))

WIDGET_POSITION_ON_THE_SCREEN=((True, 'Left'),(False, 'Right'))

NOTIFICATION_SOUND_FOR_BOT=(('Eventual','Eventual'),('Subtle','Subtle'),
               ('Light','Light'),('Open Ended','Open Ended'))

LANGUAGE_CHOICES = (("English","English"),("Spanish", "Spanish"),
           ("German", "German"),("Portuguese", "Portuguese"))

CHAT_HISTORY_REMOVABLE_INDICATOR=((True,"Time Basis"),(False,"Session Basis"))

def default_value_for_icon():
    img_obj=Default_Image_Icon_Gallery.objects.get(image_name="icon_1")
    return img_obj


class Bot_Details(models.Model):
    bot_id= models.AutoField(primary_key=True)
    bnk_id = models.ForeignKey(Bank_Configuration,on_delete=models.CASCADE,verbose_name='Bank ID')
    #customization(ct)
    ct_pos=models.BooleanField('Position',choices=WIDGET_POSITION_ON_THE_SCREEN,default=False)
    ct_clr = models.CharField('Color Of Bot',max_length=100, default='#50A59D')
    # default=default_value_for_icon
    dflt_icn=models.ForeignKey(Default_Image_Icon_Gallery,on_delete=models.CASCADE,default=default_value_for_icon)
    ct_cstm_icn= models.ImageField('Custom Icon',upload_to='images/',default= '/media/images/Launcher_icon1.png',blank=True,null=True)
    ct_ntn_snd = models.CharField('Notification Sound',max_length=100, choices=NOTIFICATION_SOUND_FOR_BOT,default='Eventual')
    ct_popup=models.BooleanField("Popup",default=False)
    #configuration(cf)
    cf_hx_rml=models.BooleanField('Chat history removable indicator',choices=CHAT_HISTORY_REMOVABLE_INDICATOR,default=False)
    cf_rml_dys=models.IntegerField('Chat history removal days',default=1,help_text="30 days")
    cf_rml_hrs=models.IntegerField('Chat history removal hours',default=0,help_text="10 hours")
    cf_rml_mnts=models.IntegerField('Chat history removal minutes',default=0,help_text="30 minutes")
    cf_rpls_dly=models.IntegerField('Bot replies delay period',default=5,help_text="0 second")
    cf_dply_inditr=models.BooleanField('Chat widget display indicator',choices=BOOL_CHOICES,default=True)
    cf_clct_fdk=models.BooleanField('CollectFeedback',choices=BOOL_CHOICES,default=False) 
    def __str__(self):
        return str(self.bot_id) 
        
USER_STATUS = (('1', 'super admin'), ('2', 'teammate'), ('3', 'operator'))
class Custom_User_Model(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    urole = models.CharField(max_length=30, choices=USER_STATUS, default='3')
    bot_id= models.ForeignKey(Bot_Details,on_delete=models.CASCADE,null=True,blank=True)
    bankid = models.CharField(max_length=6,default=auto_generated_bankid)
    def __str__(self):
        return str(self.user.username)

