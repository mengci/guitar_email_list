import StringIO
from string import maketrans

with open("list.txt") as f:
	with open("insert.sql", "w+") as sqlfile:
		for line in f:
			mailInfo = line.split(",")
			if mailInfo[1] == "null":
				mailInfo[1] = "NULL"
			else:
				mailInfo[1] = "\""+ mailInfo[1] +"\"";
			a = "INSERT INTO emails (name,email,title,source_type,country,state,city,created_date) VALUES("
			a = a +"\""+ mailInfo[0] +"\""+ ", "+ mailInfo[1]+ ", " +"\""+ mailInfo[2] +"\""+", " +"\""+ mailInfo[3] +"\""+ "," +"\""+ mailInfo[4].lower() + "\"" + ", " + "\"" + mailInfo[5].lower() + "\"" + ", " + "\"" + mailInfo[6].replace("\n", "").lower() +"\""+ ", "+"NOW()"+ ")" +";"+'\n'
			sqlfile.write(a)
f.close()
sqlfile.close()