# django-graphql-sample
## using library, tool
- django
- graphene-django

 ## attention
 - django secret key is written in local_setting.py, but file isn't commited. So it should be placed in django-website-capture/sampleproj and secret key is written in this file.

 ## preparation
 the following two steps should be executed before.
 - python manage.py makemigration
 - python manage.py migrate

 ## query
 - Item objects can be searched.
 - get all item
 ```
query {
  items {
    name,
    count,
    id
  }
}
 ```
 - get specified item
  ```
 query {
  item (id: 1) {
    name,
    count,
    id
  }
}
 ```

 ## mutation
  - create specified item
 ```
mutation {
  createItem(name:"orange", count:3) {
    item {
      name
      count
    }
  }
}
 ```
 - update specified item
 ```
mutation {
  updateItem(id:1, name:"grape", count:4) {
    item {
      id
      name
      count
    }
  }
}
 ```
 - delete specified item
  ```
mutation {
  deleteItem(id:1) {
    item {
      id
    }
  }
}
 ```