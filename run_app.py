from classList import User
import dbFacade
import sys
import json

# data = {
# 	"table" : "user",
# 	"fields" : {
# 		"id" : "",
# 		"name" : "Robby",
# 		"surname" : "Murrey",
# 		"age" : "50"
# 	},
# 	"method" : "insert"
# }

inputfile = sys.argv[1]
with open(inputfile) as f:
	data = json.load(f)


user = User(data["table"], data["fields"], data["method"])
db = dbFacade.Facade().dbChoise()
db.run(user)



