import os
def sms():
phone_id='919958032589'
message='We will start in 1 hr.Sam'
curr_dir=os.getcwd()
os.chdir('/home/server/Desktop/abc');
sms_file=file('new_sms.txt','w');
sms_file.write('To:');
sms_file.write(phone_id);
sms_file.write("\n\n");
sms_file.write(message);
sms_file.close();
#os.system('sudo /etc/init.d/sms start');###few doubts
#os.system('mv new_sms.txt /home/sangeeta/Desktop/abc2');
os.system('sudo mv new_sms.txt /var/spool/sms/outgoing')
os.chdir(curr_dir)



