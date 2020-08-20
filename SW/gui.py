from py2neo import Graph, Path
from py2neo.packages.httpstream import http
import networkx as nx
import csv
import codecs

yelp_graph = Graph()
graph = nx.DiGraph()
http.socket_timeout = 9999

def get_business_count_vegas(a,c,s):
	
	return yelp_graph.cypher.execute("MATCH (u:User)-[r:reviewed]->(b:Business) WHERE u.user_id='"+a+"' AND r.stars='5' AND b.city='"+c+"' AND b.state='"+s+"' RETURN b.business_id as bid, b.name as name, b.categories as categories, b.stars as stars, b.latitude as latitude, b.longitude as longitude, b.full_address as full_address, b.`attributes.Price Range` as price, b.`attributes.Takes Reservations` as reservation, b.`hours.Monday.open` as hours_Monday_open, b.`hours.Monday.close` as hours_Monday_close,b.`hours.Tuesday.open` as hours_Tuesday_open, b.`hours.Tuesday.close` as hours_Tuesday_close , b.`hours.Wednesday.open` as hours_Wednesday_open , b.`hours.Wednesday.close` as hours_Wednesday_close , b.`hours.Thursday.open` as hours_Thursday_open,  b.`hours.Thursday.close` as  hours_Thursday_close,b.`hours.Friday.open` as hours_Friday_open, b.`hours.Friday.close` as hours_Friday_close,b.`hours.Saturday.open` as hours_Saturday_open, b.`hours.Saturday.close` as hours_Saturday_close, b.`hours.Sunday.open` as hours_Sunday_open, b.`hours.Sunday.close` as  hours_Sunday_close, b.`attributes.Parking.lot` as parking ,b.`attributes.Wi-Fi` as wifi,r.stars as alpha_rating,r.review_id as rid,r.text as text, r.date as date order by b.id asc, r.date desc")

def check(x):
	if(x is None): 
		return  None
	else:
		return x.encode('utf-8') 
