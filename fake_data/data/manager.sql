INSERT INTO authentication_user
SELECT * FROM json_populate_recordset(NULL::authentication_user, '[{"id": 1, "first_name": "Angela", "last_name": "Costa", "username": "Angela Costa", "email": "john22@example.net", "password": "a28031415f0dcbf097dd121222fcfb645541c08a", "role_id": 1, "manager_id_id": null, "is_staff": true, "is_active": true, "date_joined": "1989-10-17", "is_superuser": false}, {"id": 22, "first_name": "Eric", "last_name": "Fritz", "username": "Eric Fritz", "email": "rchristian@example.com", "password": "1c0a9ef4e2dbd6daeccfdc22513481e4096276e5", "role_id": 1, "manager_id_id": null, "is_staff": true, "is_active": true, "date_joined": "1988-12-03", "is_superuser": false}, {"id": 59, "first_name": "Sarah", "last_name": "Jennings", "username": "Sarah Jennings", "email": "wrightsusan@example.com", "password": "02285370dea4cc5e3c59e240f39eccb48141a670", "role_id": 1, "manager_id_id": null, "is_staff": true, "is_active": true, "date_joined": "1992-07-28", "is_superuser": false}, {"id": 96, "first_name": "Lynn", "last_name": "Mcintosh", "username": "Lynn Mcintosh", "email": "eparker@example.org", "password": "0b0544e4543c8a9e8281b153ab930ea87b2a4d59", "role_id": 1, "manager_id_id": null, "is_staff": true, "is_active": true, "date_joined": "1970-11-10", "is_superuser": false}, {"id": 125, "first_name": "Gabriel", "last_name": "Wright", "username": "Gabriel Wright", "email": "madelinejohnson@example.org", "password": "29ea7623787ef394c8721b8ada1b696b15d85f0e", "role_id": 1, "manager_id_id": null, "is_staff": true, "is_active": true, "date_joined": "2001-05-01", "is_superuser": false}]');