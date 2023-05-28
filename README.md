# Raamatukogu

## Description
We are making simple library "database". It will remember librarys, members of those librarys, rentable object of those librarys and late fees. We will also add basic GUI if we have enough time for that. <br />
We are usining Pivotal Tracker for version control.

Datastorage: Mongodb

### Needed python librarys: <br />
* PyMongo


## Members and there rolls.
* Jürmo Mihhailov - Leader and coder
* Aaron Aivo Alev - Coder
* Aimar Kiivits - Coder

# Database example
### Library collection
```
{
  "_id":{"$oid":"643849a059fb70c4f796b652"},
  "name":"Marten lib",
  "rentables":[
      {"type":"book",
      "name":"sus",
      "amount":{"$numberInt":"999975"},
      "popularity":{"$numberInt":"10"}}
      ] 
}
```

__Work on this has been stoped__
