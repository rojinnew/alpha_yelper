from py2neo import Graph, Path
from py2neo.packages.httpstream import http
from collections import defaultdict
import networkx as nx
import csv
import operator

yelp_graph = Graph()
graph = nx.DiGraph()
http.socket_timeout = 9999

def get_alphainf(uid):
    return yelp_graph.cypher.execute("MATCH (u1)-[:friends_with]->(u2) WHERE u1.user_id={uid} MATCH (u1)-[r1:reviewed]->(b:Business)<-[r2:reviewed]-(u2) WHERE r1.date < r2.date AND r2.date < (r1.date + 14*24*60*60) RETURN count(r2) AS influences", {"uid":uid})

def get_allreviews(bid):
    return yelp_graph.cypher.execute("MATCH (u:User)-[r:reviewed]->(b:Business) WHERE b.business_id={bid} RETURN u.elite AS elite, r.stars AS rrate", {"bid":bid})

def get_business(uid):
    return yelp_graph.cypher.execute("MATCH (u:User)-[r:reviewed]->(b:Business) WHERE u.user_id={uid} RETURN b.business_id AS bid, b.city AS city, b.stars AS arate, r.stars AS rrate", {"uid":uid})

def get_influence():
    return yelp_graph.cypher.execute("MATCH (u1)-[:friends_with]->(u2) WITH u1, u2 ORDER BY id(u1) DESC MATCH (u1)-[r1:reviewed]->(b:Business)<-[r2:reviewed]-(u2) WHERE r1.date < r2.date AND r2.date < (r1.date + 14*24*60*60) RETURN u2.user_id AS uid2, u1.user_id AS uid1")

if __name__ == "__main__":

  e_list = get_influence()
  for e in e_list:
     graph.add_edge(e.uid1, e.uid2)

  alpha=[]
  pgrank=[]
  page_rank = nx.pagerank(graph)
  for key, value in sorted(page_rank.iteritems(), key=lambda (k,v): (v,k)):
     alpha.append(key)
     pgrank.append(value)
  alpha.reverse()
  pgrank.reverse()

  print "Top Ranked Alphas:"
  cumalpha=0.0
  cumelite=0.0
  for index in range(0,10):
    uid = alpha[index]
    diff = 0.0
    diff2 = 0.0
    b_list = get_business(uid)
    d = defaultdict(int)
    for b in b_list:
      d[b.city] += 1
      fa = float(b.arate)
      fb = float(b.rrate)
      diff += abs(fa - fb)
      b_reviews = get_allreviews(b.bid)
      fe = 0.0
      count = 0.0
      diff3 = 0.0
      for r in b_reviews:
	if(r.elite is not None):
	  fe = float(r.rrate)
	  diff3 += abs(fa - fe)
	  count += 1.0
      if(count is not 0.0):
	diff2 += diff3/count
    max=0
    for item in d:
      if d[item] > max:
	max = d[item]
	city = item
    print "alpha #" + str(index) + " UserID: " + str(uid) + " City: " + str(city) 
    cumalpha+=diff/(5.0*len(b_list))
    cumelite+=diff2/(5.0*len(b_list))
  print "Alpha's Average Rating Inaccuracy: " + str(cumalpha/10.0)
  print "Elite's Average Rating Inaccuracy: " + str(cumelite/10.0)
