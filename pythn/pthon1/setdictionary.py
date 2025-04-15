d={
  "name": "John",
  "Age": 32,
  "Address": {
    "city": "Hyderabad",
    "state": "Telangana"
  },
  "Projects": [
    {
      "description": "project 1",
      "tech stack": "Java"
    },
    {
      "description": "project 2",
      "tech stack": "Python"
    },
    {
      "description": "project 3",
      "tech stack": "C#"
    }
  ]
}

w=d["Projects"]
print(w)
for i in w:
    print(i["description"])

