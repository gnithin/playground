// Just trying out express. Not needed for this thing
/*
var express = require('express');
app = express();

app.get('/', function(req, res){
    console.log('At /');
    res.send('hello');
})

// This doesn't seem to work as expected.
app.listen(
    3000,
    function(){
        console.log("Listening at 3000");
    }
)
*/
var g = require('ger');
var esm = new g.MemESM();
var ger = new g.GER(esm);

ger.initialize_namespace('movies')
.then( function() {
  return ger.events([
    {
      namespace: 'movies',
      person: 'bob',
      action: 'likes',
      thing: 'xmen',
      expires_at: '2020-06-06'
    },
    {
      namespace: 'movies',
      person: 'bob',
      action: 'likes',
      thing: 'avengers',
      expires_at: '2020-06-06'
    },
    {
      namespace: 'movies',
      person: 'alice',
      action: 'likes',
      thing: 'xmen',
      expires_at: '2020-06-06'
    },
  ])
})
.then( function() {
  // What things might alice like?
  return ger.recommendations_for_person('movies', 'alice', {actions: {likes: 1}})
})
.then( function(recommendations) {
  console.log("\nRecommendations For 'alice'")
  console.log(JSON.stringify(recommendations,null,2))
})
.then( function() {
  // What things are similar to xmen?
  return ger.recommendations_for_thing('movies', 'xmen', {actions: {likes: 1}})
})
.then( function(recommendations) {
  console.log("\nRecommendations Like 'xmen'")
  console.log(JSON.stringify(recommendations,null,2))
})
