{
	"info": {
		"_postman_id": "4150bf39-7fea-4bbf-9add-5ea15b692226",
		"name": "Artist-Project Copy 4",
		"schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
		"_exporter_id": "26196580"
	},
	"item": [
		{
			"name": "Talent",
			"item": [
				{
					"name": "Auth",
					"item": [
						{
							"name": "sign up",
							"request": {
								"method": "POST",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "{\n    \"encoded_id\": \"NTI0NzYxNA==\",\n    \"first_name\": \"kane\",\n    \"last_name\": \"williamson\",\n    \"email\": \"steve51@yopmail.com\",\n    \"password\":\"9014\",\n    \"experience\": 1,\n    \"date_of_birth\": \"2021-09-09\",\n    \"gender\": 1,\n    \"profile_picture\": 1,\n    \"phone_no\": \"8787878776\",\n    \"country_code\": \"+91\",\n    \"address\": \"456 Elm St\",\n    \"city\": \"London\",\n    \"state\": \"NY\",\n    \"country\": \"UK\"\n}",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "{{local}}talent/registration",
									"host": [
										"{{local}}talent"
									],
									"path": [
										"registration"
									]
								}
							},
							"response": []
						},
						{
							"name": "send otp",
							"request": {
								"method": "POST",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "{\n    \"encoded_id\": \"NTI0NzYxNA==\",\n    // \"email\": \"steve51@yopmail.com\"\n    \"country_code\": \"+91\",\n    \"phone_no\": \"8787878776\"\n}",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "{{local}}talent/send-otp",
									"host": [
										"{{local}}talent"
									],
									"path": [
										"send-otp"
									]
								}
							},
							"response": []
						},
						{
							"name": "verify otp",
							"request": {
								"method": "POST",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "{\n    \"country_code\": \"+91\",\n    \"phone_no\": \"8787878776\",\n    // \"email\": \"steve51@yopmail.com\",\n    \"otp\": \"1234\"\n}",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "{{local}}talent/verify-otp",
									"host": [
										"{{local}}talent"
									],
									"path": [
										"verify-otp"
									]
								}
							},
							"response": []
						},
						{
							"name": "sub categories listing",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE4Mzg0MTY2LCJpYXQiOjE3MTgyOTc3NjYsImp0aSI6IjVmNTAxNDE0ZDFhNTQ0NjRhZGVkNGMxMGQ4NGU2MGE1IiwidXNlcl9pZCI6NTd9.hibeKg2ZLsjV6h0FQsARvKd4E6qvRg-n9cNuwALLlOg",
											"type": "string"
										}
									]
								},
								"method": "POST",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "{\r\n    \"categories\": [1, 2]\r\n}",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "{{local}}talent/sub-categories",
									"host": [
										"{{local}}talent"
									],
									"path": [
										"sub-categories"
									]
								}
							},
							"response": []
						},
						{
							"name": "update profile",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE4Mzg0MTY2LCJpYXQiOjE3MTgyOTc3NjYsImp0aSI6IjVmNTAxNDE0ZDFhNTQ0NjRhZGVkNGMxMGQ4NGU2MGE1IiwidXNlcl9pZCI6NTd9.hibeKg2ZLsjV6h0FQsARvKd4E6qvRg-n9cNuwALLlOg",
											"type": "string"
										}
									]
								},
								"method": "PUT",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "{\r\n    // \"user\": {\r\n    //     \"first_name\": \"kane stuart\",\r\n    //     \"last_name\": \"williamson\",\r\n    //     \"address\": \"nz tauranga\",\r\n    //     \"profile_picture\": 1\r\n    // },\r\n//     \"category\" : [\r\n//     {\r\n//       \"subcategory_id\" : [\r\n//         19\r\n//       ],\r\n//       \"category_id\" : 17\r\n//     }\r\n//   ]\r\n    \"model_status\": {\r\n            \"hips\" : 12,\r\n            \"waist\" : 15,\r\n            // \"hair_color\" : 2,\r\n            \"height_inches\" : 1,\r\n            // \"eye_color\" : 4,\r\n            \"bust\" : 7,\r\n            \"height_feet\" : 5\r\n  }\r\n    // \"portfolio\": {\r\n    //     \"portfolio\": [214, 215],\r\n    //     \"cover_photo\": 214\r\n    // }\r\n    // \"booking_method\": {\r\n    //     \"method\": 1\r\n    // },\r\n    // \"services\": [\r\n    //                 {\r\n    //                     \"price\": 400,\r\n    //                     \"service\": \"facial\"\r\n    //                 },\r\n    //                 {\r\n    //                     \"price\": 1000,\r\n    //                     \"service\": \"makeup\"\r\n    //                 }\r\n    //             ]    \r\n}",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "{{local}}talent/update-profile",
									"host": [
										"{{local}}talent"
									],
									"path": [
										"update-profile"
									]
								}
							},
							"response": []
						},
						{
							"name": "login",
							"request": {
								"method": "POST",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "{\r\n    \"email\": \"steve@yopmail.com\",\r\n    \"password\": \"9014\"\r\n    // \"country_code\": \"+91\",\r\n    // \"phone_no\": \"8787878776\"\r\n}",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "{{dev}}talent/login",
									"host": [
										"{{dev}}talent"
									],
									"path": [
										"login"
									]
								}
							},
							"response": []
						},
						{
							"name": "profile details",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE4Mzg0MTY2LCJpYXQiOjE3MTgyOTc3NjYsImp0aSI6IjVmNTAxNDE0ZDFhNTQ0NjRhZGVkNGMxMGQ4NGU2MGE1IiwidXNlcl9pZCI6NTd9.hibeKg2ZLsjV6h0FQsARvKd4E6qvRg-n9cNuwALLlOg",
											"type": "string"
										}
									]
								},
								"method": "GET",
								"header": [],
								"url": {
									"raw": "{{local}}talent/profile-details",
									"host": [
										"{{local}}talent"
									],
									"path": [
										"profile-details"
									]
								}
							},
							"response": []
						},
						{
							"name": "category listing",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE4Mzg0MTY2LCJpYXQiOjE3MTgyOTc3NjYsImp0aSI6IjVmNTAxNDE0ZDFhNTQ0NjRhZGVkNGMxMGQ4NGU2MGE1IiwidXNlcl9pZCI6NTd9.hibeKg2ZLsjV6h0FQsARvKd4E6qvRg-n9cNuwALLlOg",
											"type": "string"
										}
									]
								},
								"method": "GET",
								"header": [],
								"url": {
									"raw": "{{local}}talent/all-categories",
									"host": [
										"{{local}}talent"
									],
									"path": [
										"all-categories"
									]
								}
							},
							"response": []
						},
						{
							"name": "change password",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE2MDg5ODQ1LCJpYXQiOjE3MTYwMDM0NDUsImp0aSI6ImRjYTU0MGVhODNkYjRlNGJhNjZkMjU2YTAzMDliNmUxIiwidXNlcl9pZCI6NTB9.TDGss4e-a--MgnsPzIzry8VDZEwiw2bB3L7uuCr5FHw",
											"type": "string"
										}
									]
								},
								"method": "POST",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "{\r\n    \"old_password\": \"9014\",\r\n    \"new_password\": \"1234\"\r\n}",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "{{local}}talent/change-password",
									"host": [
										"{{local}}talent"
									],
									"path": [
										"change-password"
									]
								}
							},
							"response": []
						},
						{
							"name": "edit profile",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE4Mzg0MTY2LCJpYXQiOjE3MTgyOTc3NjYsImp0aSI6IjVmNTAxNDE0ZDFhNTQ0NjRhZGVkNGMxMGQ4NGU2MGE1IiwidXNlcl9pZCI6NTd9.hibeKg2ZLsjV6h0FQsARvKd4E6qvRg-n9cNuwALLlOg",
											"type": "string"
										}
									]
								},
								"method": "PUT",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "{\r\n    \"first_name\": \"new\",\r\n    \"last_name\": \"account\",\r\n    // \"email\": \"brock@yopmail.com\",\r\n    // \"phone_no\": \"987654210\",\r\n    // \"country_code\": \"+91\",\r\n    \"address\": \"new address\",\r\n    \"city\": \"London\",\r\n    \"state\": \"NY\",\r\n    \"country\": \"UK\",\r\n    \"profile_picture\": 1,\r\n    \"bust\": 36,\r\n    \"waist\": 36, \r\n    \"hips\": 10,\r\n    \"height_feet\": 10,\r\n    \"height_inches\": 1,\r\n    \"weight\": 10.9,\r\n    // \"hair_color\": 1,\r\n    // \"eye_color\": 1,\r\n    \"booking_method\": 1,\r\n    \"portfolio\": [5, 6],\r\n    \"cover_photo\": 1,\r\n    \"categories\": [1],\r\n    \"sub_categories\": [1],\r\n    \"services\": [\r\n            {\r\n                \"price\": 1000,\r\n                \"service\": \"detan\"\r\n            },\r\n            {\r\n                \"price\": 300,\r\n                \"service\": \"scrub\"\r\n            }\r\n        ]\r\n}",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "{{local}}talent/edit-profile",
									"host": [
										"{{local}}talent"
									],
									"path": [
										"edit-profile"
									]
								}
							},
							"response": []
						},
						{
							"name": "otp to user",
							"request": {
								"method": "POST",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "{\r\n    \"country_code\": \"+91\",\r\n    \"phone_no\": \"8787878777\"\r\n}",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "{{local}}talent/otp-to-user",
									"host": [
										"{{local}}talent"
									],
									"path": [
										"otp-to-user"
									]
								}
							},
							"response": []
						}
					]
				},
				{
					"name": "Bookings",
					"item": [
						{
							"name": "Upcoming bookings",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE4MjkxODc1LCJpYXQiOjE3MTgyMDU0NzUsImp0aSI6ImUyY2RjOTJkZDE3NTQ3MDdiZjg0NWYwODY3M2ZhM2NjIiwidXNlcl9pZCI6MTcxfQ.1ypIEoQiESqTeSoIR7zNvur7Cm0r5DcazEtOvxJoSJU",
											"type": "string"
										}
									]
								},
								"method": "GET",
								"header": [],
								"url": {
									"raw": "{{local}}talent/upcoming-bookings-listing",
									"host": [
										"{{local}}talent"
									],
									"path": [
										"upcoming-bookings-listing"
									]
								}
							},
							"response": []
						},
						{
							"name": "past-bookings",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE2MDIxMzIyLCJpYXQiOjE3MTU5MzQ5MjIsImp0aSI6IjY3OTY1NGM5Yzc4ZDQ0OTliZTM4OTRmY2ZiODA3Mzk2IiwidXNlcl9pZCI6Mzh9.7kFsBoL6rCpU9pJ0mwibCmqIm1UBhXK9T3NrF6vW2fg",
											"type": "string"
										}
									]
								},
								"method": "GET",
								"header": [],
								"url": {
									"raw": "{{local}}talent/past-bookings",
									"host": [
										"{{local}}talent"
									],
									"path": [
										"past-bookings"
									]
								}
							},
							"response": []
						},
						{
							"name": "recent offers",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE2ODczNTc4LCJpYXQiOjE3MTY3ODcxNzgsImp0aSI6ImU1YzBkNDY5MmJkNjQxY2E5YTcxNDFmMmE4OTYwMjhjIiwidXNlcl9pZCI6OTR9.mEQyt99eTChnH5-nAMWTxKic3Tvo0ImB082LzQebIp8",
											"type": "string"
										}
									]
								},
								"method": "GET",
								"header": [],
								"url": {
									"raw": "{{dev}}talent/recent-offers",
									"host": [
										"{{dev}}talent"
									],
									"path": [
										"recent-offers"
									]
								}
							},
							"response": []
						},
						{
							"name": "cancelled bookings",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE2MDIxMzIyLCJpYXQiOjE3MTU5MzQ5MjIsImp0aSI6IjY3OTY1NGM5Yzc4ZDQ0OTliZTM4OTRmY2ZiODA3Mzk2IiwidXNlcl9pZCI6Mzh9.7kFsBoL6rCpU9pJ0mwibCmqIm1UBhXK9T3NrF6vW2fg",
											"type": "string"
										}
									]
								},
								"method": "GET",
								"header": [],
								"url": {
									"raw": "{{local}}talent/cancelled-bookings",
									"host": [
										"{{local}}talent"
									],
									"path": [
										"cancelled-bookings"
									]
								}
							},
							"response": []
						},
						{
							"name": "booking details by id",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE2MDIxMzIyLCJpYXQiOjE3MTU5MzQ5MjIsImp0aSI6IjY3OTY1NGM5Yzc4ZDQ0OTliZTM4OTRmY2ZiODA3Mzk2IiwidXNlcl9pZCI6Mzh9.7kFsBoL6rCpU9pJ0mwibCmqIm1UBhXK9T3NrF6vW2fg",
											"type": "string"
										}
									]
								},
								"method": "GET",
								"header": [],
								"url": {
									"raw": "{{local}}talent/fetch-booking-details/6",
									"host": [
										"{{local}}talent"
									],
									"path": [
										"fetch-booking-details",
										"6"
									]
								}
							},
							"response": []
						},
						{
							"name": "counter offer",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE2MDIxMzIyLCJpYXQiOjE3MTU5MzQ5MjIsImp0aSI6IjY3OTY1NGM5Yzc4ZDQ0OTliZTM4OTRmY2ZiODA3Mzk2IiwidXNlcl9pZCI6Mzh9.7kFsBoL6rCpU9pJ0mwibCmqIm1UBhXK9T3NrF6vW2fg",
											"type": "string"
										}
									]
								},
								"method": "POST",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "{\r\n    \"booking_id\": 6,\r\n    \"counter_offer_price\": 1000\r\n}",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "{{local}}talent/counter-offer",
									"host": [
										"{{local}}talent"
									],
									"path": [
										"counter-offer"
									]
								}
							},
							"response": []
						},
						{
							"name": "accept booking",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE2OTc1MTE1LCJpYXQiOjE3MTY4ODg3MTUsImp0aSI6ImM1NzQ0MzAwMDk1YjRjMTE4NTZiYmY1Mzk2NDZiNjQwIiwidXNlcl9pZCI6OTR9.2MxB2J9doIB9Wp3kOLsqmHeqWx3oO93TXYqUH1maNMw",
											"type": "string"
										}
									]
								},
								"method": "POST",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "{\r\n    \"booking_id\": 23\r\n}",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "{{dev}}talent/accept-offer",
									"host": [
										"{{dev}}talent"
									],
									"path": [
										"accept-offer"
									]
								}
							},
							"response": []
						},
						{
							"name": "decline offer",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE2NzE0NTE5LCJpYXQiOjE3MTY2MjgxMTksImp0aSI6IjUyZTVhOTYxOWY5NjQ1ZTE4ZTIyMmFiYWIyYWMzZmY0IiwidXNlcl9pZCI6Mzh9.F1FNVguQszoaJQLeVamBP_M2giRwsME1oVAeGwVpG5Y",
											"type": "string"
										}
									]
								},
								"method": "POST",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "{\r\n    \"booking_id\": 12\r\n}",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "{{local}}talent/decline-offer",
									"host": [
										"{{local}}talent"
									],
									"path": [
										"decline-offer"
									]
								}
							},
							"response": []
						},
						{
							"name": "accepted offers",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE2ODc4NDA3LCJpYXQiOjE3MTY3OTIwMDcsImp0aSI6Ijk1ZjBiNmJkYmM1ZTQ0OGZhNGY1YzEzN2NkNDRkN2M2IiwidXNlcl9pZCI6Mzh9.ffx7pgYuu42DE90GGNQAr2MiFD-He-PtOeDK1_nPxaE",
											"type": "string"
										}
									]
								},
								"method": "GET",
								"header": [],
								"url": {
									"raw": "{{local}}talent/accepted-offers",
									"host": [
										"{{local}}talent"
									],
									"path": [
										"accepted-offers"
									]
								}
							},
							"response": []
						}
					]
				},
				{
					"name": "slots",
					"item": [
						{
							"name": "operational slots",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE4Mzg0MTY2LCJpYXQiOjE3MTgyOTc3NjYsImp0aSI6IjVmNTAxNDE0ZDFhNTQ0NjRhZGVkNGMxMGQ4NGU2MGE1IiwidXNlcl9pZCI6NTd9.hibeKg2ZLsjV6h0FQsARvKd4E6qvRg-n9cNuwALLlOg",
											"type": "string"
										}
									]
								},
								"method": "POST",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "[\n    {\n        \"day\": 0,\n        \"date\": \"2024-06-17\",\n        \"start\": \"16:00\",\n        \"end\": \"23:00\",\n        \"is_active\": true\n    },\n    {\n        \"day\": 1,\n        \"date\": \"2024-05-18\",\n        \"start\": \"09:00\",\n        \"end\": \"18:00\",\n        \"is_active\": true\n    },\n    {\n        \"day\": 2,\n        \"date\": \"2024-05-19\",\n        \"start\": \"09:00\",\n        \"end\": \"16:00\",\n        \"is_active\": true\n    },\n    {\n        \"day\": 3,\n        \"date\": \"2024-05-13\",\n        \"start\": \"09:00\",\n        \"end\": \"18:00\",\n        \"is_active\": true\n    },\n    {\n        \"day\": 4,\n        \"date\": \"2024-05-14\",\n        \"start\": \"09:00\",\n        \"end\": \"18:00\",\n        \"is_active\": false\n    },\n    {\n        \"day\": 5,\n        \"date\": \"2024-05-15\",\n        \"start\": \"09:00\",\n        \"end\": \"18:00\",\n        \"is_active\": true\n    },\n    {\n        \"day\": 6,\n        \"date\": \"2024-05-16\",\n        \"start\": \"09:00\",\n        \"end\": \"18:00\",\n        \"is_active\": true\n    }\n]",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "{{local}}talent/add-slots",
									"host": [
										"{{local}}talent"
									],
									"path": [
										"add-slots"
									]
								}
							},
							"response": []
						},
						{
							"name": "weekly timings",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE4Mzg0MTY2LCJpYXQiOjE3MTgyOTc3NjYsImp0aSI6IjVmNTAxNDE0ZDFhNTQ0NjRhZGVkNGMxMGQ4NGU2MGE1IiwidXNlcl9pZCI6NTd9.hibeKg2ZLsjV6h0FQsARvKd4E6qvRg-n9cNuwALLlOg",
											"type": "string"
										}
									]
								},
								"method": "GET",
								"header": [],
								"url": {
									"raw": "{{local}}talent/week-timings",
									"host": [
										"{{local}}talent"
									],
									"path": [
										"week-timings"
									]
								}
							},
							"response": []
						},
						{
							"name": "day slots",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE4Mzg0MTY2LCJpYXQiOjE3MTgyOTc3NjYsImp0aSI6IjVmNTAxNDE0ZDFhNTQ0NjRhZGVkNGMxMGQ4NGU2MGE1IiwidXNlcl9pZCI6NTd9.hibeKg2ZLsjV6h0FQsARvKd4E6qvRg-n9cNuwALLlOg",
											"type": "string"
										}
									]
								},
								"method": "POST",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "{\r\n    \"date\": \"2024-06-17\"\r\n}",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "{{local}}talent/day-slots",
									"host": [
										"{{local}}talent"
									],
									"path": [
										"day-slots"
									]
								}
							},
							"response": []
						}
					]
				}
			]
		},
		{
			"name": "Admin",
			"item": [
				{
					"name": "Terms-And-Conditions",
					"item": [
						{
							"name": "add TAC",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE0ODA1MDEyLCJpYXQiOjE3MTQ3MTg2MTIsImp0aSI6IjVmMjc5ODgyNDc4ZjQzNWFiYTRlZDI3NWE0MDVjNzA4IiwidXNlcl9pZCI6Mn0.Iw0rhsAWsxr55gLrjxwDbnttfp-G-wctqtOVOvxuKHk",
											"type": "string"
										}
									]
								},
								"method": "POST",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "{\n    \"data\":\"hello world!!!\"\n}",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "{{local}}admin/terms-and-conditions",
									"host": [
										"{{local}}admin"
									],
									"path": [
										"terms-and-conditions"
									]
								}
							},
							"response": []
						},
						{
							"name": "update TAC",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE0ODA1MDEyLCJpYXQiOjE3MTQ3MTg2MTIsImp0aSI6IjVmMjc5ODgyNDc4ZjQzNWFiYTRlZDI3NWE0MDVjNzA4IiwidXNlcl9pZCI6Mn0.Iw0rhsAWsxr55gLrjxwDbnttfp-G-wctqtOVOvxuKHk",
											"type": "string"
										}
									]
								},
								"method": "PUT",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "{\n    \"data\":\"testing1234\"\n}",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "{{local}}admin/update-terms-and-conditions/1",
									"host": [
										"{{local}}admin"
									],
									"path": [
										"update-terms-and-conditions",
										"1"
									]
								}
							},
							"response": []
						},
						{
							"name": "get-TAC",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE0ODA1MDEyLCJpYXQiOjE3MTQ3MTg2MTIsImp0aSI6IjVmMjc5ODgyNDc4ZjQzNWFiYTRlZDI3NWE0MDVjNzA4IiwidXNlcl9pZCI6Mn0.Iw0rhsAWsxr55gLrjxwDbnttfp-G-wctqtOVOvxuKHk",
											"type": "string"
										}
									]
								},
								"method": "GET",
								"header": [],
								"url": {
									"raw": "{{local}}terms-and-conditions-show",
									"host": [
										"{{local}}terms-and-conditions-show"
									]
								}
							},
							"response": []
						}
					]
				},
				{
					"name": "admin onboarding",
					"item": [
						{
							"name": "admin-login",
							"request": {
								"method": "POST",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "{\n    \"email\":\"admin_artist@yopmail.com\",\n    \"password\":\"Test@123\"\n}",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "{{local}}admin/admin-log-in",
									"host": [
										"{{local}}admin"
									],
									"path": [
										"admin-log-in"
									]
								}
							},
							"response": []
						},
						{
							"name": "sent-otp",
							"request": {
								"method": "POST",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "{\n    \"email\":\"admin_artist@yopmail.com\"\n}",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "{{local}}admin/send-otp",
									"host": [
										"{{local}}admin"
									],
									"path": [
										"send-otp"
									]
								}
							},
							"response": []
						},
						{
							"name": "verify-otp",
							"request": {
								"method": "POST",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "{\n    \"email\":\"admin_artist@yopmail.com\",\n    \"otp\": \"1234\"\n}",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "{{local}}admin/verify-otp",
									"host": [
										"{{local}}admin"
									],
									"path": [
										"verify-otp"
									]
								}
							},
							"response": []
						},
						{
							"name": "forgot-password",
							"request": {
								"method": "POST",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "{\n    \"encoded_id\": \"MjI0MTg4MA==\",\n    \"password\":\"Test@123\"\n}",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "{{local}}admin/forgot-password",
									"host": [
										"{{local}}admin"
									],
									"path": [
										"forgot-password"
									]
								}
							},
							"response": []
						},
						{
							"name": "admin_details",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE1MzMxMzYxLCJpYXQiOjE3MTUyNDQ5NjEsImp0aSI6IjYwNDUwYzM0NjgyNTRiYzhiNTQ5Y2M2NzJkYjliOGYwIiwidXNlcl9pZCI6MX0.uE2Yx7loPvApqg2wQ7gGec-v4CRhL2wWG3bPsX9HBKk",
											"type": "string"
										}
									]
								},
								"method": "GET",
								"header": [],
								"url": {
									"raw": "{{local}}admin/admin-details",
									"host": [
										"{{local}}admin"
									],
									"path": [
										"admin-details"
									]
								}
							},
							"response": []
						},
						{
							"name": "update details",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE1MzI0MzU1LCJpYXQiOjE3MTUyMzc5NTUsImp0aSI6IjY3YjY4N2U5YzRmMjRlNTdhNTVhZWNhNjY1YTc0MGFmIiwidXNlcl9pZCI6MX0.gSRQFUAxY7gseTDXTI0BLTJY1es2pRL59HrcSw6PUnY",
											"type": "string"
										}
									]
								},
								"method": "PUT",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "{\n    \"username\": \"admin1234\",\n        \"country_code\": \"+91\",\n        \"email\": \"admin123@yopmail.com\",\n        \"phone_no\": \"9876543221\",\n        \"address\": \"helloworld\",\n    \"profile_picture\":1\n}",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "{{local}}admin/update-details",
									"host": [
										"{{local}}admin"
									],
									"path": [
										"update-details"
									]
								}
							},
							"response": []
						},
						{
							"name": "change password",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE1MjQ4MjgzLCJpYXQiOjE3MTUxNjE4ODMsImp0aSI6ImM2MDA4N2ViNjE3MzRlMGI5YjU4MGVmZDY2OWMyODRiIiwidXNlcl9pZCI6MX0.e0jZk0CKSDaPhhm3JOBWfmA2Z2MNFKPK_eiI7PSr19E",
											"type": "string"
										}
									]
								},
								"method": "POST",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "{\n    \"old_password\":\"admin123\",\n    \"new_password\":\"admin1234\"\n}",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "{{local}}admin/change-password",
									"host": [
										"{{local}}admin"
									],
									"path": [
										"change-password"
									]
								}
							},
							"response": []
						},
						{
							"name": "logout",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE1MjQ4MjgzLCJpYXQiOjE3MTUxNjE4ODMsImp0aSI6ImM2MDA4N2ViNjE3MzRlMGI5YjU4MGVmZDY2OWMyODRiIiwidXNlcl9pZCI6MX0.e0jZk0CKSDaPhhm3JOBWfmA2Z2MNFKPK_eiI7PSr19E",
											"type": "string"
										}
									]
								},
								"method": "POST",
								"header": [],
								"url": {
									"raw": "{{local}}admin/admin-log-out",
									"host": [
										"{{local}}admin"
									],
									"path": [
										"admin-log-out"
									]
								}
							},
							"response": []
						}
					]
				},
				{
					"name": "manage customers",
					"item": [
						{
							"name": "add-customer-through-admin",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE1MDczMjc1LCJpYXQiOjE3MTQ5ODY4NzUsImp0aSI6IjE5ODUzMTNkYjljMjQ5YjBiODY0MDhmN2Y5ZjgzYmFhIiwidXNlcl9pZCI6MX0.ko8HOWNWXbD67vsuRsgCmf2uoGQlhI4GBkUt2Dk3T_Y",
											"type": "string"
										}
									]
								},
								"method": "POST",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "{\n    \"first_name\":\"john\",\n    \"last_name\":\"clark\",\n    \"city\":\"NY\",\n    \"state\":\"kjhsdfka\",\n    \"country\":\"USA\",\n    \"phone_no\":\"987611111\",\n    \"email\":\"john@yopmail.com\",\n    \"address\":\"testing12345678\"\n\n}",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "{{local}}admin/add-customer",
									"host": [
										"{{local}}admin"
									],
									"path": [
										"add-customer"
									]
								}
							},
							"response": []
						},
						{
							"name": "get all the clients",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE1OTIwMTk2LCJpYXQiOjE3MTU4MzM3OTYsImp0aSI6ImFlNWFkMjUyOGFjODRhMDM4MTJiZWQ5OWYzMzMyY2FiIiwidXNlcl9pZCI6MX0.zwMzY_lR1b7L7L2gW6yTXsfHgIYYNTz9P_EY5jnbu6M",
											"type": "string"
										}
									]
								},
								"method": "POST",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "{\r\n    \"length\": 10,\r\n    \"start\": 1,\r\n    \"search\": \"\"\r\n}",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "{{local}}admin/all-customers",
									"host": [
										"{{local}}admin"
									],
									"path": [
										"all-customers"
									]
								}
							},
							"response": []
						},
						{
							"name": "edit-customer-by-id",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE1MjQ4MjgzLCJpYXQiOjE3MTUxNjE4ODMsImp0aSI6ImM2MDA4N2ViNjE3MzRlMGI5YjU4MGVmZDY2OWMyODRiIiwidXNlcl9pZCI6MX0.e0jZk0CKSDaPhhm3JOBWfmA2Z2MNFKPK_eiI7PSr19E",
											"type": "string"
										}
									]
								},
								"method": "PUT",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "{\n    \"first_name\":\"kane\",\n    \"last_name\":\"williamson\"\n}",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "{{local}}admin/edit-customer-by-id/2",
									"host": [
										"{{local}}admin"
									],
									"path": [
										"edit-customer-by-id",
										"2"
									]
								}
							},
							"response": []
						},
						{
							"name": "customer-details-by-id",
							"protocolProfileBehavior": {
								"disableBodyPruning": true
							},
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE1MjQ4MjgzLCJpYXQiOjE3MTUxNjE4ODMsImp0aSI6ImM2MDA4N2ViNjE3MzRlMGI5YjU4MGVmZDY2OWMyODRiIiwidXNlcl9pZCI6MX0.e0jZk0CKSDaPhhm3JOBWfmA2Z2MNFKPK_eiI7PSr19E",
											"type": "string"
										}
									]
								},
								"method": "GET",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "{{local}}admin/customers-details-by-id/2",
									"host": [
										"{{local}}admin"
									],
									"path": [
										"customers-details-by-id",
										"2"
									]
								}
							},
							"response": []
						},
						{
							"name": "delete customer",
							"request": {
								"method": "DELETE",
								"header": [],
								"url": {
									"raw": "{{local}}admin/delete-customer-by-id/15",
									"host": [
										"{{local}}admin"
									],
									"path": [
										"delete-customer-by-id",
										"15"
									]
								}
							},
							"response": []
						},
						{
							"name": "update status",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE1NjYzNjU1LCJpYXQiOjE3MTU1NzcyNTUsImp0aSI6ImQ4YTdjMmMwYmJjYTRmYmFiYzUwYjdkNDc2OGQ1ZWIzIiwidXNlcl9pZCI6MX0.s61JF9GLc7lYFq1JVobeObPl_k4pOkdjj8AXQKAVYsc",
											"type": "string"
										}
									]
								},
								"method": "PUT",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "{\r\n    \"is_active\": false\r\n}",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "{{local}}admin/update-status-of-user/19",
									"host": [
										"{{local}}admin"
									],
									"path": [
										"update-status-of-user",
										"19"
									]
								}
							},
							"response": []
						},
						{
							"name": "customer bookings",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE2NDYzMjc3LCJpYXQiOjE3MTYzNzY4NzcsImp0aSI6ImJiNWM3YmRkNTgzZjQzZjRhM2NlMWVmZWYwNTcwNGM1IiwidXNlcl9pZCI6MX0.9O22WlSpX6Bzm9a8FEH-LDSV43I61cGRPaubg2x15HM",
											"type": "string"
										}
									]
								},
								"method": "POST",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "{\r\n    \"length\": 10,\r\n    \"start\": 1,\r\n    \"search\": \"\",\r\n    \"key\": 1\r\n}",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "{{local}}admin/customer-bookings/37",
									"host": [
										"{{local}}admin"
									],
									"path": [
										"customer-bookings",
										"37"
									]
								}
							},
							"response": []
						}
					]
				},
				{
					"name": "category module",
					"item": [
						{
							"name": "add sub category",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE1NjYzNjU1LCJpYXQiOjE3MTU1NzcyNTUsImp0aSI6ImQ4YTdjMmMwYmJjYTRmYmFiYzUwYjdkNDc2OGQ1ZWIzIiwidXNlcl9pZCI6MX0.s61JF9GLc7lYFq1JVobeObPl_k4pOkdjj8AXQKAVYsc",
											"type": "string"
										}
									]
								},
								"method": "POST",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "{\n    \"name\": \"wedding dancer\",\n    \"category\":2\n}",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "{{local}}admin/sub-category/",
									"host": [
										"{{local}}admin"
									],
									"path": [
										"sub-category",
										""
									]
								}
							},
							"response": []
						},
						{
							"name": "add category",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE2Mjg1NjQzLCJpYXQiOjE3MTYxOTkyNDMsImp0aSI6ImUwMzE4YzRkZWZmZTRhZTRiOGNkNTMwMmUwMzkzODNhIiwidXNlcl9pZCI6MX0.H9gX7Kn61uNqdTBxb_y_nT10WVZP_3Vmtxnlh_mrTWc",
											"type": "string"
										}
									]
								},
								"method": "POST",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "{\n    \"image\": 1,\n    \"name\": \"reder\"\n}",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "{{local}}admin/category",
									"host": [
										"{{local}}admin"
									],
									"path": [
										"category"
									]
								}
							},
							"response": []
						},
						{
							"name": "all category",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE2Mjg1NjQzLCJpYXQiOjE3MTYxOTkyNDMsImp0aSI6ImUwMzE4YzRkZWZmZTRhZTRiOGNkNTMwMmUwMzkzODNhIiwidXNlcl9pZCI6MX0.H9gX7Kn61uNqdTBxb_y_nT10WVZP_3Vmtxnlh_mrTWc",
											"type": "string"
										}
									]
								},
								"method": "POST",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "{\n    \"length\": 10,\n    \"start\": 1,\n    \"search\": \"\"\n}",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "{{local}}admin/all-category",
									"host": [
										"{{local}}admin"
									],
									"path": [
										"all-category"
									]
								}
							},
							"response": []
						},
						{
							"name": "get category by id",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE2Mjg1NjQzLCJpYXQiOjE3MTYxOTkyNDMsImp0aSI6ImUwMzE4YzRkZWZmZTRhZTRiOGNkNTMwMmUwMzkzODNhIiwidXNlcl9pZCI6MX0.H9gX7Kn61uNqdTBxb_y_nT10WVZP_3Vmtxnlh_mrTWc",
											"type": "string"
										}
									]
								},
								"method": "GET",
								"header": [],
								"url": {
									"raw": "{{local}}admin/get-categories-details-by-id/3",
									"host": [
										"{{local}}admin"
									],
									"path": [
										"get-categories-details-by-id",
										"3"
									]
								}
							},
							"response": []
						},
						{
							"name": "update category by id",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE1MjQ4MjgzLCJpYXQiOjE3MTUxNjE4ODMsImp0aSI6ImM2MDA4N2ViNjE3MzRlMGI5YjU4MGVmZDY2OWMyODRiIiwidXNlcl9pZCI6MX0.e0jZk0CKSDaPhhm3JOBWfmA2Z2MNFKPK_eiI7PSr19E",
											"type": "string"
										}
									]
								},
								"method": "PUT",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "{\n    \"name\": \"singers\"\n}",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "{{local}}admin/update-categories-detail-by-id/2",
									"host": [
										"{{local}}admin"
									],
									"path": [
										"update-categories-detail-by-id",
										"2"
									]
								}
							},
							"response": []
						},
						{
							"name": "delete category by id",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE1MjQ4MjgzLCJpYXQiOjE3MTUxNjE4ODMsImp0aSI6ImM2MDA4N2ViNjE3MzRlMGI5YjU4MGVmZDY2OWMyODRiIiwidXNlcl9pZCI6MX0.e0jZk0CKSDaPhhm3JOBWfmA2Z2MNFKPK_eiI7PSr19E",
											"type": "string"
										}
									]
								},
								"method": "DELETE",
								"header": [],
								"url": {
									"raw": "{{local}}admin/delete-category-by-id/6",
									"host": [
										"{{local}}admin"
									],
									"path": [
										"delete-category-by-id",
										"6"
									]
								}
							},
							"response": []
						},
						{
							"name": "get_all_subcategory",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE2MjgzMTkyLCJpYXQiOjE3MTYxOTY3OTIsImp0aSI6IjFiN2Q5YTVmOTg2ZTQ5NzM4MDI0NjMxY2ZmNGQ1ZDBiIiwidXNlcl9pZCI6MX0.s2oNGUp4XXKkCLTzn0-gaLCBGcXNUU3oz0dNGVlBQEw",
											"type": "string"
										}
									]
								},
								"method": "POST",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "{\n    \"category\": 1,\n    \"length\": 5,\n    \"start\": 1,\n    \"search\": \"\"\n}",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "{{dev}}admin/sub-category-based-on-category",
									"host": [
										"{{dev}}admin"
									],
									"path": [
										"sub-category-based-on-category"
									]
								}
							},
							"response": []
						},
						{
							"name": "get-subcategory-by-id",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE1NDE1NTYxLCJpYXQiOjE3MTUzMjkxNjEsImp0aSI6IjAxZDgzYWIzOTVhMjRjOGI5NmY4MjEzZjg5NTI4NTk1IiwidXNlcl9pZCI6MX0.YAZbq35330nwa5gxnJtaQMJ5aBzVk1K5mlDyX3cIg80",
											"type": "string"
										}
									]
								},
								"method": "GET",
								"header": [],
								"url": {
									"raw": "{{local}}admin/get-subcategory-by-id/5",
									"host": [
										"{{local}}admin"
									],
									"path": [
										"get-subcategory-by-id",
										"5"
									]
								}
							},
							"response": []
						},
						{
							"name": "update-subcategories-by-id",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE1NDE1NTYxLCJpYXQiOjE3MTUzMjkxNjEsImp0aSI6IjAxZDgzYWIzOTVhMjRjOGI5NmY4MjEzZjg5NTI4NTk1IiwidXNlcl9pZCI6MX0.YAZbq35330nwa5gxnJtaQMJ5aBzVk1K5mlDyX3cIg80",
											"type": "string"
										}
									]
								},
								"method": "PUT",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "{\n    \"name\": \"commercial shoots\"\n}",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "{{local}}admin/update-subcategory-by-id/5",
									"host": [
										"{{local}}admin"
									],
									"path": [
										"update-subcategory-by-id",
										"5"
									]
								}
							},
							"response": []
						},
						{
							"name": "delete-sub-cat-by-id",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE1NDE1NTYxLCJpYXQiOjE3MTUzMjkxNjEsImp0aSI6IjAxZDgzYWIzOTVhMjRjOGI5NmY4MjEzZjg5NTI4NTk1IiwidXNlcl9pZCI6MX0.YAZbq35330nwa5gxnJtaQMJ5aBzVk1K5mlDyX3cIg80",
											"type": "string"
										}
									]
								},
								"method": "DELETE",
								"header": [],
								"url": {
									"raw": "{{local}}admin/delete-subcategory-by-id/5",
									"host": [
										"{{local}}admin"
									],
									"path": [
										"delete-subcategory-by-id",
										"5"
									]
								}
							},
							"response": []
						},
						{
							"name": "update status",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE2MDE2Mzk0LCJpYXQiOjE3MTU5Mjk5OTQsImp0aSI6Ijg4YWQzYTAxOTQyNDQ5NDFhNWFiNmU3MDAxNjdkNDk5IiwidXNlcl9pZCI6MX0.KTqS3itNh3g3XBBtjdyfW-3BcTT02wZsIQKTjzJxfcs",
											"type": "string"
										}
									]
								},
								"method": "PATCH",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "{\r\n    \"is_active\": false\r\n}",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "{{local}}admin/update-status-of-category/1",
									"host": [
										"{{local}}admin"
									],
									"path": [
										"update-status-of-category",
										"1"
									]
								}
							},
							"response": []
						}
					]
				},
				{
					"name": "manage artist",
					"item": [
						{
							"name": "get all artist",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE2NDYzMjc3LCJpYXQiOjE3MTYzNzY4NzcsImp0aSI6ImJiNWM3YmRkNTgzZjQzZjRhM2NlMWVmZWYwNTcwNGM1IiwidXNlcl9pZCI6MX0.9O22WlSpX6Bzm9a8FEH-LDSV43I61cGRPaubg2x15HM",
											"type": "string"
										}
									]
								},
								"method": "POST",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "{\n    \"length\": 10,\n    \"start\": 1,\n    \"search\": \"\",\n    \"verification_status\": 0\n}",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "{{local}}admin/get-all-artist-details",
									"host": [
										"{{local}}admin"
									],
									"path": [
										"get-all-artist-details"
									]
								}
							},
							"response": []
						},
						{
							"name": "get-artist-by-id",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE2MDI2MTg3LCJpYXQiOjE3MTU5Mzk3ODcsImp0aSI6ImY3MDk1MzY5YmUwMTQzOTZhZTJjMGI1NTYxMWEyNThlIiwidXNlcl9pZCI6MX0.568wKij7N8FZj67D4b3vmKfxT12Or40FYNywnN3rDTY",
											"type": "string"
										}
									]
								},
								"method": "GET",
								"header": [],
								"url": {
									"raw": "{{local}}admin/get-artist-details-by-id/55",
									"host": [
										"{{local}}admin"
									],
									"path": [
										"get-artist-details-by-id",
										"55"
									]
								}
							},
							"response": []
						},
						{
							"name": "add artist",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE2MjcwNzc2LCJpYXQiOjE3MTYxODQzNzYsImp0aSI6IjFmYjIyZjg0NzIwZDRkOTU4NDY0MjJmMzNmYWYzNGY3IiwidXNlcl9pZCI6MX0.ihu60QSvwP7iCRwAzVcTc5J8Af-DCWqwvFeN5E4Be8o",
											"type": "string"
										}
									]
								},
								"method": "POST",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "{\r\n    \"profile_picture\": 1,\r\n    \"first_name\": \"fff\",\r\n    \"last_name\": \"ggg\",\r\n    \"email\": \"faeef@yopmail.com\",\r\n    \"phone_no\": \"3453333343333\",\r\n    \"country_code\": \"+91\",\r\n    \"gender\": \"1\",\r\n    \"date_of_birth\": \"2016-04-30\",\r\n    \"experience\": \"12\",\r\n    \"address\": \"asdas\",\r\n    \"country\": \"asdas\",\r\n    \"state\": \"asdasd\",\r\n    \"city\": \"asdasasdas\",\r\n    \"booking_method\": \"1\",\r\n    \"categories\": [\r\n        9\r\n    ],\r\n    \"sub_categories\": [\r\n        9\r\n    ],\r\n    \"portfolio\": 1,\r\n    \"cover_photo\": 1,\r\n    \"bust\": null,\r\n    \"waist\": null,\r\n    \"hips\": null,\r\n    \"height_feet\": null,\r\n    \"height_inches\": null,\r\n    \"weight\": null,\r\n    \"hair_color\": null,\r\n    \"eye_color\": null\r\n}",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "{{dev}}admin/add-artist",
									"host": [
										"{{dev}}admin"
									],
									"path": [
										"add-artist"
									]
								}
							},
							"response": []
						},
						{
							"name": "update artist",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE1NzU0MTMzLCJpYXQiOjE3MTU2Njc3MzMsImp0aSI6IjdhZWY4MGU5MjI4OTQ1MWE4ZDk3NDk4YTc4ZGYxOWQwIiwidXNlcl9pZCI6MX0.HHt3ILfNJqq9sT74AaaTwu-p3y_CHG2wHxBwp44eNNE",
											"type": "string"
										}
									]
								},
								"method": "PUT",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "{\r\n    \"first_name\": \"kane\",\r\n    \"last_name\": \"williamson\",\r\n    \"email\": \"kane0@yopmail.com\",\r\n    \"phone_no\": \"9076543211\",\r\n    \"date_of_birth\": \"2020-09-09\",\r\n    \"experience\": \"5 years\",\r\n    \"gender\": 1,\r\n    \"country_code\": \"+91\",\r\n    \"address\": \"456 Elm St\",\r\n    \"city\": \"London\",\r\n    \"state\": \"NY\",\r\n    \"country\": \"UK\",\r\n    \"profile_picture\": 1,\r\n    \"bust\": 10,\r\n    \"waist\": 10, \r\n    \"hips\": 10,\r\n    \"height_feet\": 10,\r\n    \"height_inches\": 1,\r\n    \"weight\": 10,\r\n    \"hair_color\": 1,\r\n    \"eye_color\": 1,\r\n    \"booking_method\": 1,\r\n    \"portfolio\": 1,\r\n    \"cover_photo\": 1,\r\n    \"categories\": [1],\r\n    \"sub_categories\": [1]\r\n}",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "{{local}}admin/update-artist-details-by-id/44",
									"host": [
										"{{local}}admin"
									],
									"path": [
										"update-artist-details-by-id",
										"44"
									]
								}
							},
							"response": []
						},
						{
							"name": "delete arrtist",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE1NjYzNjU1LCJpYXQiOjE3MTU1NzcyNTUsImp0aSI6ImQ4YTdjMmMwYmJjYTRmYmFiYzUwYjdkNDc2OGQ1ZWIzIiwidXNlcl9pZCI6MX0.s61JF9GLc7lYFq1JVobeObPl_k4pOkdjj8AXQKAVYsc",
											"type": "string"
										}
									]
								},
								"method": "DELETE",
								"header": [],
								"url": {
									"raw": "{{local}}admin/delete-artist-details-by-id/11",
									"host": [
										"{{local}}admin"
									],
									"path": [
										"delete-artist-details-by-id",
										"11"
									]
								}
							},
							"response": []
						},
						{
							"name": "verify artist",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE1ODQ4MTQ5LCJpYXQiOjE3MTU3NjE3NDksImp0aSI6IjFlNmY4MjdiZDgyZTQ0ZTNhMmY3NDlhZDZhYTg4MTMyIiwidXNlcl9pZCI6MX0.o4OFFgD-qr0SIcXm5XNRPtKvk9aQAWrbc7p7nn9xP04",
											"type": "string"
										}
									]
								},
								"method": "PATCH",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "{\r\n    \"verification_status\": 1\r\n}",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "{{local}}admin/verify-artist/19",
									"host": [
										"{{local}}admin"
									],
									"path": [
										"verify-artist",
										"19"
									]
								}
							},
							"response": []
						},
						{
							"name": "booking history",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE2NDYzMjc3LCJpYXQiOjE3MTYzNzY4NzcsImp0aSI6ImJiNWM3YmRkNTgzZjQzZjRhM2NlMWVmZWYwNTcwNGM1IiwidXNlcl9pZCI6MX0.9O22WlSpX6Bzm9a8FEH-LDSV43I61cGRPaubg2x15HM",
											"type": "string"
										}
									]
								},
								"method": "POST",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "{\r\n    \"length\": 10,\r\n    \"start\": 1,\r\n    \"search\": \"\",\r\n    \"key\": 1\r\n}",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "{{local}}admin/artist-bookings/38",
									"host": [
										"{{local}}admin"
									],
									"path": [
										"artist-bookings",
										"38"
									]
								}
							},
							"response": []
						}
					]
				},
				{
					"name": "booking module",
					"item": [
						{
							"name": "bookings",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE1NzU0MTMzLCJpYXQiOjE3MTU2Njc3MzMsImp0aSI6IjdhZWY4MGU5MjI4OTQ1MWE4ZDk3NDk4YTc4ZGYxOWQwIiwidXNlcl9pZCI6MX0.HHt3ILfNJqq9sT74AaaTwu-p3y_CHG2wHxBwp44eNNE",
											"type": "string"
										}
									]
								},
								"method": "POST",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "{\n    \"length\": 10,\n    \"start\": 1,\n    \"search\": \"\",\n    \"key\": 3\n}",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "{{local}}admin/bookings",
									"host": [
										"{{local}}admin"
									],
									"path": [
										"bookings"
									]
								}
							},
							"response": []
						},
						{
							"name": "get booking",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE2ODc0ODY5LCJpYXQiOjE3MTY3ODg0NjksImp0aSI6ImIyZTIwMGEzMmVjMjQ2M2ZiNGM3ZTdhMjc5ZGEyMTA2IiwidXNlcl9pZCI6MX0.SSbbS3YKNt-D1lwgL-MtMrntjOeZcdQaKuR_9sNwPUI",
											"type": "string"
										}
									]
								},
								"method": "GET",
								"header": [],
								"url": {
									"raw": "{{local}}admin/booking/6",
									"host": [
										"{{local}}admin"
									],
									"path": [
										"booking",
										"6"
									]
								}
							},
							"response": []
						}
					]
				},
				{
					"name": "Manage sub admin",
					"item": [
						{
							"name": "add sub admin",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE1NjYzNjU1LCJpYXQiOjE3MTU1NzcyNTUsImp0aSI6ImQ4YTdjMmMwYmJjYTRmYmFiYzUwYjdkNDc2OGQ1ZWIzIiwidXNlcl9pZCI6MX0.s61JF9GLc7lYFq1JVobeObPl_k4pOkdjj8AXQKAVYsc",
											"type": "string"
										}
									]
								},
								"method": "POST",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "{\r\n  \"first_name\": \"ram\",\r\n  \"last_name\": \"Doe\",\r\n  \"email\": \"jass@yopmail.com\",\r\n  \"country_code\": \"+91\",\r\n  \"profile_picture\": 1,\r\n  \"phone_no\": \"1234590\",\r\n  \"permissions\": [\r\n    {\r\n      \"module\": 1,\r\n      \"is_add_edit\": true,\r\n      \"is_view\": true,\r\n      \"is_delete\": true\r\n    },\r\n    {\r\n      \"module\": 2,\r\n      \"is_add_edit\": true,\r\n      \"is_view\": false,\r\n      \"is_delete\": false\r\n    },\r\n    {\r\n      \"module\": 3,\r\n      \"is_add_edit\": true,\r\n      \"is_view\": false,\r\n      \"is_delete\": false\r\n    },\r\n    {\r\n      \"module\": 4,\r\n      \"is_add_edit\": true,\r\n      \"is_view\": false,\r\n      \"is_delete\": false\r\n    },\r\n    {\r\n      \"module\": 5,\r\n      \"is_add_edit\": true,\r\n      \"is_view\": false,\r\n      \"is_delete\": false\r\n    },\r\n    {\r\n      \"module\": 6,\r\n      \"is_add_edit\": true,\r\n      \"is_view\": false,\r\n      \"is_delete\": false\r\n    },\r\n    {\r\n      \"module\": 7,\r\n      \"is_add_edit\": true,\r\n      \"is_view\": false,\r\n      \"is_delete\": false\r\n    },\r\n    {\r\n      \"module\": 8,\r\n      \"is_add_edit\": true,\r\n      \"is_view\": false,\r\n      \"is_delete\": false\r\n    }\r\n  ]\r\n\r\n}\r\n",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "{{local}}admin/add-sub-admin",
									"host": [
										"{{local}}admin"
									],
									"path": [
										"add-sub-admin"
									]
								}
							},
							"response": []
						},
						{
							"name": "get sub admin",
							"request": {
								"method": "GET",
								"header": [],
								"url": {
									"raw": ""
								}
							},
							"response": []
						},
						{
							"name": "update sub admin",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE1NjYzNjU1LCJpYXQiOjE3MTU1NzcyNTUsImp0aSI6ImQ4YTdjMmMwYmJjYTRmYmFiYzUwYjdkNDc2OGQ1ZWIzIiwidXNlcl9pZCI6MX0.s61JF9GLc7lYFq1JVobeObPl_k4pOkdjj8AXQKAVYsc",
											"type": "string"
										}
									]
								},
								"method": "PUT",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "{\r\n        \"id\": 14,\r\n        \"username\": null,\r\n        \"country_code\": \"\",\r\n        \"email\": \"jass@yopmail.com\",\r\n        \"phone_no\": \"1234590\",\r\n        \"address\": \"\",\r\n        \"profile_picture\": 1,\r\n        \"permissions\": [\r\n            {\r\n                \"id\": 2,\r\n                \"module\": 1,\r\n                \"can_add_edit\": true,\r\n                \"can_view\": false,\r\n                \"can_be_delete\": false\r\n            },\r\n            {\r\n                \"id\": 3,\r\n                \"module\": 2,\r\n                \"can_add_edit\": false,\r\n                \"can_view\": false,\r\n                \"can_be_delete\": false\r\n            },\r\n            {\r\n                \"id\": 4,\r\n                \"module\": 3,\r\n                \"can_add_edit\": false,\r\n                \"can_view\": false,\r\n                \"can_be_delete\": false\r\n            },\r\n            {\r\n                \"id\": 5,\r\n                \"module\": 4,\r\n                \"can_add_edit\": false,\r\n                \"can_view\": false,\r\n                \"can_be_delete\": false\r\n            },\r\n            {\r\n                \"id\": 6,\r\n                \"module\": 5,\r\n                \"can_add_edit\": false,\r\n                \"can_view\": false,\r\n                \"can_be_delete\": false\r\n            },\r\n            {\r\n                \"id\": 7,\r\n                \"module\": 6,\r\n                \"can_add_edit\": false,\r\n                \"can_view\": false,\r\n                \"can_be_delete\": false\r\n            },\r\n            {\r\n                \"id\": 8,\r\n                \"module\": 7,\r\n                \"can_add_edit\": false,\r\n                \"can_view\": false,\r\n                \"can_be_delete\": false\r\n            },\r\n            {\r\n                \"id\": 9,\r\n                \"module\": 8,\r\n                \"can_add_edit\": false,\r\n                \"can_view\": false,\r\n                \"can_be_delete\": false\r\n            }\r\n        ]\r\n    }",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "{{local}}admin/update-sub-admin/14",
									"host": [
										"{{local}}admin"
									],
									"path": [
										"update-sub-admin",
										"14"
									]
								}
							},
							"response": []
						},
						{
							"name": "all sub admins",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE1NjYzNjU1LCJpYXQiOjE3MTU1NzcyNTUsImp0aSI6ImQ4YTdjMmMwYmJjYTRmYmFiYzUwYjdkNDc2OGQ1ZWIzIiwidXNlcl9pZCI6MX0.s61JF9GLc7lYFq1JVobeObPl_k4pOkdjj8AXQKAVYsc",
											"type": "string"
										}
									]
								},
								"method": "POST",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "{\r\n    \"length\": 10,\r\n    \"start\": 1,\r\n    \"search\": \"\"\r\n}",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "{{local}}admin/get-all-sub-admin",
									"host": [
										"{{local}}admin"
									],
									"path": [
										"get-all-sub-admin"
									]
								}
							},
							"response": []
						},
						{
							"name": "delete sub admin",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE1NjYzNjU1LCJpYXQiOjE3MTU1NzcyNTUsImp0aSI6ImQ4YTdjMmMwYmJjYTRmYmFiYzUwYjdkNDc2OGQ1ZWIzIiwidXNlcl9pZCI6MX0.s61JF9GLc7lYFq1JVobeObPl_k4pOkdjj8AXQKAVYsc",
											"type": "string"
										}
									]
								},
								"method": "DELETE",
								"header": [],
								"url": {
									"raw": "{{local}}admin/delete-sub-admin/14",
									"host": [
										"{{local}}admin"
									],
									"path": [
										"delete-sub-admin",
										"14"
									]
								}
							},
							"response": []
						}
					]
				},
				{
					"name": "Manage Notifications",
					"item": [
						{
							"name": "add notifications",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE1OTU5MTk5LCJpYXQiOjE3MTU4NzI3OTksImp0aSI6ImNlNjA0YmVhNWJmODQ1MDc5YTk3MzZhMjQ5MDY0M2ZjIiwidXNlcl9pZCI6MX0.z0L1p33H6Ucte99gMPZ3UigEQ8EFNNVKmnJF4SnujPA",
											"type": "string"
										}
									]
								},
								"method": "POST",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "{\r\n    \"notification_for\": 1,\r\n    \"notification_type\": 1,\r\n    \"notification_title\": \"Lorem Ipsum\",\r\n    \"notification_description\": \"Lorem ipsum, dolor sit amet consectetur adipisicing elit. Expedita totam consectetur, dignissimos\"\r\n}",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "{{local}}admin/add-notifications",
									"host": [
										"{{local}}admin"
									],
									"path": [
										"add-notifications"
									]
								}
							},
							"response": []
						},
						{
							"name": "all notifications",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE1OTU5MTk5LCJpYXQiOjE3MTU4NzI3OTksImp0aSI6ImNlNjA0YmVhNWJmODQ1MDc5YTk3MzZhMjQ5MDY0M2ZjIiwidXNlcl9pZCI6MX0.z0L1p33H6Ucte99gMPZ3UigEQ8EFNNVKmnJF4SnujPA",
											"type": "string"
										}
									]
								},
								"method": "POST",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "{\r\n    \"length\": 10,\r\n    \"start\": 1,\r\n    \"search\": \"\"\r\n}",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "{{local}}admin/all-notifications",
									"host": [
										"{{local}}admin"
									],
									"path": [
										"all-notifications"
									]
								}
							},
							"response": []
						}
					]
				}
			]
		},
		{
			"name": "Client",
			"item": [
				{
					"name": "Booking",
					"item": [
						{
							"name": "talent-details",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE2MzcxNTM1LCJpYXQiOjE3MTYyODUxMzUsImp0aSI6IjQyMjBiMWMyODMxMzRjZDM5NmJkMmY0N2Y3MWU5YWI2IiwidXNlcl9pZCI6Mzd9.XoTiQN8VJM74XeSmcHpt9l1H90EFUIEyiqTn_nDHk38",
											"type": "string"
										}
									]
								},
								"method": "POST",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "{\n    \"sub_category\": [4, 5]\n}",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "{{local}}client/talent-detials",
									"host": [
										"{{local}}client"
									],
									"path": [
										"talent-detials"
									]
								}
							},
							"response": []
						},
						{
							"name": "all services",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE2MjgxMDc5LCJpYXQiOjE3MTYxOTQ2NzksImp0aSI6IjIwNTcxYTMxNDhmMTQ2OTQ4ZTdiYzk4Zjc0M2ZhZjhmIiwidXNlcl9pZCI6Mzd9.F1Zy0eZOpsLSITsc6OrFbwf0TQZvjsDXfSi-kZpVnw4",
											"type": "string"
										}
									]
								},
								"method": "GET",
								"header": [],
								"url": {
									"raw": "{{local}}client/all-services/38",
									"host": [
										"{{local}}client"
									],
									"path": [
										"all-services",
										"38"
									]
								}
							},
							"response": []
						},
						{
							"name": "talent slots by date",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE4Mzg1MDQxLCJpYXQiOjE3MTgyOTg2NDEsImp0aSI6Ijk4ZWU4YTM2N2UzNTQyMzY5NTA2MmJjZWQ1NTViMmZmIiwidXNlcl9pZCI6NTh9.HZYCCmh7mZv2pAWzpHRSTgW2Ulx7Z0qhBHVbzlFfGbQ",
											"type": "string"
										}
									]
								},
								"method": "POST",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "{\r\n    \"date\": \"2024-06-17\",\r\n    \"user\": 57\r\n}",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "{{local}}client/talent-slots-by-date",
									"host": [
										"{{local}}client"
									],
									"path": [
										"talent-slots-by-date"
									]
								}
							},
							"response": []
						},
						{
							"name": "get-booking-details-by-id",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE3MDQ5MDczLCJpYXQiOjE3MTY5NjI2NzMsImp0aSI6IjA2MGEwNGIxN2I5YTQ2OWE5ZDA5YmU1MmViYTQyMzJmIiwidXNlcl9pZCI6Mzd9.LStLuU4KrXVWh2q7jyMrarhwUY89fcA07F2CgY5ZA84",
											"type": "string"
										}
									]
								},
								"method": "GET",
								"header": [],
								"url": {
									"raw": "{{local}}client/fetch-booking-details/6",
									"host": [
										"{{local}}client"
									],
									"path": [
										"fetch-booking-details",
										"6"
									]
								}
							},
							"response": []
						},
						{
							"name": "book talent",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE4MjkyNDAxLCJpYXQiOjE3MTgyMDYwMDEsImp0aSI6ImI1ODk1OGExZDc1MzQwNjJhN2MzMTBlMjExZGUyMDU1IiwidXNlcl9pZCI6MTI5fQ.9LEe9M4I1MMZ7tB2wdcJf1iY_oW4ERaBwO5VbVGVtgM",
											"type": "string"
										}
									]
								},
								"method": "POST",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "{\n    \"talent\": 171,\n    \"address\": 8,\n    \"date\": \"2024-06-12\",\n    \"time\": \"22:00\",\n    \"duration\": 1,\n    \"offer_price\": 100,\n    \"comment\": \"Test comment\",\n    \"currency\": \"USD\",\n    \"services\": [\n                    {\n                        \"price\": 100,\n                        \"service\": \"facial\"\n                    }\n                ]\n}",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "{{dev}}client/book-talent",
									"host": [
										"{{dev}}client"
									],
									"path": [
										"book-talent"
									]
								}
							},
							"response": []
						},
						{
							"name": "talent-details-by-id",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE2NDUzNzE0LCJpYXQiOjE3MTYzNjczMTQsImp0aSI6ImE1MWQ5MzEzZjM3MzRiZTc4ZGZmNGUyN2ZhZTFmMjhjIiwidXNlcl9pZCI6Mzd9.8stus8QO8Ngs4aXNehfDIVNq675vvZE3bED0qpN0bWc",
											"type": "string"
										}
									]
								},
								"method": "GET",
								"header": [],
								"url": {
									"raw": "{{local}}client/talent-detials-by-id/38",
									"host": [
										"{{local}}client"
									],
									"path": [
										"talent-detials-by-id",
										"38"
									]
								}
							},
							"response": []
						},
						{
							"name": "ongoing bookings",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE2MzU1OTE0LCJpYXQiOjE3MTYyNjk1MTQsImp0aSI6ImI4NWZhYWEzNDA1YTQ3NzU4ZmJhMDMxMjVmZGMzNzg0IiwidXNlcl9pZCI6Mzd9.ksvLUXO07rmD5dCHJsj1UtoVrnqRtTpObVwPC1O9fYg",
											"type": "string"
										}
									]
								},
								"method": "GET",
								"header": [],
								"url": {
									"raw": "{{local}}client/ongoing-bookings",
									"host": [
										"{{local}}client"
									],
									"path": [
										"ongoing-bookings"
									]
								}
							},
							"response": []
						},
						{
							"name": "mark booking completed",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE3ODAxMjg0LCJpYXQiOjE3MTc3MTQ4ODQsImp0aSI6ImEzYjAxMjM2NzQxNDQ1ZTdiNmExOGFhNGIxMDczNjVlIiwidXNlcl9pZCI6Mzd9.7xvCXNH3fF_vp8qfhyIhbvrG80l7A1etx8d0JMaxDp4",
											"type": "string"
										}
									]
								},
								"method": "POST",
								"header": [],
								"url": {
									"raw": "{{local}}client/mark-booking-completed/16",
									"host": [
										"{{local}}client"
									],
									"path": [
										"mark-booking-completed",
										"16"
									]
								}
							},
							"response": []
						},
						{
							"name": "completed bookings",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE2MTg0MDk3LCJpYXQiOjE3MTYwOTc2OTcsImp0aSI6ImE1NDU3MDRkMmEwZTQyYjg5MjQ3MmFlNDg2Mjg5YzVjIiwidXNlcl9pZCI6Mzd9.CeOWN7h_ok2MbvU0GSAvaBTgYIGtYIMcarZQpKQULyU",
											"type": "string"
										}
									]
								},
								"method": "GET",
								"header": [],
								"url": {
									"raw": "{{local}}client/completed-bookings",
									"host": [
										"{{local}}client"
									],
									"path": [
										"completed-bookings"
									]
								}
							},
							"response": []
						},
						{
							"name": "cancelled bookings",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE2MTg0MDk3LCJpYXQiOjE3MTYwOTc2OTcsImp0aSI6ImE1NDU3MDRkMmEwZTQyYjg5MjQ3MmFlNDg2Mjg5YzVjIiwidXNlcl9pZCI6Mzd9.CeOWN7h_ok2MbvU0GSAvaBTgYIGtYIMcarZQpKQULyU",
											"type": "string"
										}
									]
								},
								"method": "GET",
								"header": [],
								"url": {
									"raw": "{{local}}client/cancelled-bookings",
									"host": [
										"{{local}}client"
									],
									"path": [
										"cancelled-bookings"
									]
								}
							},
							"response": []
						},
						{
							"name": "accept/decline booking",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE2ODk4MjI4LCJpYXQiOjE3MTY4MTE4MjgsImp0aSI6IjUzOTk3OTJjNDdhNjRmN2FiNzljZDdkMWYwM2NmOTZkIiwidXNlcl9pZCI6Mzd9.SuV2MfKJO4tV0TYYtjF58Xf7LXMUBi_zcduJ0jyZhp0",
											"type": "string"
										}
									]
								},
								"method": "PATCH",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "{\r\n    \"accept\": true,\r\n    \"cancellation_reason\": \"price is too much\"\r\n}",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "{{local}}client/accept-decline-booking/6",
									"host": [
										"{{local}}client"
									],
									"path": [
										"accept-decline-booking",
										"6"
									]
								}
							},
							"response": []
						},
						{
							"name": "filter&sort",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE3ODAxMjg0LCJpYXQiOjE3MTc3MTQ4ODQsImp0aSI6ImEzYjAxMjM2NzQxNDQ1ZTdiNmExOGFhNGIxMDczNjVlIiwidXNlcl9pZCI6Mzd9.7xvCXNH3fF_vp8qfhyIhbvrG80l7A1etx8d0JMaxDp4",
											"type": "string"
										}
									]
								},
								"method": "POST",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "{\r\n    \"search\": {\r\n        \"search_value\": \"\"\r\n    },\r\n    \"filters\": {\r\n        \"height_feet\": 10,\r\n        \"height_inches\": 11,\r\n        \"experience\": [1,4],\r\n        // \"categories\": [1, 2],\r\n        // \"sub_categories\": [4],\r\n        // \"gender\": 1,\r\n        // \"hair_color\": 1,\r\n        // \"eye_color\": 1,\r\n        // \"weight\": [40, 58],\r\n        \"bust\": [10, 30],\r\n        // \"waist\": [10, 30],\r\n        // \"hips\": [10, 20],\r\n        // \"nationality\": \"IN\",\r\n        // \"city\": \"new york\",\r\n        \"state\": \"los angeles\",\r\n        \"date\": \"2024-05-28\",\r\n        \"time\": [2]\r\n        // \"booking_method\": [1,2]\r\n    }\r\n    // \"sort\": {\r\n    //     \"sort_value\": 1 \r\n    // }\r\n}",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "{{local}}client/filter-talent",
									"host": [
										"{{local}}client"
									],
									"path": [
										"filter-talent"
									]
								}
							},
							"response": []
						},
						{
							"name": "talent details booking screen",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE2MjgzNjIxLCJpYXQiOjE3MTYxOTcyMjEsImp0aSI6IjdkZDc3NGRhMzg0OTRhNTJhZWY3NTc3N2JkOGZmMmIwIiwidXNlcl9pZCI6Mzd9.Bomn_UjOEeYrc31TGb3CpRib6vW0gf-K88ZrEF0SHCg",
											"type": "string"
										}
									]
								},
								"method": "GET",
								"header": [],
								"url": {
									"raw": "{{local}}client/talent-detials-for-booking/19",
									"host": [
										"{{local}}client"
									],
									"path": [
										"talent-detials-for-booking",
										"19"
									]
								}
							},
							"response": []
						}
					]
				},
				{
					"name": "Auth",
					"item": [
						{
							"name": "Sign-up",
							"request": {
								"method": "POST",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "{\n    \"encoded_id\": \"Nzg1MTM3Mg==\",\n    \"profile_picture\": 1,\n    \"first_name\": \"Alice\",\n    \"last_name\": \"Smith\",\n    \"gender\": 1,\n    \"date_of_birth\": \"2000-09-07\",\n    \"email\": \"client13@yopmail.com\",\n    \"password\":\"alice123\",\n    \"phone_no\": \"987281200\",\n    \"country_code\": \"+91\",\n    \"address\": \"456 Elm St\",\n    \"city\": \"London\",\n    \"state\": \"NY\",\n    \"country\": \"UK\"\n}",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "{{local}}client/signup",
									"host": [
										"{{local}}client"
									],
									"path": [
										"signup"
									]
								}
							},
							"response": []
						},
						{
							"name": "login",
							"request": {
								"method": "POST",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "{\n    \"country_code\": \"+91\",\n    \"phone_no\":\"987281200\"\n    // \"otp\":\"123456\"\n    // \"email\":\"client13@yopmail.com\",\n    // \"password\":\"alice123\"\n}",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "{{local}}client/log-in",
									"host": [
										"{{local}}client"
									],
									"path": [
										"log-in"
									]
								}
							},
							"response": []
						},
						{
							"name": "otp-verification",
							"request": {
								"method": "POST",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "{\n    // \"email\": \"client13@yopmail.com\",\n    \"country_code\": \"+91\",\n    \"phone_no\": \"987281200\",\n    \"otp\":\"1234\"\n}",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "{{local}}client/verify-otp",
									"host": [
										"{{local}}client"
									],
									"path": [
										"verify-otp"
									]
								}
							},
							"response": []
						},
						{
							"name": "resendOtp",
							"request": {
								"method": "POST",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "{\n    \"encoded_id\": \"Nzg1MTM3Mg==\",\n    // \"email\": \"client13@yopmail.com\"\n    \"country_code\": \"+91\",\n    \"phone_no\": \"987281200\"\n}",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "{{local}}client/resend-otp",
									"host": [
										"{{local}}client"
									],
									"path": [
										"resend-otp"
									]
								}
							},
							"response": []
						},
						{
							"name": "verify -opt-without-register",
							"request": {
								"method": "POST",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "{\n    // \"email\": \"ram9014@yopmail.com\"\n    \"phone_no\": \"9872812\"\n}",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "{{local}}verify-without-otp/",
									"host": [
										"{{local}}verify-without-otp"
									],
									"path": [
										""
									]
								}
							},
							"response": []
						},
						{
							"name": "listing categories",
							"request": {
								"method": "GET",
								"header": [],
								"url": {
									"raw": ""
								}
							},
							"response": []
						},
						{
							"name": "subcategories-Listing",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE0NjQ5NzU5LCJpYXQiOjE3MTQ1NjMzNTksImp0aSI6IjFiMzBjOWUzNzEzMjRkOTA5YTM0N2I4ZTVkMzk1ODI0IiwidXNlcl9pZCI6Mn0.phHZrtB-PHBHnAk2mjL3AVtCiBZAbA6UO3cPcYPHKNY",
											"type": "string"
										}
									]
								},
								"method": "POST",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "{\n    \"category\":1\n}",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "{{local}}client/talent-depends-sub-categories",
									"host": [
										"{{local}}client"
									],
									"path": [
										"talent-depends-sub-categories"
									]
								}
							},
							"response": []
						},
						{
							"name": "change password",
							"request": {
								"method": "POST",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "{\r\n    \"old_password\": \"9014\",\r\n    \"new_password\": \"1234\"\r\n}",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "{{local}}client/change-password",
									"host": [
										"{{local}}client"
									],
									"path": [
										"change-password"
									]
								}
							},
							"response": []
						},
						{
							"name": "profile details",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE2NzEwMTAyLCJpYXQiOjE3MTY2MjM3MDIsImp0aSI6IjI4MmViNzQzY2FiNzQyYTg4Zjc4MDQ0MTdjYTRjMDRlIiwidXNlcl9pZCI6OTR9.qSsU5jy34up1F5erdmHOaCmj6aMboXj8a3IDAgSbZ5I",
											"type": "string"
										}
									]
								},
								"method": "GET",
								"header": [],
								"url": {
									"raw": "{{dev}}client/profile-details",
									"host": [
										"{{dev}}client"
									],
									"path": [
										"profile-details"
									]
								}
							},
							"response": []
						},
						{
							"name": "edit profile",
							"request": {
								"auth": {
									"type": "bearer",
									"bearer": [
										{
											"key": "token",
											"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE2NzEwMTAyLCJpYXQiOjE3MTY2MjM3MDIsImp0aSI6IjI4MmViNzQzY2FiNzQyYTg4Zjc4MDQ0MTdjYTRjMDRlIiwidXNlcl9pZCI6OTR9.qSsU5jy34up1F5erdmHOaCmj6aMboXj8a3IDAgSbZ5I",
											"type": "string"
										}
									]
								},
								"method": "PUT",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "{\r\n    \"first_name\": \"Justin\",\r\n    \"last_name\": \"Beiber\",\r\n    \"address\": \"Toronto City , Canada\",\r\n    \"city\": \"Toronto\",\r\n    \"state\": \"Brampton\",\r\n    \"country\": \"Canada\",\r\n    \"profile_picture\": 303\r\n}",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "{{dev}}client/edit-profile",
									"host": [
										"{{dev}}client"
									],
									"path": [
										"edit-profile"
									]
								}
							},
							"response": []
						},
						{
							"name": "otp to user",
							"request": {
								"method": "POST",
								"header": [],
								"body": {
									"mode": "raw",
									"raw": "{\r\n    \"country_code\": \"+91\",\r\n    \"phone_no\": \"987281200\"\r\n}",
									"options": {
										"raw": {
											"language": "json"
										}
									}
								},
								"url": {
									"raw": "{{local}}client/otp-to-user",
									"host": [
										"{{local}}client"
									],
									"path": [
										"otp-to-user"
									]
								}
							},
							"response": []
						}
					]
				}
			]
		},
		{
			"name": "Add-Address Crud",
			"item": [
				{
					"name": "add-new-address",
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE2Mjg3MTIyLCJpYXQiOjE3MTYyMDA3MjIsImp0aSI6IjI0ZTExODUyYzlkMDQwNTZhMTcyYmM3OTA1MGRhYTdmIiwidXNlcl9pZCI6Mzd9.FMUwc3ZPSXf0HCokX-BMuzViuRw7dSPvhHkasa5BQ8I",
									"type": "string"
								}
							]
						},
						"method": "POST",
						"header": [],
						"body": {
							"mode": "raw",
							"raw": "// {\n//     \"address_location\": \"123 Main Street\",\n//     \"house_flat_block_no\": \"Apartment 101\",\n//     \"landmark\": \"Near City Park\",\n//     \"street_no\": \"ABC Street\",\n//     \"phone_no_manage_address\": \"1234567890\",\n//     \"address_type\": 1\n// }\n\n{\n    \"address_location\": \"456 Elm Street\",\n    \"house_flat_block_no\": \"Unit B\",\n    \"landmark\": \"Next to ABC Store\",\n    \"street_no\": \"XYZ Avenue\",\n    \"phone_no_manage_address\": \"9876543210\",\n    \"address_type\": 2\n}",
							"options": {
								"raw": {
									"language": "json"
								}
							}
						},
						"url": {
							"raw": "{{local}}client/address",
							"host": [
								"{{local}}client"
							],
							"path": [
								"address"
							]
						}
					},
					"response": []
				},
				{
					"name": "get-all-records-by-token",
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE0NTY3ODMxLCJpYXQiOjE3MTQ0ODE0MzEsImp0aSI6ImIwYTEwYjQ2MzI4MzRlZTBiZWZmMDkwNzU4YmJiMzU2IiwidXNlcl9pZCI6NH0.kxa4YR_duTvjUayrYJdvvCFyOtn1uq47GrEUaL1RKFg",
									"type": "string"
								}
							]
						},
						"method": "GET",
						"header": [],
						"url": {
							"raw": "{{local}}client/all-address",
							"host": [
								"{{local}}client"
							],
							"path": [
								"all-address"
							]
						}
					},
					"response": []
				},
				{
					"name": "edit-address-details",
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE0NTY3ODMxLCJpYXQiOjE3MTQ0ODE0MzEsImp0aSI6ImIwYTEwYjQ2MzI4MzRlZTBiZWZmMDkwNzU4YmJiMzU2IiwidXNlcl9pZCI6NH0.kxa4YR_duTvjUayrYJdvvCFyOtn1uq47GrEUaL1RKFg",
									"type": "string"
								}
							]
						},
						"method": "PUT",
						"header": [],
						"body": {
							"mode": "raw",
							"raw": "{\n    // {\n    \"address_location\": \"458 Elm Street\",\n    \"house_flat_block_no\": \"Unit c\"\n//     \"landmark\": \"Next to ABC Store\",\n//     \"street_no\": \"XYZ Avenue\",\n//     \"phone_no_manage_address\": \"9876543210\",\n//     \"address_type\": 2\n// }\n}",
							"options": {
								"raw": {
									"language": "json"
								}
							}
						},
						"url": {
							"raw": "{{local}}client/address-details/2",
							"host": [
								"{{local}}client"
							],
							"path": [
								"address-details",
								"2"
							]
						}
					},
					"response": []
				},
				{
					"name": "Delete-address",
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE0NTY3ODMxLCJpYXQiOjE3MTQ0ODE0MzEsImp0aSI6ImIwYTEwYjQ2MzI4MzRlZTBiZWZmMDkwNzU4YmJiMzU2IiwidXNlcl9pZCI6NH0.kxa4YR_duTvjUayrYJdvvCFyOtn1uq47GrEUaL1RKFg",
									"type": "string"
								}
							]
						},
						"method": "DELETE",
						"header": [],
						"url": {
							"raw": "{{local}}client/delete-address/2",
							"host": [
								"{{local}}client"
							],
							"path": [
								"delete-address",
								"2"
							]
						}
					},
					"response": []
				}
			]
		},
		{
			"name": "FAQ",
			"item": [
				{
					"name": "show-all-records",
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE2NTM5MDAyLCJpYXQiOjE3MTY0NTI2MDIsImp0aSI6ImZkMGQ4OWNmNjYzNzQxNzBiZjhmY2UyYTIwYmI5MTExIiwidXNlcl9pZCI6Mzd9.AJj3cxlGG5EntNV8_s8JoPqEGTOrF5davXWGXrWW1yU",
									"type": "string"
								}
							]
						},
						"method": "POST",
						"header": [],
						"body": {
							"mode": "raw",
							"raw": "{\r\n    \"length\": 10,\r\n    \"start\": 1,\r\n    \"search\": \"\"\r\n}",
							"options": {
								"raw": {
									"language": "json"
								}
							}
						},
						"url": {
							"raw": "{{local}}show-questions",
							"host": [
								"{{local}}show-questions"
							]
						}
					},
					"response": []
				},
				{
					"name": "add-questions-answers",
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE2NTM5MDAyLCJpYXQiOjE3MTY0NTI2MDIsImp0aSI6ImZkMGQ4OWNmNjYzNzQxNzBiZjhmY2UyYTIwYmI5MTExIiwidXNlcl9pZCI6Mzd9.AJj3cxlGG5EntNV8_s8JoPqEGTOrF5davXWGXrWW1yU",
									"type": "string"
								}
							]
						},
						"method": "POST",
						"header": [],
						"body": {
							"mode": "raw",
							"raw": "{\n    \"question\":\"hellojsadhflkja\",\n    \"answer\":\"jalskdjfalkjsfdalkjdf\"\n}",
							"options": {
								"raw": {
									"language": "json"
								}
							}
						},
						"url": {
							"raw": "{{local}}admin/questions",
							"host": [
								"{{local}}admin"
							],
							"path": [
								"questions"
							]
						}
					},
					"response": []
				},
				{
					"name": "update-question-answer",
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE0NjMxNzIxLCJpYXQiOjE3MTQ1NDUzMjEsImp0aSI6ImUyNWU4NGQ1NzJmMTRiYjZiYmE4YjAxYmI5YjM3Y2I3IiwidXNlcl9pZCI6NH0.cgazpVcUqEKNdqdJX6GMQ9Y1hbtzU-4QI9ZKAA_zNY8",
									"type": "string"
								}
							]
						},
						"method": "PUT",
						"header": [],
						"body": {
							"mode": "raw",
							"raw": "{\n    \"question\":\"hello\",\n    \"answer\":\"jalskdjfalkjsfdalkjdf\"\n}",
							"options": {
								"raw": {
									"language": "json"
								}
							}
						},
						"url": {
							"raw": "{{local}}admin/update-question/1",
							"host": [
								"{{local}}admin"
							],
							"path": [
								"update-question",
								"1"
							]
						}
					},
					"response": []
				},
				{
					"name": "delete-quesitions-ans",
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE0NjMxNzIxLCJpYXQiOjE3MTQ1NDUzMjEsImp0aSI6ImUyNWU4NGQ1NzJmMTRiYjZiYmE4YjAxYmI5YjM3Y2I3IiwidXNlcl9pZCI6NH0.cgazpVcUqEKNdqdJX6GMQ9Y1hbtzU-4QI9ZKAA_zNY8",
									"type": "string"
								}
							]
						},
						"method": "DELETE",
						"header": [],
						"url": {
							"raw": "{{local}}admin/delete-question/1",
							"host": [
								"{{local}}admin"
							],
							"path": [
								"delete-question",
								"1"
							]
						}
					},
					"response": []
				}
			]
		},
		{
			"name": "Ratings",
			"item": [
				{
					"name": "Add rating",
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE2MzQxOTQxLCJpYXQiOjE3MTYyNTU1NDEsImp0aSI6Ijg4OTIxMjNhOWZhMTQ0MGFiNTRkYjExNDNjZjgxZWFmIiwidXNlcl9pZCI6Mzd9.yLexBq34FICippJyHsPq9U42PR3zCTYSuk1VUC7BZaQ",
									"type": "string"
								}
							]
						},
						"method": "POST",
						"header": [],
						"body": {
							"mode": "raw",
							"raw": "{\r\n    \"talent\": 38,\r\n    \"booking\": 6,\r\n    \"best_liked\": 1,\r\n    \"review\": \"he has done great\",\r\n    \"rating\": 5\r\n}",
							"options": {
								"raw": {
									"language": "json"
								}
							}
						},
						"url": {
							"raw": "{{local}}ratings",
							"host": [
								"{{local}}ratings"
							]
						}
					},
					"response": []
				},
				{
					"name": "get user ratings",
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE2MjEwODQ1LCJpYXQiOjE3MTYxMjQ0NDUsImp0aSI6ImMzZWRlNmZjMmQxYzRhMTI4MmJhZjFlNzU5NzlkMTE4IiwidXNlcl9pZCI6Mzd9.EIXwP_2IuCX2mjH8exvdyUuyi3YT-TwEfpMpjzLvl38",
									"type": "string"
								}
							]
						},
						"method": "GET",
						"header": [],
						"url": {
							"raw": "{{local}}user-ratings/38",
							"host": [
								"{{local}}user-ratings"
							],
							"path": [
								"38"
							]
						}
					},
					"response": []
				}
			]
		},
		{
			"name": "media",
			"item": [
				{
					"name": "media upload",
					"request": {
						"method": "POST",
						"header": [],
						"body": {
							"mode": "formdata",
							"formdata": [
								{
									"key": "media\n",
									"type": "file",
									"src": [
										"/C:/Users/dell/Downloads/skin_dataset/DATASET/train/acne/2.jpg",
										"/C:/Users/dell/Downloads/skin_dataset/DATASET/train/acne/3.jpg"
									]
								}
							]
						},
						"url": {
							"raw": "{{local}}media",
							"host": [
								"{{local}}media"
							]
						}
					},
					"response": []
				}
			]
		},
		{
			"name": "Terms-And-Conditions Copy",
			"item": [
				{
					"name": "add TAC",
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE2MDA5OTA1LCJpYXQiOjE3MTU5MjM1MDUsImp0aSI6ImYzNTNlOWZkZGYwODQ0YTc4OGE4ZmM5Nzc5OGVhYzdmIiwidXNlcl9pZCI6MX0.3KlELASp_lVFNcTBsJTSol1KyiLzTQCXiu72vNkXUNU",
									"type": "string"
								}
							]
						},
						"method": "PUT",
						"header": [],
						"body": {
							"mode": "raw",
							"raw": "{\n    \"data\":\"ajsdhfkljah\"\n}",
							"options": {
								"raw": {
									"language": "json"
								}
							}
						},
						"url": {
							"raw": "{{local}}admin/terms-and-condition",
							"host": [
								"{{local}}admin"
							],
							"path": [
								"terms-and-condition"
							]
						}
					},
					"response": []
				},
				{
					"name": "update TAC",
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE0ODA1MDEyLCJpYXQiOjE3MTQ3MTg2MTIsImp0aSI6IjVmMjc5ODgyNDc4ZjQzNWFiYTRlZDI3NWE0MDVjNzA4IiwidXNlcl9pZCI6Mn0.Iw0rhsAWsxr55gLrjxwDbnttfp-G-wctqtOVOvxuKHk",
									"type": "string"
								}
							]
						},
						"method": "PUT",
						"header": [],
						"body": {
							"mode": "raw",
							"raw": "{\n    \"data\":\"testing1234\"\n}",
							"options": {
								"raw": {
									"language": "json"
								}
							}
						},
						"url": {
							"raw": "{{local}}admin/update-terms-and-conditions/1",
							"host": [
								"{{local}}admin"
							],
							"path": [
								"update-terms-and-conditions",
								"1"
							]
						}
					},
					"response": []
				},
				{
					"name": "get-TAC",
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE2MDA5OTA1LCJpYXQiOjE3MTU5MjM1MDUsImp0aSI6ImYzNTNlOWZkZGYwODQ0YTc4OGE4ZmM5Nzc5OGVhYzdmIiwidXNlcl9pZCI6MX0.3KlELASp_lVFNcTBsJTSol1KyiLzTQCXiu72vNkXUNU",
									"type": "string"
								}
							]
						},
						"method": "GET",
						"header": [],
						"url": {
							"raw": "{{local}}terms-and-conditions-show",
							"host": [
								"{{local}}terms-and-conditions-show"
							]
						}
					},
					"response": []
				},
				{
					"name": "add-privacy",
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE2MDA3NTkzLCJpYXQiOjE3MTU5MjExOTMsImp0aSI6ImJkYjkxMzBiZDBmZjRhZGRhYmJmNWQ3NmJkM2EyNDJmIiwidXNlcl9pZCI6MX0.dTmhxx3ZP_JAni1fB2OOnMj1wP0eDTLHydNO4A8N3iU",
									"type": "string"
								}
							]
						},
						"method": "PUT",
						"header": [],
						"body": {
							"mode": "raw",
							"raw": "{\n    \"privacy_policy\":\"kakjdshf\"\n}",
							"options": {
								"raw": {
									"language": "json"
								}
							}
						},
						"url": {
							"raw": "{{local}}admin/add-privacy-policy",
							"host": [
								"{{local}}admin"
							],
							"path": [
								"add-privacy-policy"
							]
						}
					},
					"response": []
				},
				{
					"name": "get-policy",
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE2MDA5OTA1LCJpYXQiOjE3MTU5MjM1MDUsImp0aSI6ImYzNTNlOWZkZGYwODQ0YTc4OGE4ZmM5Nzc5OGVhYzdmIiwidXNlcl9pZCI6MX0.3KlELASp_lVFNcTBsJTSol1KyiLzTQCXiu72vNkXUNU",
									"type": "string"
								}
							]
						},
						"method": "GET",
						"header": [],
						"url": {
							"raw": "{{local}}admin/get-policy",
							"host": [
								"{{local}}admin"
							],
							"path": [
								"get-policy"
							]
						}
					},
					"response": []
				}
			]
		},
		{
			"name": "customer support",
			"item": [
				{
					"name": "add-contact-us",
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE2MDA3NTkzLCJpYXQiOjE3MTU5MjExOTMsImp0aSI6ImJkYjkxMzBiZDBmZjRhZGRhYmJmNWQ3NmJkM2EyNDJmIiwidXNlcl9pZCI6MX0.dTmhxx3ZP_JAni1fB2OOnMj1wP0eDTLHydNO4A8N3iU",
									"type": "string"
								}
							]
						},
						"method": "PUT",
						"header": [],
						"body": {
							"mode": "raw",
							"raw": "{\n    \"name\":\"john\",\n    \"country_code\":\"+91\",\n    \"phone_no\":\"123456799\"\n}",
							"options": {
								"raw": {
									"language": "json"
								}
							}
						},
						"url": {
							"raw": "{{local}}admin/add-contact-us",
							"host": [
								"{{local}}admin"
							],
							"path": [
								"add-contact-us"
							]
						}
					},
					"response": []
				},
				{
					"name": "New Request",
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE2MDA5OTA1LCJpYXQiOjE3MTU5MjM1MDUsImp0aSI6ImYzNTNlOWZkZGYwODQ0YTc4OGE4ZmM5Nzc5OGVhYzdmIiwidXNlcl9pZCI6MX0.3KlELASp_lVFNcTBsJTSol1KyiLzTQCXiu72vNkXUNU",
									"type": "string"
								}
							]
						},
						"method": "GET",
						"header": [],
						"url": {
							"raw": "{{local}}admin/get-contact-us",
							"host": [
								"{{local}}admin"
							],
							"path": [
								"get-contact-us"
							]
						}
					},
					"response": []
				}
			]
		},
		{
			"name": "Chat",
			"item": [
				{
					"name": "all chats",
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE3MDQ5MDczLCJpYXQiOjE3MTY5NjI2NzMsImp0aSI6IjA2MGEwNGIxN2I5YTQ2OWE5ZDA5YmU1MmViYTQyMzJmIiwidXNlcl9pZCI6Mzd9.LStLuU4KrXVWh2q7jyMrarhwUY89fcA07F2CgY5ZA84",
									"type": "string"
								}
							]
						},
						"method": "GET",
						"header": [],
						"url": {
							"raw": "{{local}}all-chats",
							"host": [
								"{{local}}all-chats"
							]
						}
					},
					"response": []
				},
				{
					"name": "conversation",
					"request": {
						"auth": {
							"type": "bearer",
							"bearer": [
								{
									"key": "token",
									"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE2NzQwMzUzLCJpYXQiOjE3MTY2NTM5NTMsImp0aSI6ImE2MjYwZDdkZjk2YjQ2YjdiMDIwNTk4ZmYzZTU2MjlkIiwidXNlcl9pZCI6Mzh9.FzZhT-m0hhqCAJsz94FhwP6uCDMJ3AyGAVbAztOLFIA",
									"type": "string"
								}
							]
						},
						"method": "GET",
						"header": [],
						"url": {
							"raw": "{{local}}conversation/7",
							"host": [
								"{{local}}conversation"
							],
							"path": [
								"7"
							]
						}
					},
					"response": []
				}
			]
		},
		{
			"name": "New Request",
			"request": {
				"method": "GET",
				"header": [],
				"url": {
					"raw": ""
				}
			},
			"response": []
		}
	]
}
