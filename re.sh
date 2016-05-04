heroku maintenance:on
 
#提交部署
 
#重新运行服务器
heroku run python manage.py deploy
heroku restart
 
#告诉Heroku，升级完成
heroku maintenance:off