if __name__ == "__main__":
   alpha_list = [{ "alpha":  "WmAyExqSWoiYZ5XEqpk_Uw", "city": "Las Vegas","state" : "NV"}, 
  			{ "alpha":  "fczQCSmaWF78toLEmb0Zsw", "city": "Phoenix","state" : "AZ"}, 
  			{ "alpha":  "nEYPahVwXGD2Pjvgkm7QqQ", "city": "Pittsburgh","state" : "PA"}, 
  			{ "alpha":  "CvMVd31cnTfzMUsHDXm4zQ", "city": "Charlotte","state" : "NC"} 
		]
	
   index=0
   while (index < 4):
	business_list=[]
  	business_list = get_business_count_vegas(alpha_list[index]["alpha"], 
						 alpha_list[index]["city"],
						 alpha_list[index]["state"])
  	i = 0 
  	cat = []
  	fieldnames = ['id', 'name', 'categories','stars', 'latitude', 'longitude','full_address',
		      'price','reservation','hours_Monday_open',  'hours_Monday_close', 'hours_Tuesday_open',
		      'hours_Tuesday_close' , 'hours_Wednesday_open' , 'hours_Wednesday_close' , 'hours_Thursday_open',
		      'hours_Thursday_close', 'hours_Friday_open','hours_Friday_close', 'hours_Saturday_open', 
		      'hours_Saturday_close',  'hours_Sunday_open', 'hours_Sunday_close', 'parking', 'wifi',
		      'alpha_rating','rid','text']
  	category_type = []
  	c = 0
  	with open('./AlphaSelects/guidata/b_info_'+ alpha_list[index]["state"]+'.csv', 'w') as csvfile:
    		writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quotechar='"', quoting=csv.QUOTE_MINIMAL)
    		writer.writeheader()
    		b_id_list = []
    		while( i < len(business_list)):
      			bid = business_list[i].bid
      			if(bid not in b_id_list):
      				b_id_list.append(bid)
				name =business_list[i].name
        			if business_list[i].categories is not None:
					if ("Restaurants" in business_list[i].categories):
						category_type.append(business_list[i].categories)
	   					cat =  '|'.join(business_list[i].categories)
	   					stars = business_list[i].stars
	   					lat = business_list[i].latitude
	   					lng = business_list[i].longitude
	   					full_address = business_list[i].full_address
	   					price = business_list[i].price
	   					reservation = business_list[i].reservation
	   					if(reservation == 'True'):
							reservation = 'Yes'
	  					else: 
							reservation ='No'
	   					if(business_list[i].parking == "True"):
							parking = "Yes"
	   					else:
							parking = "No"
		
	   					if(business_list[i].wifi == "free"):
							wifi = "Yes"
	   					else:
							wifi = "No"
						rid = business_list[i].rid
						text = business_list[i].text
	   					counter = 0
	   					hours_Monday_open = business_list[i].hours_Monday_open
	   					if(hours_Monday_open!=None) :
							counter =counter+1
	   					hours_Monday_close = business_list[i].hours_Monday_close
	   					hours_Tuesday_open = business_list[i].hours_Tuesday_open
	   					if(hours_Tuesday_open!=None):
		 					counter =counter+1
	   					hours_Tuesday_close = business_list[i].hours_Tuesday_close
	   					hours_Wednesday_open = business_list[i].hours_Wednesday_open 
	   					if(hours_Wednesday_open!=None):
		 					counter =counter+1
	   					hours_Wednesday_close = business_list[i].hours_Wednesday_close
	  					hours_Thursday_open = business_list[i].hours_Thursday_open
	   					if(hours_Thursday_open!=None):
		 					counter =counter+1
	   					hours_Thursday_close = business_list[i].hours_Thursday_close
	   					hours_Friday_open = business_list[i].hours_Friday_open
	   					if(hours_Friday_open!=None):
		 					counter =counter+1
	   					hours_Friday_close = business_list[i].hours_Friday_close	
	   					hours_Saturday_open = business_list[i].hours_Saturday_open
	   					if(hours_Saturday_open!=None):
		 					counter =counter+1
	   					hours_Saturday_close = business_list[i].hours_Saturday_close
	   					hours_Sunday_open = business_list[i].hours_Sunday_open
	   					if(hours_Sunday_open!=None):
		 					counter =counter+1
	   					hours_Sunday_close = business_list[i].hours_Sunday_close
	   					alpha_rating = business_list[i].alpha_rating
						if(counter!=0):
  	   						#writer[index].writerow({'id': bid.encode('utf-8'),
  	   						writer.writerow({'id': bid.encode('utf-8'),
									 'name': name.encode('utf-8'),
									 'categories': cat.encode('utf-8'),
									 'stars': stars.encode('utf-8'),
									 'latitude': lat,
									 'longitude': lng ,
									 'full_address':full_address.encode('utf-8'),
									 'price':price,
									 'reservation':reservation,
									 'hours_Monday_open':check(hours_Monday_open),
									 'hours_Monday_close':check(hours_Monday_close),
									 'hours_Tuesday_open':check(hours_Tuesday_open),
									 'hours_Tuesday_close':check(hours_Tuesday_close) ,
									 'hours_Wednesday_open':check(hours_Wednesday_open) ,
									 'hours_Wednesday_close':check(hours_Wednesday_close),
									 'hours_Thursday_open':check(hours_Thursday_open),
									 'hours_Thursday_close':check(hours_Thursday_close), 
									 'hours_Friday_open':check(hours_Friday_open), 
									 'hours_Friday_close':check(hours_Friday_close),
									 'hours_Saturday_open':check(hours_Saturday_open),
									 'hours_Saturday_close':check(hours_Saturday_close),
									 'hours_Sunday_open':check(hours_Sunday_open),
									 'hours_Sunday_close':check(hours_Sunday_close),
									 'parking': parking,
									 'wifi':wifi,
									 'alpha_rating':alpha_rating,
									 'rid':rid,
									 'text':text.encode('utf-8')})
      			i = i +1 

 	index = index + 1
