enliten.sql:
	7z x archive/enliten.7z # 7zipped Enliten SQL dump

import: enliten.sql
	mysql -uroot -e "DROP DATABASE IF EXISTS enliten; CREATE DATABASE enliten;"
	mysql -uroot enliten < enliten.sql
	mysql -uroot enliten -e "ALTER TABLE HTCs MODIFY HTCs.default TINYINT(1);"
	mysql -uroot enliten -e "ALTER TABLE login_attempts MODIFY ip_address VARCHAR(255);"
	mysql -uroot enliten -e "DELETE FROM users;" # personally identifiable info
	mysql -uroot enliten -e "ALTER TABLE users MODIFY ip_address VARCHAR(255);"
	mysql -uroot enliten -e "ALTER TABLE whomes MODIFY code VARCHAR(255);"

# For testing the schema

enlitenschema.sql: enliten.sql
	cat enliten.sql | grep -v ^INSERT | grep -v ^" (" > enlitenschema.sql

importschema: enlitenschema.sql
	mysql -uroot -e "DROP DATABASE IF EXISTS enlitenschema; CREATE DATABASE enlitenschema;"
	mysql -uroot enlitenschema < enlitenschema.sql
	mysql -uroot enlitenschema -e "ALTER TABLE HTCs MODIFY HTCs.default TINYINT(1);"
	mysql -uroot enlitenschema -e "ALTER TABLE login_attempts MODIFY ip_address VARCHAR(255);"
	mysql -uroot enlitenschema -e "DELETE FROM users;"
	mysql -uroot enlitenschema -e "ALTER TABLE users MODIFY ip_address VARCHAR(255);"
	mysql -uroot enlitenschema -e "ALTER TABLE whomes MODIFY code VARCHAR(255);"
