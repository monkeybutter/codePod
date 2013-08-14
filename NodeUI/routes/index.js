var mongo=require('mongodb');

var Server = mongo.Server,
    Db = mongo.Db,
    BSON = mongo.BSONPure;
  
var server = new Server('localhost', 27017, {auto_reconnect: true});
db = new Db('solarPod', server);
 
db.open(function(err, db) {
   if(!err) {
     console.log("Connected to solarPod database");
   }
});

exports.index = function(req, res){
  res.render('index.html');
};


exports.findDateRange = function(req, res){
   var station = "Namadgi School"
   var params = req.body;
   console.log(params);
   
   db.collection('obs', function(err, collection) {
       collection.find({"name": station}, {"sort": [['field1','asc']]}, {"limit": 1}, function(err, cursor) {
          cursor.toArray(function(err, items) {
	         res.json(items);
	         res.end();
	      }); 
	   }); 
   }); 
};


exports.findObsByInterval = function(req, res){
   var station = "Namadgi School"
   var date1 = new Date(2012, 6, 1, 0, 0, 0, 0);
   var date2 = new Date(2012, 7, 1, 0, 0, 0, 0);
   var params = req.body;

   console.log(params);
   
   db.collection('obs', function(err, collection) {
       collection.find({"name": station, "date": { $gt: date1, $lte: date2 } }, function(err, cursor) {
          cursor.toArray(function(err, items) {
	         res.json(items);
	         res.end();
	      }); 
	   }); 
   }); 
};