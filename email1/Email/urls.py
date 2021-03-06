"""Email URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from frontend import views

urlpatterns = [
    path('admin/', admin.site.urls),
# 登录页面
    path('', views.Login),
# 注册页面
    path('SignUp/', views.SignUp),
# 主页
    path('Index/', views.Index),
# 写邮件页面
    path('WriteEmail/', views.WriteEmail),
# 收件箱页面
    path('ReceiveEmail/', views.ReceiveEmail),
# 已发送页面
    path('SentEmail/', views.SentEmail),
# 回收站页面
    path('DeledEmail/', views.DeledEmail),
# 修改密码页面
    path('ChangePass/', views.ChangePass),
# 用户管理页面
    path('UserManage/',views.UserManage),
# 后台主界面
    path('AdminIndex/',views.AdminIndex),
# 邮箱管理界面
    path('EmailManage/',views.EmailManage),
# smtp日志界面
    path('SMTPLog/',views.SMTPLog),
# pop3日志界面
    path('POP3Log/',views.POP3Log),
# 创建用户
    path('CreateUser/',views.CreateUser),

# 身份信息获取
    path('GetIdentity/', views.GetIdentity),
# 登录认证
    path('userIdentified/', views.user_identified),
# 用户注册
    path('userRegister/', views.register),
# 登出
    path('Logout/', views.Logout),
# 修改密码
    path('ChangePwd/', views.ChangePwd),

# 管理员用户管理列表
    path('UserList/', views.UserList),
# SMTP禁用
    path('StopSMTP/', views.StopSMTP),
# SMTP开启
    path('StartSMTP/', views.StartSMTP),
# POP3禁用
    path('StopPOP3/', views.StopPOP3),
# POP3开启
    path('StartPOP3/', views.StartPOP3),
# 管理员删除用户
    path('DeleUser/', views.DeleUser),
# 管理员删除邮件
    path('ManagerDeleEmail/', views.ManagerDeleEmail),
# 设为管理员
    path('SetAsManager/', views.SetAsManager),
# 设为普通用户
    path('SetAsUser/', views.SetAsUser),
# 邮件管理列表
    path('EmailList/', views.EmailList),
# SMTP日志列表
    path('SMTPLogList/', views.SMTPLogList),
# POP日志列表
    path('POPLogList/', views.POPLogList),
# SMTP日志清除
    path('DeleSMTPLog/', views.DeleSMTPLog),
# POP日志清除
    path('DelePOPLog/', views.DelePOPLog),
# 后台主页数据
    path('AdminIndexInfo/', views.AdminIndexInfo),
# 某用户的smtp pop authority权限
    path('UserStates/', views.UserStates),



# 发邮件，含群发
    path('SendEmail/', views.SendEmail),
# 具体邮件查看
    path('CheckMail/', views.CheckMail),


# 发件箱列表
    path('SendList/', views.SendList),
# 收件箱列表
    path('RcvList/', views.RcvList),
# 普通用户发件箱删除邮件
    path('SenderDeleEmail/', views.SenderDeleEmail),
# 普通用户收件箱删除邮件
    path('RcverDeleEmail/', views.RcverDeleEmail),
# 用户主页数据
    path('IndexInfo/', views.IndexInfo),
# 已删除列表
    path('DeletedMailList/', views.DeletedMailList),
# 恢复已删除邮件
    path('RecoverDeletedMail/', views.RecoverDeletedMail),
# 彻底删除已删除邮件
    path('CompleDelMail/', views.CompleDelMail),

]
